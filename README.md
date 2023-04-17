# Features
- Sends OGG audio voice feature files directly from your computer to a Discord channel
- Does not require a smartphone
- It is also possible to reply to messages with voice, just edit the "message_reference"

![image](https://media.discordapp.net/attachments/739575553253834754/1097418237488140338/image.png?width=286&height=274)

# Requirements
- Python 3.x
- requests module

# Installation
1. Clone or download the repository.
2. Install the requests module using the following command in your terminal or command prompt:

pip install requests

3. Use the file named token.txt in the same directory as the script and paste your Discord token in it.

# Usage
1. Modify the filename to the audio name what do you want to send;
2. Set the channel_id variable to the ID of the Discord channel where you want to send the audio file;
3. Set the audio_length variable to the length of the audio file in seconds.
4. Run the script using the following command in your terminal or command prompt:

python audio_sender.py

# Notes
- This script was tested on Windows 10 and Python 3.9.5.
- Make sure that you have bot permissions to send messages and files in the channel specified by the channel_id variable.
- The waveform key in the json_data variable is a fake wave and can be edited if desired.

# Another versions:
- C#: https://github.com/Reiko69420/Discord-Mobile-Audio-Sender-Windows (From Reiko)

I know there is a way to improve the script using libraries like pydub but I didn't want to depend on pydub to do that.
Maybe I'll update sometime
to get the seconds of a song just multiply the minute value by 60, example: 4 minutes = 240 seconds in audio_legth