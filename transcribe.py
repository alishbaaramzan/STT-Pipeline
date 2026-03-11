import sys
import json
from faster_whisper import WhisperModel
from pydub import AudioSegment

# reading the audio file path from cli argument
audio_file = sys.argv[1]

# standardizing the input
audio = AudioSegment.from_file(audio_file)
audio = audio.set_channels(1).set_frame_rate(16000)
audio.export("converted.wav", format="wav")

# loading sst model
model = WhisperModel("base")

# transcribing
segments, info = model.transcribe("converted.wav")

# storing results in a list
results = []

for segment in segments:
    results.append({
        "start": segment.start,
        "end": segment.end,
        "text": segment.text
    })

# saving the output
output = {
    "language": info.language,
    "segments": results
}

with open("output.json", "w") as f:
    json.dump(output, f, indent=2)

print("Transcription saved to output.json")