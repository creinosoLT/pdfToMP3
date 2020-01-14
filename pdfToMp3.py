from tkinter import Tk
import sys
import os
from tkinter.filedialog import askopenfilename
import pdftotext
from gtts import gTTS

if os.environ.get('DISPLAY', '') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

Tk().withdraw()
filelocation = askopenfilename()

with open(filelocation, "rb") as f:
    pdf = pdftotext.PDF(f)

string_of_text = ''
for text in pdf:
    string_of_text += text

final_file = gTTS(text=string_of_text, lang='en')
final_file.save("GeneratedSpeech.mp3")
