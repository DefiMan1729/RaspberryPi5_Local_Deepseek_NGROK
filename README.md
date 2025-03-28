# Serving LLMs Running Locally on Raspberry Pi Over Public Internet Using FastAPI and Ngrok

This repository provides a step-by-step guide to expose large language models (LLMs), such as Deepseek, running locally on a Raspberry Pi as APIs over the public internet. We use **FastAPI** to create the API endpoint and **Ngrok** to expose the localhost to a public URL.
<img width="1174" alt="Screenshot 2025-03-28 at 11 36 39 PM" src="https://github.com/user-attachments/assets/00289d40-f14c-4e71-bd55-e62dee5e3b21" />

## Prerequisites

- A Raspberry Pi device
- locally running LLM such as Deepseek (refer my previous github)
- Python installed on the Raspberry Pi
- Ngrok installed on your Pi
- Fast API installed on your Pi
- The `ollama` Python package installed for interacting with the AI model 

## Setup Instructions

### 1. Install Dependencies
Ensure you have the required Python libraries:
```bash
pip install fastapi uvicorn ollama
```
Refer ngrok webiste for installation details
```
curl -sSL https://ngrok-agent.s3.amazonaws.com/ngrok.asc \
	| sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null \
	&& echo "deb https://ngrok-agent.s3.amazonaws.com buster main" \
	| sudo tee /etc/apt/sources.list.d/ngrok.list \
	&& sudo apt update \
	&& sudo apt install ngrok
```
refer the requirements.tx file attached

### 2. Create the FastAPI Endpoint
Use the following Python code to create an API endpoint that interacts with the Deepseek model

```python
from fastapi import FastAPI
import ollama

app = FastAPI()
DESIRED_MODEL = 'deepseek-r1:1.5b'  # AI model to process the input

@app.get("/")
def read_root():
    return {"Message": "this message is served from Arka's Raspberry Pi"}

@app.get("/prompts/{prompt}")
def read_prompt(prompt: str):
    # Sending the request to the Ollama model
    response = ollama.chat(
        model=DESIRED_MODEL,
        messages=[
            {
                'role': 'user',
                'content': prompt  
            }
        ]
    )
    # Returning the response content
    return response['message']['content']
```

Save this file as `main.py`.

### 3. Run the FastAPI Server
Launch the FastAPI server using Uvicorn:
```bash
fastapi dev main.py
```
Note that the Swagger documentation for the API will be available at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs):
<img width="915" alt="Screenshot 2025-03-28 at 11 23 30 PM" src="https://github.com/user-attachments/assets/26453cdf-93c7-4f57-8654-f4ac001ef6cf" />

### 4. Set Up Ngrok
Expose your local FastAPI server to the public internet using Ngrok:
```bash
ngrok http http://127.0.0.1:8000
```
This command will provide you with a public URL that forwards requests to your local server running on port 8000.

<img width="844" alt="Screenshot 2025-03-28 at 11 26 24 PM" src="https://github.com/user-attachments/assets/f8f9a8da-1160-4c46-ac80-5dea4934319b" />


## License
This guide and code are provided under the MIT License.

---

Explore my repository for guides to running Deepseek and other models locally on Raspberry Pi 
