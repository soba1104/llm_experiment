import tiktoken
import sys

def count_chatgpt4o_token(text):
    enc = tiktoken.encoding_for_model("gpt-4o")
    tokens = enc.encode(text)
    return len(tokens)

# sys.args からファイルパスを取得
path = sys.argv[1]
with open(path, 'r') as file:
    text = file.read()

token_count = count_chatgpt4o_token(text)
print(f'Total tokens in the file: {token_count}')