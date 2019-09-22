from chatterbot import ChatBot
from gtts import gTTS as gt
import os
from googletrans import Translator
import speech_recognition as sr
from polyglot.transliteration import Transliterator
from chatterbot.trainers import ListTrainer
from pocketsphinx import LiveSpeech

tr = Translator()
r = sr.Recognizer()

def speak(audioString, langOp):
	print("Speak: ", audioString)
	tts = gt(text=audioString, lang=langOp)
	tts.save("audio_files/audio.mp3")
	os.system("mpg321 audio_files/audio.mp3 -q")

def botTrainer(name):
	bot = ChatBot(name)
	trainers = ListTrainer(bot)

	for files in os.listdir("chatterbot_corpus/data/hindi"):
		data = open("chatterbot_corpus/data/hindi/" + files, 'r').readlines()
		trainers.train(data)
	return bot

def recordAudio():
	with sr.Microphone() as source:
		print("Say Something!")
		speak(translateLang("I am listening", "hi"), "hi")
		audio = r.listen(source)

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
'''
name = input("What will be the name for your bot? ")
myBot = botTrainer(name)
input1 = translateLang("aap kaise hai", "hi")
print("INPUT1: ", input1)
reply = myBot.get_response(input1).text
print("REPLY: ", reply)
speak(translateLang(reply, "hi"),"hi")
'''
#speak(translateLang("namaskar", "en"), "en-us")

name = input("What will be the name for your bot? ")
myBot = botTrainer(name)
audioString = recordAudio()
input1 = translateLang(audioString, "hi")
reply = myBot.get_response(input1)
speak(reply, "hi")

