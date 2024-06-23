from distutils.version import LooseVersion
import pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import pyautogui
import subprocess
import cv2

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

wake_word = "Jarvis"


def open_notepad():
    try:
        subprocess.Popen(["notepad.exe"])
        print("Notepad is now open.")
    except Exception as E:
        print(f"Error: {E}")


def open_command_prompt():
    try:
        # Open the Command Prompt
        subprocess.Popen("cmd.exe", shell=True)
    except Exception as E:
        print(f"An error occurred: {E}")


def open_camera():
    # Initialize the camera
    cap = cv2.VideoCapture(0)  # 0 is the default camera, you can change it if you have multiple cameras

    if not cap.isOpened():
        print("Error: Could not open the camera.")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Cannot read a frame from the camera.")
            break

        # Display the captured frame
        cv2.imshow('Camera Feed', frame)

        # Exit the camera feed by pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the OpenCV window
    cap.release()
    cv2.destroyAllWindows()


def restart_windows():
    try:
        os.system('shutdown /r /t 0')  # /r stands for restart, /t is the time delay (0 seconds in this case)
        print("System is restarting...")
    except Exception as e:
        print("An error occurred:", e)


def shutdown_computer():
    try:
        os.system("shutdown /s /t 0")
    except Exception as e:
        print("An error occurred:", str(e))


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)
    print("The current date is " + str(day) + "/" + str(month) + "/" + str(year))


def close_browser():
    # Close Microsoft Edge using taskkill command in Windows
    os.system("taskkill /f /im msedge.exe")


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning sir!")
        print("Good Morning sri!")

    elif 12 <= hour < 18:
        speak("Good Afternoon sir!")
        print("Good Afternoon sir!")

    else:
        speak("Good Evening sir!")
        print("Good Evening sir!")

    speak("I am Jarvis your personal assistant. Please tell me how may I help you")
    print("I am Jarvis your personal assistant. Please tell me how may I help you")


def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\NITISH KUMAR\\OneDrive\\Desktop\\Projects\\JrviaAI_Main\\screenshots\\ss1.png")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")
        return "None"

    # Convert the recognized query to lowercase for easier comparison
    query = query.lower()

    # Remove punctuation and extra whitespaces
    query = query.replace('?', '')
    query = query.replace('.', '')
    query = query.strip()

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('marurinitish1834@gmail.com', 'Nitish@1843')
    server.sendmail('marurinitish1834@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        camera_opened = False  # Variable to track if the camera is currently open
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'open camera' in query:
            open_camera()
            camera_opened = True

        elif 'close camera' in query or 'stop camera' in query or 'exit camera' in query:
            if camera_opened:
                cv2.destroyAllWindows()  # Close the camera feed window
                camera_opened = False
            else:
                speak("The camera is not currently open.")
                print("The camera is not currently open.")


        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            print('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print("According to Wikipedia")
            print(results)
            speak(results)

        elif "who are you" in query:
            speak("I'm JARVIS I'm a desktop voice assistant.")
            print("I'm JARVIS I'm a desktop voice assistant.")

        elif "how are you" in query:
            speak("I'm fine sir, What about you?")
            print("I'm fine sir, What about you?")

        elif "fine" in query:
            speak("Glad to hear that sir!!")
            print("Glad to hear that sir!!")

        elif 'date' in query:
            date()

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open notepad' in query:
            open_notepad()

        elif 'open command prompt' in query:
            open_command_prompt()

        elif 'search in youtube' in query:
            speak('What should I search?')
            print('What should I search?')
            search_query = takeCommand().lower()
            url = 'https://www.youtube.com/search?q=' + search_query
            webbrowser.open(url)
            speak(f'Here is what I found for {search_query} on youtube')

        elif 'open google maps' in query:
            webbrowser.open("https://www.google.com/maps/@17.4782602,78.3500869,15z?entry=ttu")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'close google' in query:
            os.system("taskkill /im chrome.exe /f")
            speak("Google has been closed.")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open chat GPT' in query:
            webbrowser.open("chatgpt.com")

        elif 'search in google' in query:
            speak('What should I search?')
            print('What should I search?')
            search_query = takeCommand().lower()
            url = 'https://www.google.com/search?q=' + search_query
            webbrowser.open(url)
            speak(f'Here is what I found for {search_query} on google')
        elif 'close browser' in query:
            close_browser()

        elif 'play music' in query:
            music_dir = 'C:\\Users\\NITISH KUMAR\\OneDrive\\Desktop\\songs_dir'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(strTime)

        elif 'open vs code' in query:
            codePath = "C:\\Users\\NITISH KUMAR\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open py' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.2.2\\bin\\pycharm64.exe"
            os.startfile(codePath)

        elif 'open Visual Studio' in query:
            codePath = "C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\Common7\\IDE\\devenv.exe"
            os.startfile(codePath)

        elif 'open star uml' in query:
            codePath = "C:\\Program Files\\StarUML\\StarUML.exe"
            os.startfile(codePath)

        elif 'open project file' in query:
            codePath = "C:\\Users\\NITISH KUMAR\\OneDrive\\Desktop\\Projects"
            os.startfile(codePath)


        elif 'email to nitish' in query:
            try:
                speak("What should I say?")
                print("What should I say?")
                content = takeCommand()
                to = "marurinitish1843@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
                print("Email has been sent!")
            except Exception as e:
                speak("Sorry boss. I am not able to send this email")
                print("Sorry boss. I am not able to send this email")

        elif "remember that" in query:
            speak("What should I remember")
            print("What should I remember")
            data = takeCommand()
            speak("You said me to remember that" + data)
            print("You said me to remember that " + str(data))
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you remember anything" in query:
            remember = open("data.txt", "r")
            speak("You told me to remember that" + remember.read())
            print("You told me to remember that " + str(remember))

        elif "take a screenshot" in query:
            screenshot()
            speak("I've taken screenshot, please check it")
            print("I've taken screenshot, please check it")

        elif 'restart' in query:
            restart_windows()

        elif 'shutdown' in query:
            shutdown_computer()

        elif 'quit' in query:
            speak("Goodbye sir!")
            print("Goodbye sir!")
            exit()
