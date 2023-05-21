import openai
import speech_to_text.InputUserVoice as iuv
import os

def init_openai_api():
    with open('secret/OPENAI_API', 'r') as secret_file:
        openai.api_key = secret_file.read()

if __name__ == '__main__':
    init_openai_api()
    user_input = iuv.InputUserVoice()
    # out_file = user_input.generate_random_audio_file(N=7)
    # print('output file name: {0}'.format(out_file))
    user_input.record_audio(length_in_seconds=3)
    out = user_input.get_output_text()
    print('output of the speech: {0}'.format(out))

