import pyttsx3
import os
print("__________OPERATION YOU CAN PERFORM____")
print("__________open chrome browser__________")
print("__________open vlc_____________________")
print("__________open notepad_________________")
print("__________open eclipse_________________")
print("__________open control panel___________")
print("__________open oracle VM virtualbox____")
print("__________open wordpad_________________")
print("__________open paint___________________")
print("__________open excel___________________")
print("__________open calculator______________")
while True:
  
  p=(input("HEY ARE YOU READY TO CHAT WITH OS:"))
  if (("open" in p) or ("OPEN" in p) or ("play" in p) or ("PLAY" in p)  or ("run" in p) or ("RUN" in p) or ("execute" in p) or ("EXECUTE" in p) or ("start" in p) or ("START" in p)) and (("chrome" in p) or ("CHROME" in p) or ("chrome browser" in p) or ("CHROME BROWSER" in p)) and (("not" not in p) and ("NOT" not in p) and ("don't" not in p) and ("DON'T" not in p) and ("donot" not in p) and ("DONOT" not in p) and ("do not" not in p) and ("DO NOT" not in p)):
    pyttsx3.speak("opening chrome")
    os.system("chrome")

  elif (("open" in p) or ("OPEN" in p) or ("play" in p) or ("PLAY" in p)  or ("run" in p) or ("RUN" in p) or ("execute" in p) or ("EXECUTE" in p) or ("start" in p) or ("START" in p)) and (("vlc" in p) or ("VLC" in p) or ("media player" in p) or ("MEDIA PLAYER" in p)) and (("not" not in p) and ("NOT" not in p) and ("don't" not in p) and ("DON'T" not in p) and ("donot" not in p) and ("DONOT" not in p) and ("do not" not in p) and ("DO NOT" not in p)):
    pyttsx3.speak("opening VLC media player")
    os.system("vlc")

  elif (("open" in p) or ("OPEN" in p) or ("play" in p) or ("PLAY" in p)  or ("run" in p) or ("RUN" in p) or ("execute" in p) or ("EXECUTE" in p) or ("start" in p) or ("START" in p)) and (("control panel" in p) or ("CONTROL PANEL" in p) or ("control-panel" in p) or ("CONTROL-PANEL" in p)) and (("not" not in p) and ("NOT" not in p) and ("don't" not in p) and ("DON'T" not in p) and ("donot" not in p) and ("DONOT" not in p) and ("do not" not in p) and ("DO NOT" not in p)):
    pyttsx3.speak("opening control panel")
    os.system("control panel")

  elif (("open" in p) or ("OPEN" in p) or ("play" in p) or ("PLAY" in p)  or ("run" in p) or ("RUN" in p) or ("execute" in p) or ("EXECUTE" in p) or ("start" in p) or ("START" in p)) and (("notepad" in p) or ("NOTEPAD" in p) or ("editor" in p) or ("EDITOR" in p)) and (("not " not in p) and ("NOT " not in p) and ("don't " not in p) and ("DON'T " not in p) and ("donot " not in p) and ("DONOT " not in p) and ("do not " not in p) and ("DO NOT " not in p)):
    pyttsx3.speak("opening notepad")
    os.system("notepad")

  elif (("open" in p) or ("OPEN" in p) or ("play" in p) or ("PLAY" in p)  or ("run" in p) or ("RUN" in p) or ("execute" in p) or ("EXECUTE" in p) or ("start" in p) or ("START" in p)) and (("wordpad" in p) or ("WORDPAD" in p) or ("word" in p) or ("WORD" in p)) and (("not" not in p) and ("NOT" not in p) and ("don't" not in p) and ("DON'T" not in p) and ("donot" not in p) and ("DONOT" not in p) and ("do not" not in p) and ("DO NOT" not in p)):
    pyttsx3.speak("opening wordpad")
    os.system("start wordpad")

  elif (("open" in p) or ("OPEN" in p) or ("play" in p) or ("PLAY" in p)  or ("run" in p) or ("RUN" in p) or ("execute" in p) or ("EXECUTE" in p) or ("start" in p) or ("START" in p)) and (("CALCULATOR" in p) or ("calculator" in p) or ("CALCI" in p) or ("calci" in p)) and (("not" not in p) and ("NOT" not in p) and ("don't" not in p) and ("DON'T" not in p) and ("donot" not in p) and ("DONOT" not in p) and ("do not" not in p) and ("DO NOT" not in p)):
    pyttsx3.speak("opening calculator")
    os.system("start calc")

  elif (("open" in p) or ("OPEN" in p) or ("play" in p) or ("PLAY" in p)  or ("run" in p) or ("RUN" in p) or ("execute" in p) or ("EXECUTE" in p) or ("start" in p) or ("START" in p)) and (("paint" in p) or ("PAINT" in p) or ("MSPAINT" in p) or ("mspaint" in p)) and (("not" not in p) and ("NOT" not in p) and ("don't" not in p) and ("DON'T" not in p) and ("donot" not in p) and ("DONOT" not in p) and ("do not" not in p) and ("DO NOT" not in p)):
    pyttsx3.speak("opening paint")
    os.system("mspaint")

  elif (("open" in p) or ("OPEN" in p) or ("play" in p) or ("PLAY" in p)  or ("run" in p) or ("RUN" in p) or ("execute" in p) or ("EXECUTE" in p) or ("start" in p) or ("START" in p)) and (("excel" in p) or ("EXCEL" in p) or ("EXCELSHEET" in p) or ("excelsheet" in p)) and (("not" not in p) and ("NOT" not in p) and ("don't" not in p) and ("DON'T" not in p) and ("donot" not in p) and ("DONOT" not in p) and ("do not" not in p) and ("DO NOT" not in p)):
    pyttsx3.speak("opening excel")
    os.system("start excel")

  elif (("open" in p) or ("OPEN" in p) or ("play" in p) or ("PLAY" in p)  or ("run" in p) or ("RUN" in p) or ("execute" in p) or ("EXECUTE" in p) or ("start" in p) or ("START" in p)) and (("eclipse" in p) or ("ECLIPSE" in p) or ("JAVA ECLIPSE" in p) or ("java eclipse" in p)) and (("not" not in p) and ("NOT" not in p) and ("don't" not in p) and ("DON'T" not in p) and ("donot" not in p) and ("DONOT" not in p) and ("do not" not in p) and ("DO NOT" not in p)):
    pyttsx3.speak("opening eclipse hold for sometime")
    os.system("eclipse")

  elif (("open" in p) or ("OPEN" in p) or ("play" in p) or ("PLAY" in p)  or ("run" in p) or ("RUN" in p) or ("execute" in p) or ("EXECUTE" in p) or ("start" in p) or ("START" in p)) and (("virtual box" in p) or ("VIRTUAL BOX" in p) or ("VM" in p) or ("vm" in p)) and (("not" not in p) and ("NOT" not in p) and ("don't" not in p) and ("DON'T" not in p) and ("donot" not in p) and ("DONOT" not in p) and ("do not" not in p) and ("DO NOT" not in p)):
    pyttsx3.speak("opening oracle vm virtualbox")
    os.system("virtualbox")

  elif ("exit" in p) or ("EXIT" in p) or ("quit" in p) or ("QUIT" in p) or ("close" in p) or ("CLOSE" in p):
    pyttsx3.speak("THANKS FOR VISITING! HAVE A NICE DAY!")
    break;

  else:
    print("doesn't recognize")


   