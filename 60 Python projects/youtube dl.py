import subprocess
import os


def main():
    """
    Extract audio from a local MP4 video file using ffmpeg.

    This script takes a video file (e.g., '1 Defining the Problem.mp4')
    and converts it to a WAV audio file using ffmpeg.
    """
    input_video = "1  Defining the Problem.mp4"
    output_audio = "audio.wav"

    # Check if the input file exists
    if not os.path.exists(input_video):
        print(f"Error: Input file '{input_video}' not found.")
        print("This script extracts audio from a local video file using ffmpeg.")
        return

    # Build the ffmpeg command:
    # -i <input>       : input file
    # -b 160k          : audio bitrate (160 kbps)
    # -ar 44100        : audio sample rate (44.1 kHz)
    # -vn              : no video (audio only)
    command = f"ffmpeg -i \"{input_video}\" -b 160k -ar 44100 -vn \"{output_audio}\""

    print(f"Extracting audio from '{input_video}' to '{output_audio}'...")
    subprocess.call(command, shell=True)
    print("Done.")


if __name__ == '__main__':
    main()
