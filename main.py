from transformers import pipeline
import re
from pathlib import Path

file = "king.mp3"
file_name = Path(file).stem

# Load the model
asr = pipeline("automatic-speech-recognition", "NbAiLabBeta/nb-whisper-large")

#transcribe
try:
    print("Extracting transcript...")
    transcribed = asr(file, return_timestamps=True, generate_kwargs={'task': 'transcribe', 'language': 'no'})
except FileNotFoundError:
    print(f"Error: File '{file}' not found.")
    exit()
except Exception as e:
    print(f"Error during transcription: {e}")
    exit()

transcribed_text = transcribed["text"]
lines = re.split(r'(?<=[.!?])\s*', transcribed_text)# Split the text into lines based on punctuation marks
lines = [line.strip() for line in lines]# Remove any leading/trailing spaces from each line

# Save the plain text
with open(f"{file_name}.txt", "w", encoding="utf-8") as file:
    for line in lines:
        file.write(line + "\n")

print(f"Transcription text saved to {file_name}.txt!")