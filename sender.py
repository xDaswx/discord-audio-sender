import requests,random,os,json

filename = 'audio.ogg'
channel_id = 739575553253834754
audio_legth = 360 #IN SECONDS ONLY

#to get the seconds of a song just multiply the minute value by 60, example: 4 minutes = 240 seconds in audio_legth
#It is also possible to reply to messages with voice, just edit the "message_reference"

with open('token.txt','r') as token_config:
    if token_config:
        token = token_config.read()
    else:
        print('Token not found in token.txt')

def AudioSender():
    headers = {
        'User-Agent': 'Discord-Android/172024',
        'authorization': token,
        'x-super-properties': 'eyJvcyI6IkFuZHJvaWQiLCJicm93c2VyIjoiRGlzY29yZCBBbmRyb2lkIiwiZGV2aWNlIjoibXVuY2giLCJzeXN0ZW1fbG9jYWxlIjoicHQtQlIiLCJjbGllbnRfdmVyc2lvbiI6IjE3Mi4yNCAtIHJuIiwicmVsZWFzZV9jaGFubmVsIjoiZ29vZ2xlUmVsZWFzZSIsImRldmljZV92ZW5kb3JfaWQiOiIzZDk4NGYxYS02NTYwLTQ2ZjktOWZhNy0zNGU2YzEzNmQyNmUiLCJicm93c2VyX3VzZXJfYWdlbnQiOiIiLCJicm93c2VyX3ZlcnNpb24iOiIiLCJvc192ZXJzaW9uIjoiMzMiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo2OTY5Njk2OTY5Njk2LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsLCJkZXNpZ25faWQiOjB9',
        'Content-Type': 'application/json; charset=utf-8',
        'Host': 'discord.com',
        'Expect': '100-continue',
    }

    audio_location = open(filename)
    audio_location.seek(0, os.SEEK_END)
    json_data = {
        'files': [
            {
                'file_size': audio_location.tell(), #set audio size
                'filename': 'voice-message.ogg',
                'id': '20',
            },
        ],
    }

    req_audio = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/attachments', headers=headers, json=json_data)

    if (req_audio.status_code == 200):

        headers_send_audio = {'Content-Type': 'audio/ogg','Host': 'discord-attachments-uploads-prd.storage.googleapis.com'}

        with open(filename, 'rb') as f:
            file_content = f.read()

        file = requests.put(req_audio.json()['attachments'][0]['upload_url'],data=file_content,headers=headers_send_audio)

        if (file.status_code == 200):
            json_data = {
                'attachments': [
                    {
                        'duration_secs': audio_legth,
                        'filename': 'voice-message.ogg',
                        'id': '0',
                        'uploaded_filename': req_audio.json()["attachments"][0]["upload_filename"],
                        'waveform': 'AGZZZZZZZZFASDASDWFASDASDWFASDASDWFASDASDWFASDASDWAGZZZZZZZZAGZZZZZZZZ==', #Fake wave, just edit if you want
                    },
                    
                ],
                'channel_id': channel_id,
                'content': '',
                #"message_reference": { #Reply thing if needed
		        #"channel_id": channel_id,
		        #"message_id": "1097415244315365466"},
                'flags': 8192,
                'nonce': random.randint(262625563,862625563),
                'type': 0,
            }
            response = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers, json=json_data)
            print(json.dumps(response.json(), indent=3))
        else:
            print(file.text, "Error: ", file.status_code)
    else: 
        print(req_audio.status_code, "Error: ", req_audio.text)

AudioSender()