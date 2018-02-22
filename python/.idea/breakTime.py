import webbrowser
import time

print("Program started: " + time.ctime())
while(True):
    time.sleep(5)
    webbrowser.open("http://www.google.com")