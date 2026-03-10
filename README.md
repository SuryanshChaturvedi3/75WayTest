# 🎙️ AI Voice Agent

A voice-driven AI agent that listens to your microphone, understands what you say, and speaks back using OpenAI's TTS — all in real time.

---

## 📂 Project Structure

```
Voice-Agent/
├── cursor.py          # Main voice agent (STT → LLM → TTS loop)
├── agent.py           # Tool-calling agent (text input → LLM → run_cmd)
├── .env               # API keys (not committed)
├── requirements.txt   # Python dependencies
└── README.md
```

---

## 🛠 Technologies Used

| Tool / Library | Purpose |
|---|---|
| `openai` (gpt-4o-mini) | LLM for generating responses |
| `openai` (gpt-4o-mini-tts) | Text-to-Speech — speaks the AI response out loud |
| `SpeechRecognition` + Google STT | Converts microphone audio to text |
| `PyAudio` | Microphone input stream |
| `sounddevice` + `numpy` | Audio playback via `LocalAudioPlayer` |
| `python-dotenv` | Loads `OPENAI_API_KEY` from `.env` file |
| `pydantic` | Data validation (used in agent layer) |
| `requests` | HTTP calls (available for tool use in agent) |
| `asyncio` | Async TTS streaming and playback |

---

## ✅ Completed

- [x] Microphone input capture using `SpeechRecognition`
- [x] Speech-to-Text via Google STT (`recognize_google`)
- [x] LLM response generation via `gpt-4o-mini`
- [x] Text-to-Speech playback via `gpt-4o-mini-tts` + `LocalAudioPlayer`
- [x] Continuous voice loop (listens → responds → listens again)
- [x] Ambient noise adjustment for better STT accuracy
- [x] Pause threshold tuning (`pause_threshold = 2`)
- [x] Conversation history maintained across turns (`messages` list)
- [x] Tool-calling agent scaffold (`agent.py`) with `run_cmd` tool
- [x] Environment variable loading via `.env`
- [x] `requirements.txt` with all dependencies

---

## Local Setup Changes (March 10, 2026)

- Removed the extra `venv/` folder that was not used by this project.
- Kept `.venv/` as the project virtual environment.
- Recreated `.venv/` with Python `3.11` (replacing Python `3.14` usage).
- Reinstalled dependencies from `requirements.txt` into `.venv/`.
- Verified interpreter behavior:
   - Global shell `python` may vary by system.
   - Activated project `.venv` resolves to Python `3.11`.
- Ran the app successfully with exit code `0`:
   - `python cursor.py`
   - `C:/Users/Dell/AppData/Local/Programs/Python/Python311/python.exe cursor.py`

---

## ⏳ Not Yet Implemented

- [ ] Tool execution in `agent.py` (currently broken — `tool_calls.appended` is invalid)
- [ ] Integration of `agent.py` tool-calling into the voice loop (`cursor.py`)
- [ ] Wake word detection (e.g. "Hey Agent")
- [ ] Multi-tool support (web search, file operations, etc.)
- [ ] Persistent conversation memory across sessions
- [ ] GUI or web interface
- [ ] Error recovery / retry logic for failed API calls

---

## ⚡ Setup & Run

1. **Create and activate Python 3.11 virtual environment (Windows PowerShell)**
   ```bash
   py -3.11 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python --version
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file** in the project root:
   ```
   OPENAI_API_KEY=sk-...your-key-here...
   ```

4. **Run the voice agent**
   ```bash
   python cursor.py
   ```

   The agent will start listening from your microphone, respond via the LLM, and speak the answer back to you.

---

## 🔁 How It Works

```
Microphone → SpeechRecognition (Google STT) → gpt-4o-mini (LLM) → gpt-4o-mini-tts (TTS) → Speaker
```

Each response is added back to the conversation history so the agent remembers context across turns.
