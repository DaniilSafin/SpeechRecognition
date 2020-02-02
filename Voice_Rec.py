# -*- coding: utf-8 -*-
 
import speech_recognition as sr
import os
from os import path

def speech_recog(filename):
	r = sr.Recognizer()

	with sr.AudioFile(audio_file) as source:
		audio = r.record(source)

	try:
		recog_txt = r.recognize_google(audio, language="ru-RU").lower()
		print("Распознанный текст в файле " + filename +":\n" + recog_txt+"\n")
	except sr.UnknownValueError:
		print("Ошибка распознования...\n Повторяю попытку...\n")
		recog_txt = speech_recog()
	return text_editing(recog_txt)

def text_editing(txt):
    split_txt = txt.__str__().split(' ')
    for shit in split_txt:
        if shit == ("вот") or shit == ("типа") or shit == ("короче") or shit == ("однако")\
                or shit == ("это") or shit == ("ну") or shit == ("собственно") or shit == ("допустим") \
                or shit == ("слушай") or shit == ("кстати") or shit == ("вообще") or shit == ("там") or shit == ("ну"):
            array_edit_txt.append(shit.upper())
        else:
            array_edit_txt.append(shit.lower())
    final_txt = ' '.join(array_edit_txt)
    return final_txt

array_wav = []
array_txt = []
array_edit_txt=[]
for files in os.listdir():
    if files.endswith(".wav"):
        array_wav.append(files)
    if files.endswith(".txt"):
        array_txt.append(files)


for files_wav in array_wav:
    audio_file = path.join(path.dirname(path.realpath(__file__)), files_wav)
    with open(files_wav.__str__()[:-4] + ".txt", "w", encoding="utf- 8") as final:
        final.write(speech_recog(files_wav))
        array_edit_txt.clear()
array_wav.clear()
