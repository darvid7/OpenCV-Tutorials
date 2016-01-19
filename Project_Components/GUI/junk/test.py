# assuming Python3
import Tkinter as tk
import subprocess as sub

WINDOW_SIZE = "600x400"

root = tk.Tk()
root.geometry(WINDOW_SIZE)

tk.Button(root, text="Push me!", command=lambda: sub.call('something.py')).pack()

root.mainloop()