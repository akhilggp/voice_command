import speech_recognition as s
import tts
import webbrowser as wb

r=s.Recognizer()
with s.Microphone() as source:
	print("hello say something")
	audio=r.listen(source)
	print("ok")
try:
	text=r.recognize_google(audio)
	print("I think you said as:\n"+text)
	lang='en'
	tts.tts(text,lang)
	wb.open_new_tab('http://www.google.com/search?btnG=1&q='+text)
except Exception as e:
	print(e)
