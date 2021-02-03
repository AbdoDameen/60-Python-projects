import speech_recognition as sr
import moviepy.editor as mp
from  moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

num_seconds_video = 52*60
print("The video is {} seconds".format(num_seconds_video))
l=list(range(0,num_seconds_video+1,60))

diz={}
for i in range(len(l)-1):
    ffmpeg_extract_subclip("1  Defining the Problem.mp4", l[i]-2*(l[i]!=0),
    l[i+1], targetname="chunks/cut{}.mp4".format(i+1))
    clip=mp.AudioFileClip(r"converted/converted{}wav".format(i+1))
    with audio as source:
        r.adjust_for_ambient_noise(source)
        audio_file=r.record(source)
    result=r.recognize_google(audio_file)
    dis["chunck{}".format(i+1)]=result


l_chunks=[diz["chunk{}".format(i+1)] for i in range(len(diz))]
text='\n'.join(l_chunks)

with open('recognizedtxt', mode='w')as file:
    file.write("Recognized Speech:")
    file.write("\n")
    file.write(text)
    print("Finally ready!")
