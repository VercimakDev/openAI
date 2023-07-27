import requests
import json

openai_api_key = "xxx"

url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_api_key}"
}

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
    print("OpenAI:", result['choices'][0]['message']['content'])
else:
    print("Error:", response.status_code, response.text)