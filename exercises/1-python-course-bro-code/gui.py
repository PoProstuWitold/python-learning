from tkinter import *

window = Tk() #instantiate an instance of a window
window.geometry("420x420")
window.title("First GUI program")

icon = PhotoImage(file='exercises/1-python-course-bro-code/logo.png')
window.iconphoto(True,icon)
window.config(background="#5cfcff")

window.mainloop() #place window on computer screen, listen for events