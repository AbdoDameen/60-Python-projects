"""Extract speech from a video file and save it as text."""

import os
import speech_recognition as sr
import moviepy.editor as mp
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


def extract_text_from_video(
    video_path: str,
    output_file: str = "recognized_text.txt",
    chunk_duration: int = 60,
) -> None:
    """Split a video into chunks, extract speech from each, and save the text."""
    # Check that the video file exists
    if not os.path.exists(video_path):
        print(f"Error: video file '{video_path}' not found.")
        return

    # Get video duration in seconds
    try:
        clip = mp.VideoFileClip(video_path)
        total_seconds = int(clip.duration)
        clip.close()
    except Exception as e:
        print(f"Error reading video file: {e}")
        return

    print(f"The video is {total_seconds} seconds long.")

    # Build a list of chunk boundaries (every chunk_duration seconds)
    chunk_starts = list(range(0, total_seconds + 1, chunk_duration))

    # Ensure the chunks directory exists
    os.makedirs("chunks", exist_ok=True)

    recognizer = sr.Recognizer()
    all_text = {}

    for i in range(len(chunk_starts) - 1):
        chunk_start = chunk_starts[i]
        chunk_end = chunk_starts[i + 1]

        # Adjust start time to avoid repeating the last frame (except the first chunk)
        adjusted_start = chunk_start - 2 if chunk_start != 0 else 0
        chunk_filename = f"chunks/cut{i + 1}.mp4"

        print(f"Processing chunk {i + 1}/{len(chunk_starts) - 1}...")

        try:
            # Extract the chunk from the video
            ffmpeg_extract_subclip(
                video_path,
                adjusted_start,
                chunk_end,
                targetname=chunk_filename,
            )

            # Convert the chunk audio to a WAV file
            audio_clip = mp.AudioFileClip(chunk_filename)
            audio_clip.write_audiofile(f"chunks/chunk{i + 1}.wav")
            audio_clip.close()

            # Recognize speech from the audio file
            with sr.AudioFile(f"chunks/chunk{i + 1}.wav") as source:
                recognizer.adjust_for_ambient_noise(source)
                audio_data = recognizer.record(source)

            result = recognizer.recognize_google(audio_data)
            all_text[f"chunk{i + 1}"] = result
            print(f"  Chunk {i + 1} recognized successfully.")

        except sr.UnknownValueError:
            print(f"  Chunk {i + 1}: could not understand audio.")
            all_text[f"chunk{i + 1}"] = "[unrecognized]"
        except sr.RequestError as e:
            print(f"  Chunk {i + 1}: speech recognition request failed: {e}")
            all_text[f"chunk{i + 1}"] = "[recognition error]"
        except Exception as e:
            print(f"  Chunk {i + 1}: unexpected error: {e}")
            all_text[f"chunk{i + 1}"] = "[error]"

    # Combine all recognized text and write to output file
    full_text = "\n".join(all_text.values())

    with open(output_file, "w") as f:
        f.write("Recognized Speech:\n")
        f.write("\n")
        f.write(full_text)

    print(f"Done! Recognized text saved to '{output_file}'.")


if __name__ == "__main__":
    extract_text_from_video("1  Defining the Problem.mp4")
