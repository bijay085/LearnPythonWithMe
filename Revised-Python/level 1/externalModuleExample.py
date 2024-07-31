# Install an external module and use it to perform an operation of your interest. 
# We gonna use text to speech

import pyttsx3
engine = pyttsx3.init() #engine is mainly called as object but we can call it variable for simpler term, we can create any !
engine.say("Hello world, I am going to do this revised python using project just like crash course !")
engine.say("Am i ready ?")
engine.runAndWait()
print("Done !")


import pyttsx3 as p
me = p.init() 
me.say("hello world 2, Yes i am ready !")
me.runAndWait()
print("Done 2 !")