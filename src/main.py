import openai
import speech_to_text.InputUserVoice as iuv
import os
import threading

def init_openai_api():
    with open('secret/OPENAI_API', 'r') as secret_file:
        openai.api_key = secret_file.read()

if __name__ == '__main__':
    init_openai_api()
    user_input = iuv.InputUserVoice()
    MAX_SECONDS = 3

    print('Enter r to record audio, x to exit process')
    while 1:
        inp = input('Type: ')
        if inp == 'r':
            os.system('clear')
            record_thread = threading.Thread(target=user_input.record_audio, args=[MAX_SECONDS])
            # user_input.record_audio(length_in_seconds=MAX_SECONDS)
            record_thread.start() #run thread
            inp2 = input('Enter return to stop')
            user_input.stop_recording()
            out = user_input.get_output_text()
            print('output of the speech: {0}'.format(out))
        elif inp == 'x':
            print('exit process')
            break
        else:
            print('invalid character')

