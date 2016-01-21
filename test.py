import Tkinter as tk #Importing the GUI Library
import time #Importing Time#
def onKeyPress(event): #Defining my function of keypress, and using GUI Library to get the keypress.
        time.sleep(1) #Telling it to wait one second otherwise it will crash.
        text.insert('end', 'You pressed %s\n' % (event.char, )) #Telling the user if he pressed the key or not.
        speed = 50 #Setting the speed to 50 default
        while speed > 0:
            if event.char == 'w': #if key pressed = w:
                speed = speed + 1 #Change speed by 1
                time.sleep(1)
            if event.char == 's':
                speed = speed - 1
                time.sleep(1)
                print(speed)


root = tk.Tk()
root.geometry('300x200')
text = tk.Text(root, background='black', foreground='white', font=('Comic Sans MS', 12))
text.pack()
root.bind('<KeyPress>', onKeyPress)
root.mainloop()