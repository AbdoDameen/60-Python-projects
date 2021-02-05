import PyPDF2
import pyttsx3

pdfReader = PyPDF2.PdfFileReader(open("short stories.pdf", 'rb'))
speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)


for page_num in range(pdfReader.numPages):
    text = pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()

speaker.stop()

engine.save_to_file(text, "audio.mp3")
engine.runAndWait()
