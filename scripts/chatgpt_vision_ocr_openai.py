import sys
import base64
from openai import OpenAI

def get_api_key(file_path):
    with open(file_path, 'r') as file:
        api_key = file.read().strip()
    return api_key

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

def recognize_image(iamge_path, api_key):
    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
    }

    messages = [{
        "role": "user",
        "content": [{
            "type": "text",
            "text": "この画像に写っているテキストを読み取って(英文の場合、大文字小文字の正規化もすること)。"
        }, {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
        }],
    }]

    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )
    return response.json()

api_key_file_path = sys.argv[1]
api_key = get_api_key(api_key_file_path)

image_path = sys.argv[2]
base64_image = encode_image(image_path)

print(recognize_image(image_path, api_key))
