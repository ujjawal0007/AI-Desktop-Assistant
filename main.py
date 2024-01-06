
import webbrowser
import ai_zira
import ai_david
import wikipedia
from artifical import intelligence as smart
from artifical import chat as chat
import datetime
import time
print("choose AI gender\n1.Male\n2.female\n3.text male\n4.text female\n")
k = int(input("enter Choice :- "))

if k == 1 or k == 3:
    sir = ai_david.ai()
elif k == 2 or k == 4:
    sir = ai_zira.ai()
else:
    print("restart the engine.....")
    print("Enginge Going to exit in 10", end="")
    for i in range(9, 0, -1):
        time.sleep(0.5)
        print(i, end="")
sir.wishkr()

sir.speak("I am your assistant")
sir.speak("How can i help you")

r = True
while r:
    if k == 1 or k == 2:
        query = sir.chugli().upper()
    else:
        query = input("enter your query :- ").upper()

    if "open ai".upper() in query:
        sir.speak("What is your query")
        if k == 1 or k == 2:
            query = sir.chugli().upper()
        else:
            query = input("what is your query :- ").upper()
        smart(query)
    elif "bye".upper() in query:
        sir.bye()
        r = False

    elif "open".upper() in query:
        sir.speak("there is some result in your screen....")
        l = query.split("open".upper())
        # print(l)
        webbrowser.open("www."+l[1][1:len(l[1])]+".com")
    elif "play".upper() in query:
        sir.speak("Playing Music....")
        song = query.split("play".upper())
        webbrowser.open(
            "https://www.youtube.com/results?search_query=" + song[1])
    elif "current time".upper() in query:
        hour = sir.times()
        min = datetime.datetime.now().minute
        sir.speak(f"The Time is {hour} : {min}")
    elif "today date".upper() in query:
        date = datetime.datetime.now().date()
        sir.speak(f"Today is {date}")
    elif "your name".upper() in query:

        if k == 1 or k == 3:
            sir.speak("My name is David")
        else:
            sir.speak("My name is Zira")
    elif "your age".upper() in query:
        sir.speak("I am computer program, programmed on 2 october 2023 ")
    elif "your gender".upper() in query:
        if k == 1 or k == 3:
            sir.speak("I am male")
        else:
            sir.speak("I am female")
    elif "your profession".upper() in query:
        sir.speak("I am a computer program")
    elif "your hobby".upper() in query:
        sir.speak("my hobby is learn more and  more")
    elif "your country".upper() in query:
        sir.speak("I am from india")
    elif "your city".upper() in query:
        sir.speak("I am from Dhampur")
    elif "your state".upper() in query:
        sir.speak("I am from uttar pradesh")
    elif "your college".upper() in query:
        sir.speak("I am from MIT Moradabad")
    elif "your university".upper() in query:
        sir.speak("I am from AKTU")
    elif 'google'.upper() in query:
        sir.speak('Searching ai...')
        query = query.replace("google".upper(), "")
        results = wikipedia.summary(query, sentences=5)
        sir.speak("According to google")
        print(results)
        sir.speak(results)

    else:
        if query == "none".upper():
            pass
        else:
            ans = chat(query)
            sir.speak(ans)
