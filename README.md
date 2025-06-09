# Anime Face Generator 🎨

Generate anime faces using a trained DCGAN model in TensorFlow/Keras.

## Features
- Random noise input ➝ face image output
- Hosted on Hugging Face Spaces
- Simple HTML + Flask setup

## Demo
👉 [Live Demo on Hugging Face](https://huggingface.co/spaces/madhavvishist/anime-face-generator)

## Screenshot
![screenshot](demo.png)

## How it works
1. DCGAN generates 64x64 anime faces
2. Flask exposes `/generate` endpoint
3. Frontend UI fetches and displays the face

## Run Locally
```bash
pip install -r requirements.txt
python app.py
