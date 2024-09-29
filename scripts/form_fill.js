import puppeteer from "puppeteer"
import fs from "fs/promises"
import { Page } from "puppeteer"


const formToJsonMap = {
    "Phone Number": "phone",
    "Job Title": "job_title",
    "Start Date": "start_date",
    "Location": "location",
    "Reporting Manager": "reporting_manager",
    "Email Address": "email",
    "Applicant's Legal Name": "name",
    "Department": "department"
}

const formUrl = "https://forms.office.com/pages/responsepage.aspx?id=Gv_-GtOKLEaCBt1iv8DZPhnYsvcioMFPnc1mAzJhzCZURUZBWDdPTUxXOFlSMjJCMTFER0MyRkcwNi4u&route=shorturl"

/**
 * 
 * @param {Page} page 
 * @param {*} jsonF 
 */
async function fillForm(page, jsonF) {
    const file = await fs.readFile(jsonF, {encoding: "utf-8"})
    const jsonData = JSON.parse(file)
    console.log("filling", jsonData)

    await page.goto(formUrl)
    const start = page.locator("#form-main-content1 button > div")
    await start.click();

    await page.locator("[data-automation-id=questionItem]").waitHandle();

    const questions = await page.$$("[data-automation-id=questionItem]")
    for (const question of questions) {
        console.log("answering question")
        /**
         * @type string
         */
        const input_field_raw = await question.$eval(".text-format-content", node => node.innerText)
        const input_field = input_field_raw.trim()
        console.log("input field", input_field)
        /**
         * @type string
         */
        let input_value;
        if (input_field == "Start Date") {
            const dateV = jsonData["start_date"]
            const [y, m, d] = dateV.split("-")
            input_value = `${m}/${d}/${y}`
        } else {
            input_value = jsonData[formToJsonMap[input_field]]
        }
        console.log("result", input_value)
        const input_el = await question.$("input")
        await input_el.type(input_value, {delay: 10})
    }
    await page.locator("button[data-automation-id=submitButton]").click()
    await page.locator("[data-automation-id=thankYouMessage]").waitHandle()
}

const browser = await puppeteer.launch({headless: false});
const page = await browser.newPage();

const formInputs = await fs.readdir("../data/output_js/");
for (const fileName of formInputs) {
    await fillForm(page, `../data/output_js/${fileName}`)
}

await browser.close()
