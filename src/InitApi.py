import openai
from elevenlabs import set_api_key


def init_openai_api():
    with open('secret/OPENAI_API', 'r') as secret_file:
        openai.api_key = secret_file.read()


def init_elevenlabs():
    with open('secret/ELEVENLABS_API', 'r') as elvn_file:
        key = elvn_file.read()
        set_api_key(key)
