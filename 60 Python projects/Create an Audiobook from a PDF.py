"""
Audiobook Creator from PDF.
Reads a PDF file and converts its text content to speech using pyttsx3.
"""

import os
import sys
from PyPDF2 import PdfReader
import pyttsx3


def pdf_to_speech(pdf_path: str, output_audio: str = "audio.mp3"):
    """
    Read text from a PDF file and convert it to speech.
    Optionally saves the speech to an audio file.

    Args:
        pdf_path: Path to the PDF file to read.
        output_audio: Path for the output MP3 file.
    """
    # Check if the PDF file exists
    if not os.path.exists(pdf_path):
        print(f"Error: '{pdf_path}' not found.")
        sys.exit(1)

    # Open and read the PDF
    print(f"Reading PDF: {pdf_path}")
    pdf_reader = PdfReader(open(pdf_path, 'rb'))

    # Initialize text-to-speech engine
    speaker = pyttsx3.init()
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[1].id)  # Use second voice (often female)

    full_text = ""

    # Extract text from each page and speak it
    for page_num, page in enumerate(pdf_reader.pages):
        text = page.extract_text()
        full_text += text
        print(f"Reading page {page_num + 1}/{len(pdf_reader.pages)}...")
        speaker.say(text)
        speaker.runAndWait()

    # Save audio to file
    speaker.save_to_file(full_text, output_audio)
    speaker.runAndWait()
    speaker.stop()

    print(f"Audiobook saved to: {output_audio}")


def main():
    """Get PDF path from user or use default, then convert to speech."""
    pdf_path = input("Enter the path to the PDF file (default: 'short stories.pdf'): ").strip()
    if not pdf_path:
        pdf_path = "short stories.pdf"
    pdf_to_speech(pdf_path)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nAudiobook creation cancelled.")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
