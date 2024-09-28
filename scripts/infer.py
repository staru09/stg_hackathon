from llama_cpp import Llama
import json
import glob
 
llm = Llama(
    model_path="./llama-3.2-3b-instruct-q4_k_m.gguf",
    n_gpu_layers=-1,  # Uncomment to use GPU acceleration
    # seed=1337,      # Uncomment to set a specific seed
    n_ctx=2048,       # Uncomment to increase the context window
)
 
raw_file = r"C:\Users\91745\OneDrive\Desktop\stg_hackathon\data\output\PEC Hackathon-1_merged_page-0001.txt"
input_data = []

for raw_file in glob.glob(r"C:\Users\91745\OneDrive\Desktop\stg_hackathon\data\output\PEC Hackathon-1*"):
    with open(raw_file, 'r') as f:
        input_data.append((raw_file, f.read()))
 
 
example_json = {
    "phone": "(123) 345-6789",
    "location": "SanFrancisco,CA",
    "reporting_manager": "James Torvalds",
    "job_title": "Pata Analyst",
    "start_date": "2024-10-02",
    "email": "example@gmail.com",
    "name": "Emmy Dave",
    "department": "Engineering",
    
}
example = json.dumps(example_json)
base_message = {
    "role": "system",
    "content": f"""You are a helpful assistant. I will give you raw output from paddleOCR extract information from the resume appropriatly 
    Your task is to specific entries from the raw text and output it in the example format:
    {example}
    Ensure that your output specifically follows the format of this example
    the format of the start date is YYYY-MM-DD
    Output only the JSON. NOTHING ELSE.
    """
}
schema = {
    "type": "object",
    "properties": {
        "phone": { "type": "string" },
        "location": { "type": "string" },
        "reporting_manager": { "type": "string" },
        "job_title": {"type": "string"},
        "start_date": {"type": "string"},
        "email": {"type": "string"},
        "name": {"type": "string"},
        "department": {"type": "string"}
    },
    "required": [
        "phone",
        "location",
        "reporting_manager",
        "job_title",
        "start_date",
        "email",
        "name",
        "department"
    ]
}
outputs = []
for (raw_file, data) in input_data:
    messages = [
        base_message,
        {
            "role": "user",
            "content": f"RAW OCR:\n{data}"
        }
    ]
     
    # Get the response from the Llama model
    resp = llm.create_chat_completion(
        messages=messages,
        response_format={
            "type": "json_object",
            "schema": schema
        },
        temperature=0.7
    )
     
    # Extract the assistant's reply
    assistant_reply = resp['choices'][0]['message']['content'].strip()
    outputs.append((raw_file, assistant_reply))

for (raw_file, out) in outputs:
    with open(raw_file.replace('input', 'output'), 'w') as f:
        f.write(out)
