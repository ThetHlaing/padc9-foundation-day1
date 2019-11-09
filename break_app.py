import webbrowser
import time

break_times = 5

print ("The current time is ", time.ctime())

while(break_times > 0):
    time.sleep(20)
    webbrowser.open("www.youtube.com")
    break_times = break_times - 1
