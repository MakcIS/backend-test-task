class ChannelEntity:
    def __init__(self, chat_bot_name:str, url:str, token:str, channel_id:str|None=None):
        self.channel_id = channel_id
        self.chat_bot_name = chat_bot_name
        self.url = url
        self.token = token
