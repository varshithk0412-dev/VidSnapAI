# 🎬 VidSnapAI

VidSnapAI is an AI-powered Flask web application that converts a set of uploaded images and a text description into a narrated video reel. The application uses the ElevenLabs Text-to-Speech API to generate realistic voiceovers and FFmpeg to combine images with the generated audio into a final MP4 reel.

## ✨ Features

- 📷 Upload multiple images
- 📝 Enter a custom narration
- 🔊 AI-generated voice using ElevenLabs
- 🎥 Automatic video generation using FFmpeg
- 🖼️ Gallery to view generated reels
- ⚙️ Background processing for reel creation

---

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **AI Voice:** ElevenLabs API
- **Video Processing:** FFmpeg
- **File Handling:** Werkzeug

---

## 📂 Project Structure

```
VidSnapAI/
│
├── static/
│   ├── css/
│   ├── reels/
│   └── ...
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── create.html
│   └── gallery.html
│
├── user_uploads/
│   └── <uuid>/
│       ├── image1.jpg
│       ├── image2.jpg
│       ├── desc.txt
│       ├── input.txt
│       └── narration.mp3
│
├── main.py
├── text_to_speech.py
├── video_generator.py
├── done.txt
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/VidSnapAI.git
cd VidSnapAI
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Install FFmpeg

Download FFmpeg from:

https://ffmpeg.org/download.html

Make sure `ffmpeg` is added to your system PATH.

Verify installation:

```bash
ffmpeg -version
```

---

### 5. Configure ElevenLabs API Key

Create an environment variable:

**Windows**

```bash
set ELEVENLABS_API_KEY=your_api_key
```

**Linux/macOS**

```bash
export ELEVENLABS_API_KEY=your_api_key
```

Alternatively, you can use a `.env` file.

---

## ▶️ Running the Project

Start the Flask server:

```bash
python main.py
```

Run the background processing script in another terminal:

```bash
python text_to_speech.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 🚀 How It Works

1. Upload one or more images.
2. Enter the narration text.
3. The images and description are saved in a unique folder.
4. The background worker:
   - Reads the description
   - Generates speech using ElevenLabs
   - Measures the audio duration
   - Creates an FFmpeg input file
   - Generates the final MP4 reel
5. The reel appears in the Gallery page.

---
