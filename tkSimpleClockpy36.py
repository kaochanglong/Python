import tkinter as tk
import time

def update_timeText():
    # To get the current time on your system, and the format can be changed as you wish
    current = time.strftime("%Y/%m/%d %H:%M:%S")
    # To update the timeText (in the tkinter Label box) with the current time
    timeText.configure(text=current)
    # After method in tkinter can be used to generate an event at a specific time
    # In this case, after method is used to call the update_timeText() function after 1 second
    win.after(1000, update_timeText)

# To set up the window with  final mainloop()
win = tk.Tk()
# To set up the window title
win.title("Simple Clock Example")

# To create and setup a timeText Label (the format such as bg, fg,and font can be changed as you wish )
timeText = tk.Label(win, bg= 'black', text="", fg='white', font=("Helvetica", 50))
timeText.pack()
# To call update_timeText() function
update_timeText()
# To set up the window with  final mainloop()
win.mainloop()
