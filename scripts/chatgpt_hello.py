import requests
import sys

def get_api_key(file_path):
    with open(file_path, 'r') as file:
        api_key = file.read().strip()
    return api_key

def get_chatgpt_answer(query, api_key):
    # Make a request to the ChatGPT API
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    params = {
        'model': 'gpt-4o',
        'messages': [{"role": "user", "content": query}],
        'temperature': 0.5,
    }
    response = requests.post('https://api.openai.com/v1/chat/completions', json=params, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(
            f"Failed to get a successful response from ChatGPT API. "
            f"Status code: {response.status_code}. "
            f"Response body: {response.text}"
        )

api_key_file_path = sys.argv[1]
api_key = get_api_key(api_key_file_path)

query = "こんにちは、元気ですか？"
answer = get_chatgpt_answer(query, api_key)
if answer:
    print(answer)
else:
    print("Failed to get an answer from ChatGPT API.")