import tkinter as tk
import time

def update_timeText():
    # Get the current time, note you can change the format as you wish
    current = time.strftime("%Y/%m/%d %H:%M:%S")
    # Update the timeText Label box with the current time
    timeText.configure(text=current)
    # Call the update_timeText() function after 1 second
    win.after(1000, update_timeText)

win = tk.Tk()
win.title("Simple Clock Example")

# Create a timeText Label (a text box)
timeText = tk.Label(win, bg= 'black', text="", fg='white', font=("Helvetica", 50))
timeText.pack()
update_timeText()
win.mainloop()