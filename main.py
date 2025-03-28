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