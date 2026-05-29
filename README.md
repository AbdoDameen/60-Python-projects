# 60 Python Projects

A collection of 60 beginner-to-intermediate Python projects with source code. Originally based on Aman Kharwal's projects — all 39 Python scripts have been reviewed, debugged, and improved.

## What's Inside

39 Python projects covering:

**GUI Apps (tkinter)**
Calendar, Digital Clock, Music Player, Tic Tac Toe

**Games**
Card Game (War), Dice Roll Simulator, Fidget Spinner, Quiz Game, Rock Paper Scissors, Tic Tac Toe, The Game of Life, Simulating Monty Hall Problem

**Computer Vision (OpenCV)**
Barcode & QR Code Reader, Face Detection, Image to Pencil Sketch, Creating Instagram Filters, Use Phone Camera, Extract Text From Videos

**Turtle Graphics**
Fractal Tree Pattern, Chessboard, Spirograph, Shape Drawings

**Data & Analytics**
Count Rainy Days (pandas), Keyword Research (Google Trends), Spelling Correction (TextBlob), Story Generator

**Utilities**
Alarm Clock, BMI Calculator, Convert Fahrenheit to Celsius, Convert Roman Numerals, Create Acronyms, Create an Audiobook from a PDF, Desktop Notification, Email Slicer, Generate Password, Multiple Inputs, QR Codes, Video to Audio Converter, YouTube Audio Extractor

**Other**
Colored Text (colorama), Creating Graphics

## Improvements Made

Every script was reviewed and upgraded:

- **Bug fixes**: 13 critical runtime bugs fixed (typos, NameError, wrong API calls, deprecated functions, logic errors)
- **Modernised**: f-strings, type hints, snake_case, main guards, docstrings
- **Error handling**: input validation, file existence checks, try/except blocks
- **Refactored**: Turtle Graphics 2 (12 redundant functions → parameterised loop), Music Player (button wiring), Extract Text (complete rewrite), Game of Life (proper class)
- **Removed**: dead code, unused imports, commented-out debug blocks

## Quick Start

```bash
git clone https://github.com/AbdoDameen/60-Python-projects.git
cd "60-Python-projects/60 Python projects"

# Most scripts run with just Python:
python3 "BMI Calculator.py"

# Some need extra libraries:
pip install opencv-python pyzbar pygame pillow textblob pytrends
```

## Requirements by Project

| Category | Libraries |
|---|---|
| GUI | tkinter (built-in) |
| Games | random, numpy (built-in) |
| OpenCV | opencv-python, pyzbar |
| Audio/Video | moviepy, SpeechRecognition, PyAudio, pytube, PyPDF2, pyttsx3 |
| Data | pandas, numpy, matplotlib, pytrends, textblob |
| Utilities | plyer, playsound, colorama, pyqrcode |

## Repo Structure

```
60-Python-projects/
├── README.md
└── 60 Python projects/
    ├── *.py          # Python scripts
    ├── *.ipynb       # Jupyter notebooks
    ├── *.mp3         # Sample audio files
    ├── *.mp4         # Sample video files
    └── *.svg         # Generated SVG files
```

## Author

**AbdoDameen** — AI Engineer, data pipelines, and the occasional Python project.
