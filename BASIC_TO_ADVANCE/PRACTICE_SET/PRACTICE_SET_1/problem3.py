# install the external module and use operations as your interest

import pyttsx3
engine = pyttsx3.init()

engine.say("HEY! I am your virtual assistant. I can speak whatever you want me to say. Just type the text and I will speak it for you.")
engine.save_to_file("HEY! I am your virtual assistant. I can speak whatever you want me to say. Just type the text and I will speak it for you.", "output.wav")  # ADD THIS
engine.runAndWait()