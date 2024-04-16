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
        input = 0
        output = 0
        self.input = input
        self.output = output
		
	# Accessor
    @property
    def input(self):
        return self._input
	
	# Mutator with range checking to control length of input
    @input.setter
    def input(self, value):
        if (value <= 1):
            value = 2
        elif (value > 8):
            value = 8
        self._input = value
		
	# Accessor
    @property
    def output(self):
        return self._output
	
	# Mutator with range checking to control length of output
    @output.setter
    def output(self, value):
        if (value <= 1):
            value = 2
        elif (value > 8):
            value = 8
        self._output = value

    # Functions
    def add(self):
        pass
    
    def remove(self):
        pass

    def begin(self):
        pass

    def get_dim(self):
        pass

###################
window = Tk()
window.title("C.A.K.E")
app = CAKE(window)
###################

# # Images
slices = PhotoImage(file = os.path.join('Images', 'slices.png'))
# plus = PhotoImage(file = os.path.join('Images'))
# minus = PhotoImage(file = os.path.join('Images'))
# # num_slices = PhotoImage(file = os.path.join('Images'))
# status = PhotoImage(file = os.path.join('Images'))
# start = PhotoImage(file = os.path.join('Images'))
# #align = PhotoImage(file = os.path.join('Images'))
# e_stop = PhotoImage(file = os.path.join('Images', 'Stop.png'))

# Labels
diagram = Label(window, text = "picture here")
status = Label(window, text = "status")
num = Label(window, image = slices)

# Buttons
# b_plus = Button(window, image = plus, command = CAKE.add)
# b_minus = Button(window, image = minus, command = CAKE.remove)
# b_start = Button(window, image = start, command = CAKE.begin)
# b_align = Button(window, image = align, command = CAKE.get_dim)
# b_e_stop = Button(window, image = e_stop, command = exit)
b_plus = Button(window, text = "+", command = CAKE.add)
b_minus = Button(window, text = "-", command = CAKE.remove)
b_start = Button(window, text = "Start", command = CAKE.begin)
b_align = Button(window, text = "Align Slicer", command = CAKE.get_dim)
b_e_stop = Button(window, text = "Emergency Stop", command = exit, fg = "red", highlightbackground = "red", highlightthickness = 5, bg = "red")

# Grid/Pack

diagram.pack()
status.pack()
num.pack()
b_plus.pack()
b_minus.pack()
b_start.pack()
b_align.pack()
b_e_stop.pack(padx = 100, pady = 50, ipadx = 15, ipady = 40)
######################### MAIN ##############################

window.mainloop()
