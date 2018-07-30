from tkinter import*
import random

# To set up the window with  final mainloop()
win =Tk()

# To define labels and buttons
LabelN1 = Label( win, relief = 'groove', width = 2 )
LabelN2 = Label( win, relief = 'groove', width = 2 )
LabelN3 = Label( win, relief = 'groove', width = 2 )
LabelN4 = Label( win, relief = 'groove', width = 2 )
LabelN5 = Label( win, relief = 'groove', width = 2 )
LabelN6 = Label( win, relief = 'groove', width = 2 )

ButtonGet = Button( win )
ButtonReset = Button( win )

# Grid geometry
LabelN1.grid( row = 1, column = 1, padx = 10 )
LabelN2.grid( row = 1, column = 2, padx = 10 )
LabelN3.grid( row = 1, column = 3, padx = 10 )
LabelN4.grid( row = 1, column = 4, padx = 10 )
LabelN5.grid( row = 1, column = 5, padx = 10 )
LabelN6.grid( row = 1, column = 6, padx = 10 )


ButtonGet.grid( row = 3, column = 0, columnspan = 4 )
ButtonReset.grid( row = 3, column = 5, columnspan = 2 , sticky = 'ws')

# Static properties
win.title('Lotto Generator')
ButtonGet.configure( text = 'Lucky Numbers' )
ButtonReset.configure( text = 'Reset')


# Initial condition
LabelN1.configure( text = '---' )
LabelN2.configure( text = '---' )
LabelN3.configure( text = '---' )
LabelN4.configure( text = '---' )
LabelN5.configure( text = '---' )
LabelN6.configure( text = '---' )
ButtonReset.configure( state = DISABLED )

# To generate not repeatedly six random numbers
nums = []
n = 1
while n <= 6:
    randNum = random.randint(1, 49)
    if randNum not in nums:
        nums.append(randNum)
        n += 1

# To make Pick() and Reset()

def Pick() :
    LabelN1.configure( text = nums[0] )
    LabelN2.configure( text = nums[1] )
    LabelN3.configure( text = nums[2] )
    LabelN4.configure( text = nums[3] )
    LabelN5.configure( text = nums[4] )
    LabelN6.configure( text = nums[5] )
    ButtonGet.configure(state=DISABLED)
    ButtonReset.configure(state=NORMAL)

def Reset() :
    LabelN1.configure(text='---')
    LabelN2.configure(text='---')
    LabelN3.configure(text='---')
    LabelN4.configure(text='---')
    LabelN5.configure(text='---')
    LabelN6.configure(text='---')
    ButtonGet.configure(state=NORMAL)
    ButtonReset.configure(state=DISABLED)

# To call the command function Pick() and Reset()
ButtonGet.configure( command = Pick )
ButtonReset.configure( command = Reset )

# To call the window
win.mainloop()

