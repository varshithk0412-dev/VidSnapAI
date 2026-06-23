import os
import time
from text_to_speech import text_to_speech_file
import subprocess

def get_audio_duration(audio_path):
    cmd = [
        "ffprobe",
        "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        audio_path
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    return float(result.stdout.strip())


def create_reel(folder):
    image_folder = f"user_uploads/{folder}"
    output_folder = f"static/reels/{folder}"
    os.makedirs(output_folder, exist_ok=True)

    audio_path = os.path.join(image_folder, "audio.mp3")

    images = sorted([
        f for f in os.listdir(image_folder)
        if f.lower().endswith((".jpg", ".jpeg", ".png"))
    ])

    if len(images) == 0:
        print("No images found.")
        return

    audio_duration = get_audio_duration(audio_path)
    image_duration = audio_duration / len(images)

    input_txt = os.path.join(image_folder, "input.txt")

    with open(input_txt, "w") as f:
        for img in images:
            f.write(f"file '{img}'\n")
            f.write(f"duration {image_duration}\n")

        f.write(f"file '{images[-1]}'\n")

    command = [
        "ffmpeg",
        "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", input_txt,
        "-i", audio_path,
        "-vf",
        "scale=1080:1920:force_original_aspect_ratio=decrease,"
        "pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black",
        "-c:v", "libx264",
        "-c:a", "aac",
        "-pix_fmt", "yuv420p",
        "-shortest",
        os.path.join(output_folder, "reel.mp4")
    ]

    subprocess.run(command, check=True)

def text_to_audio(folder) : 
    with open(os.path.join(f"user_uploads/{folder}/desc.txt"),"r") as f : 
        text = f.read()
    savepathfile = text_to_speech_file(text,folder)
 
if __name__ == "__main__" : 
    while True : 
        with open("done.txt","r") as f : 
            done_folders = {line.strip() for line in f}
        folders = os.listdir("user_uploads")
        for folder in folders : 
            if(folder not in done_folders) : 
                try : 
                    text_to_audio(folder)
                    create_reel(folder)
                    with open("done.txt","a") as f : 
                        f.write(folder + "\n")
                except Exception as e : 
                    print(e)
        time.sleep(10)