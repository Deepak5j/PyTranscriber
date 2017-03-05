from pprint import pprint
import speech_recognition as sr
from os import path # "xxx.wav" 's path in same folder

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "as1.wav") # "french.aiff", "chinese.flac" format

r = sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source) # read the entire audio file

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said 1->" + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio 2->")
except sr.RequestError as e:
    print("Sphinx error; {0} 3->".format(e))

