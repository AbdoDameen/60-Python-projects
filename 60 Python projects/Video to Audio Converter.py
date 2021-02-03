from pytube import YouTube
import pytube
import os

def main():
    video_url = input("https://www.youtube.com/watch?v=aEAs8NRVfYE")

    if os.name=="tn":
        path=os.getcwd()+ '\\'
    else:
        path=os.getcwd()+ "/"

    name=pytube.extract.video_id(video_url)
    YouTube(video_url).streams.filter(onlonly_audio=True),first().download(filename=name)
    location=path + name + '.mp4'
    renametomp3 = path + name + '.mp3'

    if os.name=='nt':
        os.system('ren {0} {1}'. format(location, renametomp3))
    else:
        os.system('mv {0} {1}'.format(location, renametomp3))

if __name__ == '__main__':
    main()
