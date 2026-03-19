# Voice Agent

A lightweight Python voice assistant that listens through your microphone, sends the transcript to an OpenAI chat model, and plays the response back as speech.

This workspace currently includes:

- A voice loop app (`cursor.py`) using speech-to-text + chat + text-to-speech.
- A CLI agent prototype (`agent.py`) with basic tool-calling scaffolding.

## Features

- Microphone input with ambient noise adjustment.
- Speech-to-text using Google recognition via `SpeechRecognition`.
- Conversational responses using OpenAI Chat Completions.
- Spoken output using OpenAI TTS streaming.

## Project Files

- `cursor.py`: Main voice assistant loop (listen, transcribe, respond, speak).
- `agent.py`: Text-based prototype with command tool wiring.
- `requirements.txt`: Python dependencies.

## Prerequisites

- Python 3.10+
- A working microphone
- OpenAI API key
- Internet access (for STT and OpenAI APIs)

## Setup

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

## Run

### Voice Agent (recommended)

```powershell
python cursor.py
```

What happens:

1. The app waits for microphone input.
2. Your speech is transcribed to text.
3. The text is sent to the chat model.
4. The response is converted to speech and played.

### CLI Prototype Agent

```powershell
python agent.py
```

This script is a prototype and may require additional hardening before production use.

## Troubleshooting

- If microphone capture fails, check your default input device and permissions.
- If you get `Could not request results`, verify internet connectivity.
- If audio playback fails, confirm your output device is working.
- If `PyAudio` installation fails on Windows, install Visual C++ Build Tools or use a compatible wheel.

## Notes

- Models used in code are currently `gpt-4o-mini` and `gpt-4o-mini-tts`.
- The voice loop is continuous; stop it with `Ctrl+C`.
