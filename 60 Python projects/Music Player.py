"""A simple music player with Play, Stop, Pause, and Unpause controls."""

import os
import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory


def build_player() -> None:
    """Create and run the music player GUI."""
    music_player = tkr.Tk()
    music_player.title("My Music Player")
    music_player.geometry("450x350")

    # Ask the user to select a music directory
    directory = askdirectory()
    if not directory:
        print("No directory selected. Exiting.")
        return

    os.chdir(directory)
    song_list = os.listdir()

    # Create the playlist listbox
    play_list = tkr.Listbox(
        music_player,
        font="Helvetica 12 bold",
        bg="yellow",
        selectmode=tkr.SINGLE,
    )

    for i, item in enumerate(song_list):
        play_list.insert(i, item)

    # Initialize the pygame mixer
    pygame.init()
    pygame.mixer.init()

    # Track the current song title
    current_song = tkr.StringVar()

    def play() -> None:
        """Load and play the selected song."""
        selected_song = play_list.get(tkr.ACTIVE)
        pygame.mixer.music.load(selected_song)
        current_song.set(selected_song)
        pygame.mixer.music.play()

    def stop() -> None:
        """Stop playback."""
        pygame.mixer.music.stop()

    def pause() -> None:
        """Pause playback."""
        pygame.mixer.music.pause()

    def unpause() -> None:
        """Resume playback after pause."""
        pygame.mixer.music.unpause()

    # Create control buttons with distinct names
    play_button = tkr.Button(
        music_player,
        width=5,
        height=3,
        font="Helvetica 12 bold",
        text="PLAY",
        command=play,
        bg="blue",
        fg="white",
    )
    stop_button = tkr.Button(
        music_player,
        width=5,
        height=3,
        font="Helvetica 12 bold",
        text="STOP",
        command=stop,
        bg="red",
        fg="white",
    )
    pause_button = tkr.Button(
        music_player,
        width=5,
        height=3,
        font="Helvetica 12 bold",
        text="PAUSE",
        command=pause,
        bg="purple",
        fg="white",
    )
    unpause_button = tkr.Button(
        music_player,
        width=5,
        height=3,
        font="Helvetica 12 bold",
        text="UNPAUSE",
        command=unpause,
        bg="orange",
        fg="white",
    )

    # Song title label
    song_title = tkr.Label(
        music_player,
        font="Helvetica 12 bold",
        textvariable=current_song,
    )

    # Layout the widgets
    song_title.pack()
    play_button.pack(fill="x")
    stop_button.pack(fill="x")
    pause_button.pack(fill="x")
    unpause_button.pack(fill="x")
    play_list.pack(fill="both", expand=True)

    music_player.mainloop()


if __name__ == "__main__":
    build_player()
