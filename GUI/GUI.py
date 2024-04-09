from tkinter import *
import os

DEBUG = FALSE

WIDTH = 800
HEIGHT = 600

class CAKE(Frame):
    def __init__(self, master):
        super().__init__(master, bg = 'grey')

        # A list represented by a string to store all values entered and returned
		# so that I can interate backwards to remove the last button and limit the characters
		# of the display
        input = ''
        output = ''
        self.input = input
        self.output = output
		
	# Accessor
    @property
    def input(self):
        return self._input
	
	# Mutator with range checking to control length of input
    @input.setter
    def input(self, value):
        if (len(value) <= 14):
            value = value
        else:
            value = value[:14]
        self._input = value
		
	# Accessor
    @property
    def output(self):
        return self._output
	
	# Mutator with range checking to control length of output
    @output.setter
    def output(self, value):
        if (len(value) <= 14):
            value = value
        else:
            value = value[:11] + '...'
        self._output = value

###################
window = Tk()
###################

# Images
slices = PhotoImage(file = os.path.join('Images'))
plus = PhotoImage(file = os.path.join('Images'))
minus = PhotoImage(file = os.path.join('Images'))
num_slices = PhotoImage(file = os.path.join('Images'))
status = PhotoImage(file = os.path.join('Images'))
start = PhotoImage(file = os.path.join('Images'))
align = PhotoImage(file = os.path.join('Images'))
e_stop = PhotoImage(file = os.path.join('Images'))

# Buttons
b_plus = Button(window, image = plus, command = add)
b_minus = Button(window, image = minus, command = remove)
b_start = Button(window, image = start, command = begin)
b_align = Button(window, image = align, command = get_dim)
b_e_stop = Button(window, image = e_stop, command = exit)

######################### MAIN ##############################



window.title("C.A.K.E")

app = CAKE(window)

window.mainloop()
