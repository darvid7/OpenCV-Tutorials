import Tkinter
import subprocess
import cv2
import os

def somefunction():
    print 'start'
    print 'needs leap motion to be plugged in to start'
    os.system('python ~/Desktop/run_via_gui/mySample.py')
    print 'end'

def openApplication(name=None):
    print 'open'
    subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/Leap Motion.app"])
    print 'closed'

root = Tkinter.Tk()

root.title = ('Test GUI')
root.geometry('600x400')


scriptButton = Tkinter.Button(root, text='run something', command = somefunction)
scriptButton.pack()



root.mainloop()
