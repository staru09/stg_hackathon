
# OCR 

```shell
python ocr.py
```
This will take input from data/form images and will pereform OCR on these images.
<br> The output will be saved in data/output as txt files.



# LLM + Form Fill

## Llama Model

https://huggingface.co/hugging-quants/Llama-3.2-3B-Instruct-Q4_K_M-GGUF?show_file_info=llama-3.2-3b-instruct-q4_k_m.gguf

## Running inference

install (llama-cpp-python)[https://github.com/abetlen/llama-cpp-python]

This will convert our text extracted from ocr into json files which can be used to fill microsoft forms.

```shell
python infer.py
```

Output json will be written in `./output_js`

## Running form filling automation

Node.js is required

```shell
npm i
node form_fill.js
```

## Audit Report Generation

From the json data we tried to create a new csv file as our audit report 

```shell
python audit.py
```

## Audit Report Sender

```shell
python send_mail.py
```

This will share the generated audit report with the HR managers.
