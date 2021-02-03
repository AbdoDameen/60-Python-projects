import subprocess
from ibm_watson import SpeechToTextVl
from ibm_watson.websocket import RecRecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

command="ffmpeg -i 1  Defining the Problem.mp4 -b 160k -ar 44100 -vn audio.wav"
subprocess.call(command, shell=True)
