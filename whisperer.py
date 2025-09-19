import whisper

model = whisper.load_model("base")  # You can use "tiny", "small", "medium", "large"

audio_path = input("Enter the path to your audio file: ")

# Transcribe the audio file
result = model.transcribe(audio_path)

# Show detected language
print(f"Detected language: {result['language']}")

# Show the transcription
print("\nTranscription:\n")
print(result['text'])

import os

# Get the directory of the audio file
output_dir = os.path.dirname(audio_path)

# Get the base name of the file without extension
base_name = os.path.splitext(os.path.basename(audio_path))[0]

# Create a path for the output .txt file
output_txt_path = os.path.join(output_dir, f"{base_name}_transcription.txt")

# Write the transcription to the .txt file
with open(output_txt_path, "w", encoding="utf-8") as f:
    f.write(result['text'])

print(f"\nTranscription saved to: {output_txt_path}")