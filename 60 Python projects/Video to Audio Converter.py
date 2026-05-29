from pytube import YouTube
import pytube
import os


def main():
    """
    Download audio from a YouTube video and save it as an MP3 file.

    Downloads the audio-only stream, then renames the .mp4 container to .mp3.
    Most media players can play .mp3 files regardless of the container format.
    """
    # Ask the user for a YouTube URL
    video_url = input("Enter YouTube video URL: ").strip()

    if not video_url:
        print("No URL provided. Exiting.")
        return

    # Determine the path separator for the current OS
    if os.name == "nt":
        path = os.getcwd() + "\\"
    else:
        path = os.getcwd() + "/"

    # Extract the video ID for the filename
    video_id = pytube.extract.video_id(video_url)

    try:
        # Fetch the YouTube video
        yt = YouTube(video_url)

        # Get the audio-only stream (highest quality)
        audio_stream = yt.streams.filter(only_audio=True).first()

        if audio_stream is None:
            print("Error: No audio stream available for this video.")
            return

        # Download the audio stream using the video ID as the filename
        print(f"Downloading audio from: {yt.title}")
        audio_stream.download(filename=video_id)

    except Exception as e:
        print(f"Error downloading video: {e}")
        return

    # Rename the downloaded .mp4 file to .mp3
    location = os.path.join(path, f"{video_id}.mp4")
    rename_to_mp3 = os.path.join(path, f"{video_id}.mp3")

    try:
        os.rename(location, rename_to_mp3)
        print(f"Audio saved to: {rename_to_mp3}")
    except FileNotFoundError:
        print(f"Warning: Could not find downloaded file at {location}")
    except Exception as e:
        print(f"Warning: Could not rename file: {e}")


if __name__ == '__main__':
    main()
