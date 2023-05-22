import os

import openai
class ChatGPTClient:
    def __init__(self,
                 messages=None,
                 model='gpt-3.5-turbo',
                 system_instruction='Do not mention that you are an AI language model. You are a human teaching English to'
                                    'an English Second Language Student.'):
        if messages is None:
            messages = []
        self.messages = messages # {'role': , 'content': }
        self.model = model
        self.system_instruction = system_instruction
        self.messages.append(self.get_user_content_dic(user_role='system', user_message=system_instruction))

    #start a new context of chat
    def reset_chat(self):
        self.messages = []
        self.messages.append(self.get_user_content_dic(user_role='system', user_message=self.system_instruction))

    def get_user_content_dic(self, user_role='user', user_message=''):
        return {"role": user_role, "content": user_message}

    #user sends user_message to chatGPT, and returns the output of the message
    def send_message_to_chatGPT(self, user_message):
        user_dic = self.get_user_content_dic(user_role='user', user_message=user_message)
        self.add_response_to_messages(user_dic)
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self.messages
        )
        message_response = self.extract_message(response)
        self.add_response_to_messages(message_response)
        out_content_response = self.extract_content(message_response)
        return out_content_response

    def extract_content(self, message):
        return message['content']
    def extract_message(self, response):
        obj = self.get_user_content_dic(user_role=response['choices'][0]['message']['role'],
                                        user_message=response['choices'][0]['message']['content'])
        return obj
    def add_response_to_messages(self, message):
        self.messages.append(message)