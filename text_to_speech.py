import os

from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

client = ElevenLabs(
    api_key = ELEVENLABS_API_KEY
)

def text_to_speech_file(text,folder) : 
    audio = client.text_to_speech.convert(
        text=text,
        voice_id="JBFqnCBsd6RMkjVDRZzb",  # "George" - browse voices at elevenlabs.io/app/voice-library
        model_id="eleven_v3",
        output_format="mp3_44100_128",
    )
    save_file_path = os.path.join(f"user_uploads/{folder}","audio.mp3")
    with open(save_file_path,"wb") as f : 
        for chunk in audio : 
            if chunk : 
                f.write(chunk)
    return save_file_path