# STG Hackathon LLM + Form Fill

## Cloning

```shell
git clone <repo> --recursive
```

## Llama Model

https://huggingface.co/hugging-quants/Llama-3.2-3B-Instruct-Q4_K_M-GGUF?show_file_info=llama-3.2-3b-instruct-q4_k_m.gguf

## Running inference

install (llama-cpp-python)[https://github.com/abetlen/llama-cpp-python]

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