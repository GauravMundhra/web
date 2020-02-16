import speech_recognition as sr
import mail


r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source,timeout=1,phrase_time_limit=1)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
        if (text=='approved' or 'approve'):
        	mail.main()
    except:
        print("Sorry could not recognize what you said")

