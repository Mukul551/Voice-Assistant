# Voice Assistant (JARVIS)

A Python-based desktop voice assistant project that uses speech recognition and text-to-speech to interact with the computer and perform common tasks. The repository contains several assistant implementations and supporting modules, including a more feature-rich Windows-oriented assistant, browser/search helpers, alarms, news reading, games, translation, and an AI-powered JARVIS prototype.

> **Project status:** This is a collection of scripts/prototypes rather than a polished packaged application. Some scripts may need configuration or debugging before they run. Start with the setup notes below and use the entry point that matches the features you want.

## Features

Depending on which script you run and configure, the project includes:

- Voice input using a microphone and speech recognition.
- Spoken responses using `pyttsx3`.
- Google, YouTube, and Wikipedia search helpers.
- Opening applications and websites.
- News headlines and weather-related functionality (API configuration required).
- Alarm functionality.
- System and media controls such as volume, play, pause, and mute (Windows-oriented).
- Small utilities such as games, jokes, translation, and internet-speed checks.
- An experimental `JARVIS/` prototype that integrates speech, AI providers, and optional camera/vision or website-related workflows.

## Project structure

```text
Voice Assistant/
├── Advance.py              # Extended Windows desktop assistant
├── sf.py                   # Earlier assistant script (currently needs syntax fixes)
├── virtual.py               # Basic voice-assistant example
├── SearchNow.py             # Google, YouTube, and Wikipedia helpers
├── Dictapp.py               # Application/website launching helpers
├── NewsRead.py              # Reads news headlines
├── alarm.py                 # Alarm helper
├── keyboard.py              # Media-volume key controls
├── game.py                  # Mini-game functionality
├── Whatsapp.py              # WhatsApp message helper
├── translaTOR/
│   └── translator.py        # Voice translation example
├── engine/                  # Search/storage-related support modules
└── JARVIS/
    ├── main.py              # AI-enabled JARVIS prototype
    ├── IMPORTS.py           # Prototype imports and setup
    ├── requirements.txt
    └── .env.example         # Example environment-variable names
```

The archive may also contain local assets, model files, databases, caches, and other supporting files. Keep required assets in their expected relative locations when running the scripts.

## Requirements

- Windows is the primary target for several features (`SAPI5`, `winshell`, `win32com`, Windows keyboard/system controls).
- Python 3.10 or 3.11 is a reasonable starting point. Some pinned packages in `JARVIS/requirements.txt` are older and may not support newer Python versions.
- A working microphone and speakers/headphones.
- Internet access for online speech recognition, web search, news, weather, and AI-provider features.
- API credentials for services you enable.

The root `requirements.txt` and `engine/requirements.txt` are minimal and do **not** list every dependency imported by all scripts. Depending on the script, additional packages may be required, such as `SpeechRecognition`, `PyAudio`, `pyttsx3`, `pywhatkit`, `wikipedia`, `pyautogui`, `speedtest-cli`, `wolframalpha`, `winshell`, `pyjokes`, `feedparser`, `twilio`, `clint`, `ecapture`, `pywin32`, `newsapi-python`, and `mtranslate`.

## Installation

Open PowerShell or Command Prompt in the project directory.

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. Upgrade pip:

   ```bash
   python -m pip install --upgrade pip
   ```

3. Install the packages listed in the root requirements file:

   ```bash
   pip install -r requirements.txt
   ```

4. Install any additional packages needed by the specific script you plan to use. For example, a basic speech/search setup may need:

   ```bash
   pip install SpeechRecognition PyAudio pyttsx3 pywhatkit wikipedia
   ```

   **PyAudio note:** Installation can vary by Python version and Windows environment. If `pip install PyAudio` fails, use a compatible wheel or follow the official PyAudio installation guidance for your Python version.

## Running the project

Run commands from the `Voice Assistant` project root so that relative file paths and local modules can be found.

### Extended desktop assistant

```bash
python Advance.py
```

`Advance.py` is the extended Windows-oriented script. It imports several optional packages and uses external services for some commands, so install the relevant dependencies and configure credentials before using those features.

