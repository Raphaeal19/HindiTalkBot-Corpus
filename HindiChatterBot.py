from chatterbot import ChatBot
from gtts import gTTS as gt
import os
from googletrans import Translator
import speech_recognition as sr
from polyglot.transliteration import Transliterator
import random
from datetime import datetime

tr = Translator()
r = sr.Recognizer()

def speak(audioString, langOp):
	print("Speak: ", audioString)
	tts = gt(text=audioString, lang=langOp)
	tts.save("audio_files/audio.mp3")
	os.system("mpg321 audio_files/audio.mp3 -q")

def recordAudio():
	with sr.Microphone() as source:
		print("Say Something!")
		speak(translateLang("I am listening", "hi"), "hi")
		audio = r.listen(source, timeout=1, phrase_time_limit=10)

	data = ""
	try:
		data = r.recognize_google(audio)
		print("You said: " + data)
	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
	return data

def translateLang(audioString, toLang):
	if(toLang == "hi"):
		#print("")
		data = tr.translate(audioString, dest='hi').text
		print("tranlateLang: ",data)
		return data	

	elif(toLang == "en"):
		#print("")
		data = tr.translate(audioString, dest='en').text
		print("tranlateLang: ",data)
		return data	

	else:
		print("Ambiguious Language Translation Required, Exiting!")
		exit()

def transliterationLang(textString):
	trl = Transliterator(source_lang="en", target_lang="hi")
	data = trl.transliterate(textString)
	print("transliterationLang: ",data)
	return data


speak("hello good Microphone", "hi")