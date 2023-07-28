import os
import requests
import json
import logging

openai_api_key = "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"

url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_api_key}"
}

# Create 'logs' directory if it doesn't exist
logs_directory = os.path.join(os.path.dirname(__file__), "logs")
os.makedirs(logs_directory, exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=os.path.join(logs_directory, "application.log"),
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Get user input to fill the content
user_input = input("Input for OpenAI: ")

data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": user_input}],
    "temperature": 0.7
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    result = response.json()
    output = result['choices'][0]['message']['content']
    print("OpenAI:", output)
    logging.info(f"Input: {user_input}, Output: {output}")
else:
    print("Error:", response.status_code, response.text)
    logging.error(f"Error: {response.status_code}, {response.text}")