import webbrowser
import time

timer = 0

print ('This program started on ' + time.ctime())

print ('Program Menu')
print ('1. Start Program')

while (timer < 3):
    timer = timer + 1
    time.sleep(5.0)
    if (timer == 1):
        print('Opening Google')
        webbrowser.open("http://www.google.com")

    elif (timer == 2):
        print('Opening Facebook')
        webbrowser.open("http://www.facebook.com")

    else:
        print('Opening Youtube')
        webbrowser.open("http://www.youtube.com")

print ('You are now done with your work!')
