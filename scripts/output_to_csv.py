import csv

extracted_text = """
Form for Potential Candidates

1. Please complete this form for any potential new hire and email it to
hr@thesummitgrp.com, with the resume attached.

2. HR will issue an offer letter.

3. After acceptance of the offer letter, onboarding instructions will be
sent to the new hires, including background check and drug screen.

Contact Information-

Applicant’s Legal Name: John Smith
Email Address: john.smith@email.com
Phone Number: (123) 496-7890

Offer Letter Specifics-

Job Title: Software Engineer
Start Date: 2024-10-01
Location: New York, NY
Reports To: Sarah Thompson
Department: Engineering
"""

# Extract information from the OCR text
def extract_info(text):
    info = {}
    
    # Extract legal name
    if "Applicant’s Legal Name:" in text:
        info['Legal name'] = text.split("Applicant’s Legal Name:")[1].split('\n')[0].strip()
    
    # Extract email address
    if "Email Address:" in text:
        info['Email address'] = text.split("Email Address:")[1].split('\n')[0].strip()
    
    # Extract phone number
    if "Phone Number:" in text:
        info['Phone number'] = text.split("Phone Number:")[1].split('\n')[0].strip()
    
    # Extract job title
    if "Job Title:" in text:
        info['Job title'] = text.split("Job Title:")[1].split('\n')[0].strip()
    
    # Extract start date (joining date)
    if "Start Date:" in text:
        info['Joining date'] = text.split("Start Date:")[1].split('\n')[0].strip()
    
    # Extract location
    if "Location:" in text:
        info['Location'] = text.split("Location:")[1].split('\n')[0].strip()
    
    # Extract reporting manager
    if "Reports To:" in text:
        info['Reporting manager'] = text.split("Reports To:")[1].split('\n')[0].strip()
    
    # Extract department
    if "Department:" in text:
        info['Department'] = text.split("Department:")[1].split('\n')[0].strip()
    
    return info

# Extract the information from the OCR text
info_dict = extract_info(extracted_text)

# Specify the CSV file path
csv_file = r'C:\Users\91745\OneDrive\Desktop\Anaconda\Output\candidate_info.csv'

# Define the CSV headers
headers = ['Job title', 'Email address', 'Joining date', 'Legal name', 'Reporting manager', 'Location', 'Department', 'Phone number']

# Write the extracted information to the CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    
    # Write header
    writer.writeheader()
    
    # Write the extracted info as a row
    writer.writerow(info_dict)

print(f"Information successfully saved to {csv_file}")
