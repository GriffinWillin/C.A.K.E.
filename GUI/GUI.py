from tkinter import *
import os
from PIL import Image, ImageTk

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

################################# Window #################################
window = Tk()
window.title("C.A.K.E")
app = CAKE(window)
##########################################################################

################################# Images #################################
diagram = Image.open((os.path.join('GUI', 'Images', 'Ellipse 1.png')))
diagram_image = ImageTk.PhotoImage(diagram)

slices = Image.open((os.path.join('GUI', 'Images', 'slices.png')))
slices_image = ImageTk.PhotoImage(slices)

# plus = Image.open(os.path.join('Images', 'plus.png'))
# plus_image = ImageTk.PhotoImage(file = os.path.join('Images'))

# minus = Image.open(os.path.join('Images', 'minus.png'))
# minus_image = ImageTk.PhotoImage(file = os.path.join('Images'))

# num_slices = Image.open(os.path.join('Images', ))
# num_slices_image = ImageTk.PhotoImage(file = os.path.join('Images'))

# status = Image.open(os.path.join('Images'))
# status_image = ImageTk.PhotoImage(file = os.path.join('Images'))

start = Image.open(os.path.join('GUI', 'Images', "Start.png"))
start_image = ImageTk.PhotoImage(start)

# align = Image.open(os.path.join('Images'))
# align_image = ImageTk.PhotoImage(file = os.path.join('Images'))

e_stop = Image.open(os.path.join('GUI', 'Images', "Stop.png"))
e_stop_image = ImageTk.PhotoImage(e_stop)

# Labels
pie = Label(window, image = diagram_image)
status = Label(window, text = "status")
num = Label(window, image = slices_image)

################################ Buttons #################################
b_plus = Button(window, text = "+", command = CAKE.add, font = ('lobster', 45))
b_minus = Button(window, text = "-", command = CAKE.remove, font = ('lobster', 45))
b_start = Button(window, image = start_image, command = CAKE.begin)
# b_align = Button(window, image = align, command = CAKE.get_dim)
b_e_stop = Button(window, image = e_stop_image, command = exit)
# b_plus = Button(window, text = "+", command = CAKE.add)
# b_minus = Button(window, text = "-", command = CAKE.remove)
# b_start = Button(window, text = "Start", command = CAKE.begin)
# b_align = Button(window, text = "Align Slicer", command = CAKE.get_dim)
# b_e_stop = Button(window, text = "Emergency Stop", command = exit, fg = "red", highlightbackground = "red", highlightthickness = 5, bg = "red")

############################# Grid or Pack ###############################

################################## GRID ##################################
pie.grid(column = 1, row = 0)
status.grid(column = 2, row = 2, sticky = N+E)
num.grid(column = 1, row = 1, sticky = N+E+W)
b_plus.grid(column = 0, row = 2, sticky = E)
b_minus.grid(column = 2, row = 2, sticky = W)
b_start.grid(column = 5, row = 3, sticky = S+E)
b_e_stop.grid(column = 5, row = 4, sticky = S+E)



##########################################################################


################################## PACK ##################################
# diagram.pack(side = TOP)
# status.pack(side = RIGHT)
# num.pack(side = LEFT)
# b_plus.pack(side = BOTTOM)
# b_minus.pack(side = BOTTOM)
# b_start.pack(side = TOP)
# # b_align.pack()
# b_e_stop.pack(side = TOP, padx = 100, pady = 50, ipadx = 15, ipady = 40)
##########################################################################

################################## MAIN ##################################

window.mainloop()