import csv
import json
import os

folder_path = r'C:\Users\91745\OneDrive\Desktop\stg_hackathon\data\output_js'
csv_file_path = r'C:\Users\91745\OneDrive\Desktop\stg_hackathon\utils\Audit_report.csv'

headers = [
    "Date & Time", "Machine Name", "Process Name", "Process Start Time", 
    "Process End Time", "Candidate Name", "Details (As JSON)", 
    "Status", "Exception", "Remarks"
]

def write_to_csv(candidate_name, json_data, file_name):
    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)

        if file.tell() == 0:
            writer.writeheader()

        writer.writerow({
            "Date & Time": "",
            "Machine Name": file_name,
            "Process Name": "",
            "Process Start Time": "",
            "Process End Time": "",
            "Candidate Name": candidate_name,
            "Details (As JSON)": json.dumps(json_data),
            "Status": "",
            "Exception": "",
            "Remarks": ""
        })

for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)

    if file_name.endswith('.txt'):
        with open(file_path, 'r') as txt_file:
            json_content = txt_file.read().strip()
            try:
                json_data = json.loads(json_content)
                candidate_name = json_data.pop("name", "Unknown")
                write_to_csv(candidate_name, json_data, file_name)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON in file {file_name}: {e}")