### Basic assistant example

```bash
python virtual.py
```

### AI-enabled JARVIS prototype

```bash
cd JARVIS
pip install -r requirements.txt
```

Create a local `.env` file from the example:

```bash
copy .env.example .env
```

Add your own valid API credentials to `.env`, then run:

```bash
python main.py
```

The JARVIS prototype also imports project-specific modules and may require additional setup beyond the listed requirements. Review `IMPORTS.py` and the referenced modules before expecting this prototype to run independently.

## Example voice commands

The exact commands depend on the script and enabled features. Examples include:

- "What time is it?"
- "Tell me a joke."
- "Search Google for Python tutorials."
- "Search Wikipedia for machine learning."
- "Play music on YouTube."
- "Open [application or website]."
- "Read the news."
- "Set an alarm."

Speak clearly and allow the assistant to finish listening before giving another command.

## API keys and configuration

Some features rely on third-party services such as news, weather, or AI providers.

- Store credentials in environment variables or a local `.env` file.
- Do not commit `.env`, API keys, access tokens, phone numbers, or other private information.
- Use `.env.example` only as a template with placeholder values.
- If a credential was ever committed or shared publicly, revoke/rotate it with the provider and replace it with a new one.

Before publishing this project, check every Python file for hard-coded credentials. In particular, review the news/API integrations and any messaging-related scripts. Remove personal phone numbers and private configuration from the repository.

## Important notes and limitations

- Several features are Windows-specific and may not work on Linux or macOS.
- Google-based speech recognition and online services require an internet connection.
- Microphone access and audio drivers must be configured correctly.
- News, weather, AI, and messaging features may require valid API credentials or account setup.
- The scripts are separate examples; not every feature is available from every entry point.
- `sf.py` currently contains a syntax error in the supplied archive and must be corrected before it can run.
- Review potentially disruptive commands (for example, shutdown, lock, or system-control actions) before enabling or using them.

## Security and GitHub publishing checklist

Before pushing the project to GitHub:

1. Remove the `JARVIS/.env` file from the repository and keep only `.env.example` with placeholders.
2. Remove the nested `JARVIS/.git/` directory. A project should normally have one Git repository at its root.
3. Remove Python cache folders (`__pycache__/`) and compiled `.pyc` files.
4. Review source files for hard-coded API keys and personal phone numbers; rotate any exposed credentials.
5. Avoid committing generated audio, temporary files, personal conversation history, or large model/cache files unless they are intentionally part of the project.
6. Add a `.gitignore` file.

Suggested `.gitignore`:

```gitignore
# Python
__pycache__/
*.py[cod]
*.pyo
.venv/
venv/
env/

# Secrets
.env
*.pem
*.key

# Runtime/generated files
*.log
*.tmp
Remember.txt
Alarmtext.txt
JARVIS/ASSETS/conversation_history.json
JARVIS/ASSETS/output_audio.mp3

# IDE / OS
.vscode/
.idea/
.DS_Store
Thumbs.db
```

## Troubleshooting

- **Microphone not detected:** Check Windows microphone permissions, the default input device, and PyAudio installation.
- **No spoken output:** Check the selected Windows audio output device and `pyttsx3`/SAPI5 installation.
- **Missing module error:** Activate the virtual environment and install the missing package with `pip install package-name`.
- **API request fails:** Verify internet access, API key validity, provider limits, and required environment variables.
- **Application command does not work:** Some launch helpers use Windows-specific application paths or names; update them for your computer.

## Contributing

Contributions and improvements are welcome. You can help by fixing bugs, improving command recognition, adding cross-platform support, documenting setup steps, and separating configuration from source code.

1. Fork the repository.
2. Create a feature branch.
3. Make and test your changes.
4. Open a pull request with a clear description.

## License

No single project-wide license was clearly established for all files in this archive. Add a `LICENSE` file before publishing if you want others to know how the project may be used, modified, and distributed. Check the licenses of included third-party code and assets as well.

---

