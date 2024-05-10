#import all libraries
import pineworkslabs.RPi as GPIO
from time import sleep
import customtkinter
import os
from PIL import Image, ImageTk

# CONSTANTS
DIR_PIN = 20
STEP_PIN = 21
ENA = 22
DIR_PIN1 = 24
STEP_PIN1 = 25
ENA1 = 26
STOP = 19
theBug = True
runnin = True
h_tick = 0
Theme = {"bg":"#90CAF9", "text":"white", "button":"teal", "hover":"lightgrey", "tile":"lightgrey", "guide":"white", "splash":"red"}
DEPTH = 70
SPEED = 50
CUTS = 0
in_opr = False

######## SETUP GPIO ####################
GPIO.setmode(GPIO.LE_POTATO_LOOKUP)

pins = [STEP_PIN, DIR_PIN, ENA, STEP_PIN1, DIR_PIN1, ENA1]

for i in pins:
    GPIO.setup(i, GPIO.OUT)

GPIO.setup(STOP, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

########## ALL FUNCTIONS ##################

def step_motor(steps, delay, pin):

    # Step the motor
    for _ in range(steps):
        GPIO.output(pin, GPIO.HIGH)
        sleep(delay)
        GPIO.output(pin, GPIO.LOW)
        sleep(delay)
        #print(f"process complete {_} : {pin}")
def estop(): # disable both motors, turn off operation
	global in_opr
	global h_tick
	in_opr = False
	
	GPIO.cleanup()
	# ~ GPIO.output(DIR_PIN1, GPIO.HIGH) # clockwise/up
	# ~ step_motor(steps=h_tick, delay = .005, pin = STEP_PIN1)
	# ~ h_tick = 0
	GPIO.output(ENA1, GPIO.HIGH) # stop motor 2
	GPIO.output(ENA, GPIO.HIGH) # stop 1
	print("ESTOPPPP!!!")
	
def rotate_tray(degrees, speed): # motor 1
	global in_opr
	GPIO.output(ENA, GPIO.LOW) # start motor 1
	GPIO.output(DIR_PIN, GPIO.HIGH) # Clockwise
	rel_ang = 0
	while(rel_ang < degrees):
		if (in_opr):
			if GPIO.input(STOP) == 1:
				estop()
			else:
				step_motor(steps=1, delay = speed, pin = STEP_PIN)
				rel_ang += 1.8
				rel_ang = round(rel_ang,5)
				if (theBug):
					print(f"ANGLE {rel_ang}, {in_opr}")
				#print(GPIO.input(STOP))
		else:
			print("hello")
			break
	GPIO.output(ENA, GPIO.HIGH) # stop motor 1
	
def cut(depth, speed): # motor 2
        global in_opr
        global h_tick
        GPIO.output(ENA1, GPIO.LOW) # start motor 2
        print(f"THIS IS HTICK: {h_tick}")
        if (h_tick != 0):
                GPIO.output(DIR_PIN1, GPIO.HIGH) # clockwise/up
                step_motor(steps=h_tick, delay = .005, pin = STEP_PIN1)
                h_tick = 0

        GPIO.output(DIR_PIN1, GPIO.LOW) # anticlockwise/down
        rel_len = 0
        while(rel_len < depth): # Going down
                if(in_opr):
                        if GPIO.input(STOP) == 1:
                                estop()

                        step_motor(steps=1, delay = speed, pin = STEP_PIN1)
                        h_tick += 1 # 1 tick = 2/5 mm
                        rel_len += .4
                        rel_len = round(rel_len,5)
                        if (theBug):
                                print(f"LEN {rel_len}, {h_tick} ")
                                #print(GPIO.input(STOP))
                else:
                        print("hello")
                        break
                        
        GPIO.output(DIR_PIN1, GPIO.HIGH) # clockwise/up
        while(rel_len > 0): # going up
                 if(in_opr):
                        if GPIO.input(STOP) == 1:
                                estop()

                        step_motor(steps=1, delay = speed, pin = STEP_PIN1)
                        h_tick -= 1 # 1 tick = 2/5 mm
                        rel_len -= .4
                        rel_len = round(rel_len,5)
                        if (theBug):
                                print(f"LEN {rel_len}, {h_tick} ")
                                #print(GPIO.input(STOP))
                 else:
                        print("hello")
                        break
        # ~ GPIO.output(DIR_PIN1, GPIO.HIGH) # clockwise/up
        # ~ step_motor(steps=h_tick, delay = speed, pin = STEP_PIN1)
        # ~ h_tick = 0
        GPIO.output(ENA1, GPIO.HIGH) # stop motor 1
				
        
		
def cut_cycle(slices, wait, speed = 50, depth = None):
        global in_opr
        rot_speed = (.0625*(speed/100))
        cut_speed = (.020125*(speed/100))
        in_opr = True
        i = 0
        while (i < slices/2):
                if(in_opr):
                        rotate_tray((360/slices),rot_speed) # rotate tray
                        sleep(.5)
                        if(in_opr):
                                cut(depth, cut_speed)
                                i += 1  # raise cut counter
                        if(theBug):
                                print(f"{i} out of {round(slices/2)}")
                        sleep(wait)
                else:
                        print("hello")
                        break

############ TKinter classes ###################

class MainMenu(customtkinter.CTkFrame):
    def __init__(self, master):
        global Theme
        super().__init__(master, border_width=2, height=600, width=1024)
        gifs = ["2_slices.png", "4_slices.png", "6_slices.png", "8_slices.png"]
        self.images = []
        self.theme = Theme

        for i in range(len(gifs)):
            image = Image.open(os.path.join("Images", f"{gifs[i]}"))
            image_i = customtkinter.CTkImage(image, size=(335,335))
            self.images.append(image_i)

        self.bg = customtkinter.CTkLabel(master, text="", bg_color=self.theme["bg"])
        self.bg.grid(column=0, columnspan=26, row=0, rowspan=26, sticky="news")

        self.splash = customtkinter.CTkLabel(master, text="C.A.K.E", text_color=self.theme["splash"], bg_color=self.theme["bg"], anchor='center', font=("Yu Mincho Demibold", 80))
        self.splash.place(x=self.winfo_screenwidth()//3*1.65, y=300, anchor="center")

        self.diagram = customtkinter.CTkLabel(master, image=self.images[0], text="", padx=0, anchor='center')
        self.diagram.grid(column=0, columnspan=5, row=1, rowspan=4, padx=0, sticky="news")
        
        self.grey = customtkinter.CTkLabel(master, text="", font=("Trebuchet MS", 65), anchor="center", fg_color="lightgrey") #width=self.winfo_screenwidth()/10 *3.07, height=self.winfo_screenheight()/9 * 1.75)
        self.grey.grid(column=0, columnspan=5, row=20, rowspan=11, pady=2, padx=10, sticky="news")

        self.add_slice = customtkinter.CTkButton(master, text_color="black", fg_color="white", bg_color="lightgrey", hover_color="grey", text="+", corner_radius=48, font=("Trebuchet MS", 60), anchor="center", command=master.add_slices) #, width=self.winfo_screenwidth()/1 *0.01, height=self.winfo_screenheight()/10 * 0.87, command=master.add_slices)
        self.add_slice.grid(column=3, columnspan=2, row=22, rowspan=3, padx=10, sticky="news")
        
        self.remove_slice = customtkinter.CTkButton(master, text_color="black", fg_color="white", bg_color="lightgrey", hover_color="grey", text="-", corner_radius=48, font=("Trebuchet MS", 60), anchor="center", command=master.remove_slices) #, width=self.winfo_screenwidth()/10 *0.97, height=self.winfo_screenheight()/9 * 0.85, command=master.remove_slices)
        self.remove_slice.grid(column=0, columnspan=2, row=22, rowspan=3, padx=10, sticky="news")
        
        self.slice_num = customtkinter.CTkLabel(master, text="Number of Slices", bg_color=self.theme["bg"], font=("Trebuchet MS", 35), anchor="center")
        self.slice_num.grid(column=0, columnspan=5, row=9, padx=10, sticky="news")

        self.slice = customtkinter.CTkLabel(master, text="2", text_color=self.theme["text"], fg_color="black", font=("Trebuchet MS", 60), anchor="center")
        self.slice.grid(column=0, columnspan=5, row=20, padx=10, sticky="news")

        self.themes = customtkinter.CTkButton(master, text_color="white", fg_color=self.theme["button"], text="Theme Select", font=("Trebuchet MS", 30), anchor="center", command=master.theme_select)
        self.themes.grid(column=20, columnspan=2, row=0, rowspan=2, pady=(10), sticky="news")
        
        self.options = customtkinter.CTkButton(master, text_color=self.theme["text"], fg_color=self.theme["button"], bg_color=self.theme["bg"], text="Settings", font=("Trebuchet MS", 30), anchor="center", command=master.open_settings)
        self.options.grid(column=23, columnspan=2, row=0, rowspan=2, pady=(10), sticky="news")

        self.tile = customtkinter.CTkLabel(master, text="", anchor="center", fg_color=self.theme["tile"], bg_color=self.theme["bg"], width=self.winfo_screenwidth()/4 *2.55, height=self.winfo_screenheight()/3 * 1.45, corner_radius=35)
        self.tile.place(x=self.winfo_screenwidth()//6 *4.34, y=self.winfo_screenheight()//30 *23.75, anchor="center")

        self.guide = customtkinter.CTkLabel(master, text="CONTROLS:", font=("Trebuchet MS", 36), anchor="center", text_color="black", fg_color="lightgrey", bg_color="transparent", corner_radius=0)
        self.guide.place(x=self.winfo_screenwidth()//6 *3.12, y=self.winfo_screenheight()//30 *17.9, anchor="center")

        self.start = customtkinter.CTkButton(master, text_color=self.theme["text"], fg_color="#66BB6A", bg_color="lightgrey", hover_color="green", text="START", font=("Trebuchet MS", 65), anchor="center", width=585, height=self.winfo_screenheight()/3, corner_radius=35,
        command=master.start_run)
        self.start.place(x=self.winfo_screenwidth()//6 *4.21, y=self.winfo_screenheight()//30 *24.44, anchor="center")

        #self.leave = customtkinter.CTkButton(master, text_color="white", fg_color="#E57373", bg_color="lightgrey", hover_color="red", text="STOP", font=("Trebuchet MS", 65), anchor="center", width=300, height=self.winfo_screenheight()/3, corner_radius=35,
        #command=estop)
        #self.leave.place(x=self.winfo_screenwidth()//6 *5.10, y=self.winfo_screenheight()//30 *24.44, anchor="center")
    
class App(customtkinter.CTk):
    '''
    A class that serves as the basis for all menu operations
    '''
    def __init__(self):
        global Theme
        super().__init__(fg_color="#90CAF9")
        self.wm_attributes("-fullscreen", True)
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        self.build_grid(25, 25)
        self.frame = MainMenu(master=self)
        self.slices = 2
        self.DIAGRAMS = [2, 4, 6, 8, 10] # list that changes the image to the amount of slices

    @property
    def slices(self):
        return self._slices
    
    @slices.setter
    def slices(self, value):
        if (value > 8):
            value = 8
        elif (value < 2):
            value = 2
        self._slices = value


    def build_grid(self, columns:int, rows:int, weight_c:int = 1, weight_r:int = 1):
        for i in range(columns+1):
            self.grid_columnconfigure(i, weight = weight_c)
        for i in range(rows+1):
            self.grid_rowconfigure(i, weight = weight_r)

    def get_background(self, image:str):
        image = Image.open(os.path.join("Backgrounds", f"{image}"))
        background_image = customtkinter.CTkImage(image, size=(self.winfo_screenwidth(), self.winfo_screenheight()))
        bg_lbl = customtkinter.CTkLabel(self, text="", image=background_image)
        bg_lbl.place(relheight = 1.0, x=0, y=0)
    
    def add_slices(self):
        global CUTS
        if (CUTS < 3):
            CUTS += 1
        else:
            CUTS = CUTS
        self.slices += 2
        self.frame.diagram.configure(image=(self.frame.images[CUTS]))
        self.frame.slice.configure(text=f"{self.slices}")
        self.frame.diagram.update()
        self.frame.slice.update()
        sleep(0.01)

    def remove_slices(self):
        global CUTS
        if (CUTS > 0):
            CUTS -= 1
        else:
            CUTS = CUTS
        self.slices -= 2
        self.frame.diagram.configure(image=(self.frame.images[CUTS]))
        self.frame.slice.configure(text=f"{self.slices}")
        self.frame.diagram.update()
        self.frame.slice.update()
        sleep(0.01)

    def theme_select(self):
        pick = ThemeSelect(self)
        pick.attributes("-topmost", True)
        pick.mainloop()

    def open_settings(self):
        options = Settings(self)
        print("here")
        options.attributes("-topmost", True)
        options.mainloop()
        
    def leav_me_alone(self):
        global runnin
        estop()
        runnin = False
        exit()
        
    def start_run(self):
        global SPEED, DEPTH, runnin
        
        cut_cycle(self.slices,1,SPEED,DEPTH)

class Settings(customtkinter.CTkToplevel):
    def __init__(self, master):
        global Theme
        global DEPTH
        global SPEED
        super().__init__(fg_color=Theme["bg"])
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        App.build_grid(self, 8, 20)
        self.theme = Theme
        self.build_menu()
        self.master = master
        self.wm_attributes("-fullscreen", True)
        
        
        self.OPTIONS = {self.depth_:f"Depth:{DEPTH}", self.speed_:f"Speed:{SPEED}", self.cut_depth:"CUT DEPTH", self.cut_speed:"CUT SPEED"}
        self.setup_options(list(self.OPTIONS.keys()), list(self.OPTIONS.values()))
        
    def setup_options(self, buttons:list = [], names:list = []):

        for i in range(0, 2):
        
            print(self.OPTIONS[buttons[i]])
            buttons[i].configure(self, text=names[i], font=("Trebuchet MS", 30), text_color=self.theme["text"], bg_color=self.theme["bg"], fg_color=self.theme["button"],
                                                        anchor="center")
        for i in range (len(buttons)):

            if (i % 2 == 0):
                buttons[i].grid(column=1, columnspan=3, row=i+3, rowspan=1, sticky="news")
            else:
                buttons[i].grid(column=5, columnspan=3, row=i+2, rowspan=1, sticky="news")

    def build_menu(self):

        self.splash = customtkinter.CTkLabel(self, text="Settings", text_color=self.theme["text"], bg_color=self.theme["bg"], anchor='center', font=("Yu Mincho Demibold", 85))
        self.splash.grid(column=3, columnspan=3, row=0, sticky="news")

        self.depth_ = customtkinter.CTkLabel(self, font=("Trebuchet MS", 30))

        self.speed_ = customtkinter.CTkLabel(self,font=("Trebuchet MS", 30))

        self.cut_depth = customtkinter.CTkSlider(self, from_=50, to=71, number_of_steps=20, command=self.depth)
        self.cut_depth.set(DEPTH)
        self.cut_speed = customtkinter.CTkSlider(self, from_=30, to=100, number_of_steps=50, command=self.speed)
        self.cut_speed.set(SPEED)
            
        self.back = customtkinter.CTkButton(self, text_color=self.theme["text"], fg_color=self.theme["button"], hover_color=self.theme["hover"], text="RETURN TO C.A.K.E.", font=("Trebuchet MS", 30), border_width=5, border_color=self.theme["tile"], command=self.destroy)
        self.back.grid(column=3, columnspan=3, row=12, rowspan=2, sticky="news")

    def depth(self, n):
        global DEPTH
        DEPTH = round(n)
        self.depth_.configure(text=f"Depth:{DEPTH}")
        print(DEPTH)

    def speed(self, n):
        global SPEED
        SPEED = round(n)
        self.speed_.configure(text=f"Speed:{SPEED}")
        print(SPEED)

class ThemeSelect(customtkinter.CTkToplevel): # turn this into a theme select
    def __init__(self, master):
        global Theme
        super().__init__(fg_color=Theme["bg"])
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        App.build_grid(self, 6, 20)
        self.master = master
        self.wm_attributes("-fullscreen", True)
        self.theme = Theme
        self.create_labels()

        self.red_ = {"button":"#F4511E", "button_border":"#BCAAA4", "hover":"#FF7043", "text":"#FFCCBC", "bg":"#BF360C", "tile":"lightgrey "}
        self.orange_ = {"button":"#FF6F00", "button_border":"#BCAAA4", "hover":"#FFB300", "text":"#FFE0B2", "bg":"#F9A825", "tile":"lightgrey"}
        self.yellow_ = {"button":"#FFEB3B", "button_border":"#BCAAA4", "hover":"#FFF59D", "text":"white", "bg":"#FFF9C4", "tile":"lightgrey"}
        self.green_ = {"button":"#1B5E20", "button_border":"#BCAAA4", "hover":"#81C784", "text":"#E8F5E9", "bg":"#A5D6A7", "tile":"lightgrey"}
        self.blue_ = {"button":"#00ACC1", "button_border":"#BCAAA4", "hover":"#80DEEA", "text":"#E0F7FA", "bg":"#B2EBF2", "tile":"lightgrey"}
        self.indigo_ = {"button":"#311B92", "button_border":"#BCAAA4", "hover":"#D1C4E9", "text":"#EDE7F6", "bg":"#B39DDB", "tile":"lightgrey"}
        self.violet_ = {"button":"#6A1B9A", "button_border":"#BCAAA4", "hover":"#BA68C8", "text":"#F3E5F5", "bg":"#CE93D8", "tile":"lightgrey"}
        self.pink_ = {"button":"#E91E63", "button_border":"#BCAAA4", "hover":"#F06292", "text":"#FCE4EC", "bg":"#F8BBD0", "tile":"lightgrey"}
        self.dark_ = {"button":"#616161", "button_border":"#BCAAA4", "hover":"#BDBDBD", "text":"#EEEEEE", "bg":"#000000", "tile":"lightgrey"}
        self.light_ = {"button":"#E0E0E0", "button_border":"#BCAAA4", "hover":"#EEEEEE", "text":"#000000", "bg":"#FFFFFF", "tile":"lightgrey"}
        
        self.themes = {"red":self.red_, "orange":self.orange_, "yellow":self.yellow_, "green":self.green_, "blue":self.blue_, "indigo":self.indigo_, "violet":self.violet_, "pink":self.pink_, "grey":self.dark_, "white":self.light_}
        self.NAMES = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet', 'Pink', 'Dark Mode', 'Light Mode']
        self.COLORS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "pink", "grey", "white"]
        self.BUTTONS = [self.red, self.orange, self.yellow, self.green, self.blue, self.indigo, self.violet, self.pink, self.dark, self.light]
        self.setup_selection(self.BUTTONS, self.COLORS, self.NAMES)


    def setup_selection(self, buttons:list = [], colors:list = [], names:list = []):

        for i in range(len(buttons)):

            buttons[i] = customtkinter.CTkButton(self, text=names[i], font=("Trebuchet MS", 35), text_color=self.theme["text"], bg_color="transparent", fg_color=self.theme["button"], hover_color=self.theme["hover"], border_width=5, border_spacing=5, border_color="lightgrey",
                                                        anchor="center", command=lambda dest=colors[i]: self.select(dest))
            if (i < 2):
                if (i % 2 == 0):
                    buttons[i].grid(column=1, columnspan=2, row=i+3, sticky="news")
                else:
                    buttons[i].grid(column=4, columnspan=2, row=i+2, sticky="news")
            else:
                if ((i) % 2 == 0):
                    buttons[i].grid(column=1, columnspan=2, row=i+3, sticky="news")
                else:
                    buttons[i].grid(column=4, columnspan=2, row=i+2, sticky="news")

    def create_labels(self):

        self.splash = customtkinter.CTkLabel(self, text_color=self.theme["text"], bg_color=self.theme["bg"], anchor='center', text="Select Theme", font=("Yu Mincho Demibold", 65))
        self.splash.grid(column=2, columnspan=3, row=0, rowspan=3, sticky="news")

        self.red = "lots of red"
        self.orange = "lots of orange"
        self.yellow = "lots of yellow"
        self.green = "lots of green"
        self.blue = "lots of blue"
        self.indigo = "lots of indigo"
        self.violet = "lots of violet"
        self.pink = "lots of pink"
        self.dark = "darkmode, lots of grey"
        self.light = "lightmode, lots of white"

        self.back = customtkinter.CTkButton(self, text_color=self.theme["text"], bg_color="transparent", fg_color=self.theme["button"], text="Return to C.A.K.E.", font=("Trebuchet MS", 50), border_spacing=5, border_width=5, border_color="lightgrey", hover_color=self.theme["hover"], anchor="center", command=self.destroy)
        self.back.grid(column=2, columnspan=3, row=16, rowspan=3, sticky="news")

    def select(self, name):
        global Theme
        self.theme = self.themes[name]
        Theme = self.theme
        self.master.frame.bg.configure(bg_color=self.theme["bg"], text_color=self.theme["text"])
        self.master.frame.splash.configure(text_color=self.theme["text"], bg_color=self.theme["bg"], fg_color=self.theme["bg"])
        self.master.frame.diagram.configure(bg_color=self.theme["bg"])
        self.master.frame.grey.configure(bg_color=self.theme["bg"], fg_color=self.theme["tile"])
        self.master.frame.add_slice.configure(text_color=self.theme["text"], hover_color=self.theme["hover"], fg_color=self.theme["button"], bg_color=self.theme["tile"])
        self.master.frame.remove_slice.configure(text_color=self.theme["text"], hover_color=self.theme["hover"], fg_color=self.theme["button"], bg_color=self.theme["tile"])
        self.master.frame.slice_num.configure(text_color=self.theme["text"], bg_color=self.theme["bg"])
        self.master.frame.tile.configure(bg_color=self.theme["bg"], fg_color=self.theme["tile"])
        self.master.frame.themes.configure(hover_color=self.theme["hover"], fg_color=self.theme["button"], text_color=self.theme["text"], bg_color=self.theme["bg"])
        self.master.frame.options.configure(hover_color=self.theme["hover"], text_color=self.theme["text"], fg_color=self.theme["button"], bg_color=self.theme["bg"])

        self.setup_selection(self.BUTTONS, self.COLORS, self.NAMES)
        self.destroy()
        self.master.theme_select()
     
customtkinter.set_appearance_mode("system")

########### RUN THE MAIN PROGRAM ################

app = App()
app.mainloop()

while(runnin):
    try: 
        pass
    
    except KeyboardInterrupt:
        runnin = False
        in_opr = False
        estop()
