# Audio Transcription Script

This script uses the [Hugging Face Transformers library](https://huggingface.co/transformers/) and the **Whisper model** to transcribe audio files into text. It processes the transcription by splitting the text into sentences based on punctuation marks and saves the result as a `.txt` file.

The script requires you to enter the path for the audio file you want to transcribe as the `file` variable at the beginning of the script.

## Features

- Transcribes `.mp3` audio files (with potential for extension to other formats).
- Handles transcription errors gracefully (e.g., file not found or transcription failure).
- Splits the transcription into sentences based on punctuation marks (`.`, `!`, `?`).
- Saves the transcription as a plain text file.

## Requirements

Make sure you have Python 3.8 or later installed and the following libraries:
- `transformers`
- `pathlib`
- `re`