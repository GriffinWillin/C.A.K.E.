from tkinter import *

DEBUG = FALSE

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

# Images
diagram = Image()
######################### MAIN ##############################

window = Tk()

window.title("C.A.K.E")

app = CAKE(window)

window.mainloop()
