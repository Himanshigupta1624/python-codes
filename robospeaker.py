
# import pyttsx3

# engine=pyttsx3.init()
# rate=engine.getProperty('rate')
# print(rate)
# engine.setProperty('rate', rate+68)
# volume=engine.getProperty('volume')
# engine.setProperty('volume', volume+.05)

# voices=engine.getProperty('voices')
# print(voices)

# engine.say("hey himanshi ")
# engine.runAndWait()



from gtts import gTTS
from playsound import playsound
text_val='Lag Ja Gale Ki Phir Ye Hasin Raat Ho Na Ho Shaayad Phir Is Janam Men Mulaaqaat Ho Na Ho Lag Jaa Gale ...'
lang='hi'
obj=gTTS(text=text_val,lang=lang,slow=False)
obj.save('naam.mp3')
playsound('naam.mp3')
