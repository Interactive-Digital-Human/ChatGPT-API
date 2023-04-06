import openai
import json


def get_api_key():
    """
    {"api":"key"}
    :return openai_key
    """
    openai_key_file = './envs/openai_key.json'
    with open(openai_key_file, 'r', encoding='utf-8') as f:
        openai_key = json.loads(f.read())
    return openai_key['api']


openai.api_key = get_api_key()

# Example OpenAI python library request
MODEL = "gpt-3.5-turbo"
response = openai.ChatCompletion.create(
    model=MODEL,
    message=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Knock knock."},
        {"role": "assistant", "content": "Who's there?"},
        {"role": "user", "content": "Orange"},
    ],
    temperature=0,
)


def call_api(name):
    print(f'Testing, {name}')

    print(response)


if __name__ == '__main__':
    call_api('how to format inputs to ChatGPT models')
