import speech_to_text.InputUserVoice as iuv
import threading

from src.InitApi import init_openai_api, init_elevenlabs
from src.chatgpt_client.ChatGPTClient import ChatGPTClient

from src.elevenlabs_client.ElevenLabsClient import ElevenLabsClient


if __name__ == '__main__':
    init_openai_api()
    init_elevenlabs()
    MAX_SECONDS = 5*60
    chat_client = ChatGPTClient()
    elevenlabs_client = ElevenLabsClient()
    print('Enter r to record audio, x to exit process')
    while 1:
        inp = input('Type: ')
        user_input = iuv.InputUserVoice()
        if inp == 'r':
            record_thread = threading.Thread(target=user_input.record_audio, args=[MAX_SECONDS])
            record_thread.start() #run thread
            inp2 = input('Enter return to stop')
            user_input.stop_recording()
            record_thread.join()
            out = user_input.get_output_text()
            print('You: {0}'.format(out))
            out_str = chat_client.send_message_to_chatGPT(out)
            print('ChatGPT: {0}'.format(out_str))
            elevenlabs_client.say(out_str)
            user_input.remove_input_sound_file()
        elif inp == 'c':
            message = input('What do you want to write to servant Arnold? : ')
            out_str = chat_client.send_message_to_chatGPT(message)
            print(out_str)
        elif inp == 'v':
            message = 'Hello everyone! This is totally not special'
            elevenlabs_client.say(message)
            print('must complete voice recording before hitting here')
        elif inp == 'x':
            print('exit process')
            user_input.terminate_audio_input()
            break
        else:
            print('invalid character')
