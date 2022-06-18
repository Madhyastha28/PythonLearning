import pyttsx3

engine = pyttsx3.init()
some = "This is sample"
engine.say(some)
engine.runAndWait()
