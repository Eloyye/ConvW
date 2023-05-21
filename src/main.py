import openai
import speech_to_text.InputUserVoice as iuv
import os

def init_openai_api():
    with open('secret/OPENAI_API', 'r') as secret_file:
        openai.api_key = secret_file.read()

if __name__ == '__main__':
    init_openai_api()
    user_input = iuv.InputUserVoice()

    print('Enter r to record audio, x to exit process')
    while 1:
        inp = input('Type: ')
        if inp == 'r':
            user_input.record_audio(length_in_seconds=3)
            out = user_input.get_output_text()
            print('output of the speech: {0}'.format(out))
        elif inp == 'x':
            print('exit process')
            break
        else:
            print('invalid character')

