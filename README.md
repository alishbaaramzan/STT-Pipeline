# Design Choices

**Model selection**

I used the **OpenAI Whisper** implementation via **faster-whisper** because it offers high-quality transcription, is faster than OpenAI Whisper and returns timestamps for every segment. The `base` model was selected because it offers a fair compromise between local computation requirements and accuracy.

## Preprocessing audio

**pydub** is used to standardize audio files and depends on **FFmpeg** for conversion and decoding. Prior to transcription, all inputs are converted to **16 kHz mono WAV** because consistent input formats improve the performance of speech recognition models.

## Format of output

Because it is structured, simple to parse, and frequently used when sending results to downstream systems or APIs, transcriptions are stored in **JSON format**. Along with the transcribed text, each segment has start and end timestamps.

## Simplicity

In order to make the pipeline easy to comprehend, run locally, and eventually expand into a service or API if necessary, the implementation is purposefully kept straightforward and script-based.