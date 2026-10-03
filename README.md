# Voice Assistant

A Python voice assistant for Windows that listens to spoken commands and responds with text-to-speech. It can open websites, read Wikipedia summaries, play local music, announce the time, and send an email through a configured Gmail account.

## Features

- Time-based greeting and spoken responses using `pyttsx3`.
- Microphone input with Google speech recognition (`en-in`).
- Website shortcuts for YouTube, Google, Wikipedia, Stack Overflow, Amazon, W3Schools, Tutorials Point, and Flipkart.
- Spoken Wikipedia summaries of up to five sentences.
- Local music playback and current-time announcements.
- Email helper using SMTP.
- Separate OpenAI API experiment in `testOpenai.py`.

## Requirements

- Python on **Windows**: the implementation uses the SAPI5 speech engine and `os.startfile()`.
- A working microphone and speakers.
- Internet access for speech recognition, Wikipedia, websites, email, and the optional API example.

Install the dependencies:

```bash
python -m pip install pyttsx3 SpeechRecognition PyAudio wikipedia openai
```

## Run

```bash
python voice_assistant.py
```

Wait for the greeting and listening prompt, then speak a command.

| Example Command | Action |
| --- | --- |
| “Open YouTube” | Opens YouTube in the browser |
| “Open Google” | Opens Google in the browser |
| “Wikipedia Alan Turing” | Reads a Wikipedia summary |
| “Play music” | Opens a randomly selected local music entry |
| “What is the time?” | Announces the current time |
| “Email” | Asks for a message and sends it to the configured recipient |

Stop the program with **Ctrl+C** in the terminal. There is no implemented voice-exit command.

## Limitations

- Commands are matched using keywords rather than conversational intent understanding.
- There is no wake word; listening begins automatically in the loop.
- Speech recognition uses an online service.
- Wikipedia lookup errors are not handled in the command loop.
- Music paths, email settings, and some browser URLs need local configuration.
- The email flow sends the recognized message without a separate confirmation step.
