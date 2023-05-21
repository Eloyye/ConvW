import openai

def init_openai_api():
    with open('../secret/OPENAI_API', 'r') as secret_file:
        openai.api_key = secret_file.read()

if __name__ == '__main__':
    init_openai_api()

