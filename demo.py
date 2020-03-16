import speech_recognition as sr

rec1 = sr.Recognizer()
rec2 = sr.Recognizer()

with sr.Microphone() as source:
    audio = rec1.listen(source)

text = rec2.recognize_google(audio)
print(text)
