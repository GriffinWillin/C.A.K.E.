####################################################################################################
# author: Joseph Henson
# date: 05/08/2024
# description: A set of menus for a all new automatic kitchen aid, the C.A.K.E.
############################################# Imports ##############################################

import customtkinter
import os
from PIL import Image, ImageTk
from time import sleep

music = True
Theme = {"bg":"#90CAF9", "text":"black", "button":"blue", "hover":"lightgrey", "tile":"grey", "guide":"white"}
DEPTH = 1
SPEED = 1
CUTS = 0

button_colors = []
text_colors = []
bg_colors = []
hover_colors = []


class MainMenu(customtkinter.CTkFrame):
    def __init__(self, master):
        global Theme
        super().__init__(master, border_width=2, height=600, width=1024)
        gifs = ["2_slices.gif", "4_slices.gif", "6_slices.gif", "8_slices.gif"]
        self.images = []
        self.theme = Theme


        for i in range(len(gifs)):
            image = Image.open(os.path.join("Images", f"{gifs[i]}"))
            image_i = customtkinter.CTkImage(image, size=(335,335))
            self.images.append(image_i)

        ################################################################################################################################
        self.bg = customtkinter.CTkLabel(master, text="", text_color=self.theme["text"], bg_color=self.theme["bg"])
        self.bg.grid(column=0, columnspan=26, row=0, rowspan=26, sticky="news")

        self.splash = customtkinter.CTkLabel(master, text="C.A.K.E", text_color="#E57373", bg_color="#90CAF9", anchor='center', font=("Yu Mincho Demibold", 80))
        self.splash.place(x=self.winfo_screenwidth()//3*1.65, y=300, anchor="center")
        # self.splash.grid(column=0, columnspan=6, row=0, rowspan=1)

        self.diagram = customtkinter.CTkLabel(master, image=self.images[0], text="", padx=0, anchor='center', bg_color="transparent", fg_color="transparent")
        self.diagram.grid(column=0, columnspan=5, row=1, rowspan=4, padx=0, sticky="news")
        
        self.grey = customtkinter.CTkLabel(master, text="", font=("Trebuchet MS", 65), anchor="center", text_color="white", fg_color="lightgrey") #width=self.winfo_screenwidth()/10 *3.07, height=self.winfo_screenheight()/9 * 1.75)
        self.grey.grid(column=0, columnspan=5, row=20, rowspan=11, pady=2, padx=10, sticky="news")
        #self.grey.place(x=self.winfo_screenwidth()//16 *3.7, y=self.winfo_screenheight()//30 *26.9, anchor="center")

        self.add_slice = customtkinter.CTkButton(master, text_color="black", fg_color="white", bg_color="lightgrey", hover_color="grey", text="+", corner_radius=48, font=("Trebuchet MS", 60), anchor="center", command=master.add_slices) #, width=self.winfo_screenwidth()/1 *0.01, height=self.winfo_screenheight()/10 * 0.87, command=master.add_slices)
        self.add_slice.grid(column=3, columnspan=2, row=22, rowspan=3, padx=10, sticky="news")
        #self.add_slice.place(x=self.winfo_screenwidth()//16 *5.3, y=self.winfo_screenheight()//30 *28.19, anchor="center")
        
        self.remove_slice = customtkinter.CTkButton(master, text_color="black", fg_color="white", bg_color="lightgrey", hover_color="grey", text="-", corner_radius=48, font=("Trebuchet MS", 60), anchor="center", command=master.remove_slices) #, width=self.winfo_screenwidth()/10 *0.97, height=self.winfo_screenheight()/9 * 0.85, command=master.remove_slices)
        self.remove_slice.grid(column=0, columnspan=2, row=22, rowspan=3, padx=10, sticky="news")
        #self.remove_slice.place(x=self.winfo_screenwidth()//16 *2.1, y=self.winfo_screenheight()//30 *28.19, anchor="center")
        
        self.slice_num = customtkinter.CTkLabel(master, text="Number of Slices", bg_color=self.theme["bg"], font=("Trebuchet MS", 35), anchor="center")
        self.slice_num.grid(column=0, columnspan=5, row=9, padx=10, sticky="news")

        self.slice = customtkinter.CTkLabel(master, text="2", text_color=self.theme["text"], fg_color="black", font=("Trebuchet MS", 60), anchor="center")
        self.slice.grid(column=0, columnspan=5, row=20, padx=10, sticky="news")

        self.themes = customtkinter.CTkButton(master, text_color="white", fg_color=self.theme["button"], text="Theme Select", font=("Trebuchet MS", 30), anchor="center", command=master.theme_select)
        self.themes.grid(column=20, columnspan=2, row=0, rowspan=2, pady=(10), sticky="news")
        
        self.options = customtkinter.CTkButton(master, text_color="white", fg_color="#7986CB", text="Settings", font=("Trebuchet MS", 30), anchor="center", command=master.open_settings)
        self.options.grid(column=23, columnspan=2, row=0, rowspan=2, pady=(10), sticky="news")

        self.tile = customtkinter.CTkLabel(master, text="", anchor="center", text_color="white", fg_color="lightgrey", width=self.winfo_screenwidth()/4 *2.55, height=self.winfo_screenheight()/3 * 1.45, corner_radius=35)
        self.tile.place(x=self.winfo_screenwidth()//6 *4.34, y=self.winfo_screenheight()//30 *23.75, anchor="center")

        self.guide = customtkinter.CTkLabel(master, text="CONTROLS:", font=("Trebuchet MS", 36), anchor="center", text_color="black", fg_color="lightgrey", bg_color="transparent", corner_radius=0)
        self.guide.place(x=self.winfo_screenwidth()//6 *3.12, y=self.winfo_screenheight()//30 *17.9, anchor="center")

        self.start = customtkinter.CTkButton(master, text_color="white", fg_color="#66BB6A", bg_color="lightgrey", hover_color="green", text="START", font=("Trebuchet MS", 65), anchor="center", height=self.winfo_screenheight()/3, corner_radius=35, command=exit)
        # self.start.grid(column=9, columnspan=8, row=6, rowspan=15, sticky="ewsn")
        self.start.place(x=self.winfo_screenwidth()//6 *3.28, y=self.winfo_screenheight()//30 *24.44, anchor="center")

        self.leave = customtkinter.CTkButton(master, text_color="white", fg_color="#E57373", bg_color="lightgrey", hover_color="red", text="EXIT", font=("Trebuchet MS", 65), anchor="center", width=300, height=self.winfo_screenheight()/3, corner_radius=35, command=exit)
        # self.leave.grid(column=18, columnspan=7, row=6, rowspan=15, sticky="news")
        self.leave.place(x=self.winfo_screenwidth()//6 *5.10, y=self.winfo_screenheight()//30 *24.44, anchor="center")
    
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

    ####################################################################################################################################
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





    ####################################################################################################################################

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
        # self.frame.diagram.configure(image=self.DIAGRAMS[self.slices-2]) #need to fix the number for the images, or could just use fillers to make it easy
        self.frame.slice.configure(text=f"{self.slices}")
        self.frame.diagram.update()
        self.frame.slice.update()
        sleep(0.01)
    
    def game_start(self):
        start_cutting()

    def theme_select(self):
        pick = ThemeSelect(self)
        pick.attributes("-topmost", True)
        pick.mainloop()

    def open_settings(self):
        options = Settings(self)
        print("here")
        options.attributes("-topmost", True)
        options.mainloop()

class Settings(customtkinter.CTkToplevel):
    def __init__(self, master):
        global Theme
        super().__init__(fg_color=Theme["bg"])
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        App.build_grid(self, 8, 20)
        self.build_menu()
        self.master = master
        self.wm_attributes("-fullscreen", True)
        self.theme = Theme
        
        self.OPTIONS = {self.cut_depth:"CUT DEPTH", self.cut_speed:"CUT SPEED", self.info:"INFO"}
        self.setup_options(list(self.OPTIONS.keys()), list(self.OPTIONS.values()))
        
    def setup_options(self, buttons:list = [], names:list = []):

        for i in range(2, len(buttons)):
        
            print(self.OPTIONS[buttons[i]])
            buttons[i].configure(self, text=names[i], font=("Trebuchet MS", 30), text_color=self.theme["text"], bg_color=self.theme["bg"], fg_color=self.theme["button"], hover_color="lightgrey", border_width=5, border_spacing=5, border_color="lightgrey",
                                                        anchor="center")
        for i in range (len(buttons)):
            if (i < 2):
                if (i % 2 == 0):
                    buttons[i].grid(column=1, columnspan=3, row=i+3, rowspan=1, sticky="news")
                else:
                    buttons[i].grid(column=5, columnspan=3, row=i+2, rowspan=1, sticky="news")
            else:
                if ((i) % 2 == 0):
                    buttons[i].grid(column=1, columnspan=3, row=i+3, rowspan=1, sticky="news")
                else:
                    buttons[i].grid(column=5, columnspan=3, row=i+2, rowspan=1, sticky="news")

    def build_menu(self):
        global DEPTH
        global SPEED

        self.splash = customtkinter.CTkLabel(self, text="Settings", text_color=("white"), bg_color="#8560D1", anchor='center', fg_color="transparent", font=("Yu Mincho Demibold", 85))
        self.splash.grid(column=3, columnspan=3, row=0, sticky="news")

        self.cut_depth = customtkinter.CTkSlider(self, from_=.5, to=1, number_of_steps=2, command=self.depth)
        self.cut_depth.set(DEPTH)
        self.cut_speed = customtkinter.CTkSlider(self, from_=1, to=100, number_of_steps=25, command=self.speed)
        self.cut_speed.set(SPEED)

        self.info = customtkinter.CTkButton(self, command=self.list_info)
            
        self.back = customtkinter.CTkButton(self, text_color="white", bg_color="transparent", fg_color="#655482", hover_color="lightgrey", text="RETURN TO C.A.K.E.", font=("Trebuchet MS", 30), border_width=5, border_color="lightgrey", command=self.destroy)
        self.back.grid(column=3, columnspan=3, row=12, rowspan=2, sticky="news")

    def depth(self, n):
        global DEPTH
        # print(n)
        DEPTH = n
        print(DEPTH)

    def speed(self, n):
        global SPEED
        # print(n)
        SPEED = n
        print(SPEED)

    def list_info(self): # turn this into a help icon?
        list = BindKeys(self)
        self.attributes("-topmost", False)
        list.attributes("-topmost", True)
        list.mainloop()

    # def arena_select(self): # can turn this into a way to change themes
    #     global arena
        
    #     if (self.bg == 0):
    #         self.bg += 1
    #     else:
    #         self.bg -= 1

        # self.arena_toggle.configure(text=f"Current Arena: {self.ARENAS[self.bg]}")
        # arena = (os.path.join("Backgrounds", f"{self.ARENAS[self.bg]}.jpeg"))

class ThemeSelect(customtkinter.CTkToplevel): # turn this into a theme select
    def __init__(self, master):
        global Theme
        super().__init__(fg_color=Theme["bg"])
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        App.build_grid(self, 6, 20)
        # App.get_background(self, "brighttrain.jpeg")
        self.create_labels()
        self.master = master
        self.wm_attributes("-fullscreen", True)
        self.theme = Theme
        Theme = self.theme

        self.NAMES = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet', 'Pink', 'Dark Mode', 'Light Mode']
        self.COLORS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "pink", "grey", "white", "teal", "turquoise"]
        self.BUTTONS = [self.red, self.orange, self.yellow, self.green, self.blue, self.indigo, self.violet, self.pink, self.dark, self.light]
        self.setup_selection(self.BUTTONS, self.COLORS, self.NAMES)


    def setup_selection(self, buttons:list = [], colors:list = [], names:list = []):

        for i in range(len(buttons)):
            # image = Image.open(os.path.join("Images", f"{images[i]}.png"))
            # image_i = customtkinter.CTkImage(image, size=(100,100))

            buttons[i] = customtkinter.CTkButton(self, text=names[i], font=("Trebuchet MS", 35), text_color=self.theme["text"], bg_color="transparent", fg_color=self.theme["button"], hover_color="lightgrey", border_width=5, border_spacing=5, border_color="lightgrey",
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

        # CONFIGURE FOR LOOP TO SPLIT THE BUTTONS IN HALF WHILE MAKING THE GRID
        # TURN THIS INTO A FUNCTION AND ALLOW FOR THE PARAMETERS TO BE THESE GLOBAL CONSTANTS SO YOU CAN SAVE SPACE EVERYWHERE

    def create_labels(self):

        self.splash = customtkinter.CTkLabel(self, text_color=("white"), bg_color="transparent", anchor='center', fg_color="transparent", text="Select Theme", font=("Yu Mincho Demibold", 65))
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

        self.back = customtkinter.CTkButton(self, text_color="black", bg_color="transparent", fg_color="turquoise", text="Return to C.A.K.E.", font=("Trebuchet MS", 50), border_spacing=5, border_width=5, border_color="lightgrey", hover_color="lightgrey", anchor="center", command=self.destroy)
        self.back.grid(column=2, columnspan=3, row=16, rowspan=3, sticky="news")

    def select(self, name):
        changes = list(self.theme.keys())
        for option in changes:
            self.theme[option] = name
            self.master.frame.bg.configure(bg_color=name)
            self.master.frame.splash.configure(text_color=name, bg_color=name)
            self.master.frame.diagram.configure(text_color=name)
            self.master.frame.add_slice.configure(text_color=name)
            self.master.frame.remove_slice.configure(fg_color=name)
            self.master.frame.slice_num.configure(fg_color=name)
            self.master.frame.themes.configure(fg_color=name)
            self.master.frame.options.configure(fg_color=name)
        self.setup_selection(self.BUTTONS, self.COLORS, self.NAMES)
        self.destroy()
        self.master.theme_select()
        


class BindKeys(customtkinter.CTkToplevel):#
    def __init__(self, master):
        global SPEED
        global DEPTH
        global Theme
        super().__init__(fg_color=Theme["bg"])
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        App.build_grid(self, 6, 20)
        self.create_labels()
        self.master = master
        self.wm_attributes("-fullscreen", True)
        self.theme = Theme
        
        MEASUREMENTS = ["DEPTH", "SPEED"]
        LABLES = [self.depth, self.speed]
        NUMBERS = [DEPTH, SPEED]
        # self.DICT = {ACTIONS[i]:DEFAULT[i] for i in range(len(ACTIONS))}
        self.setup_selection(LABLES, MEASUREMENTS, NUMBERS)


    def setup_selection(self, labels, actions, keys):

        for i in range(len(labels)):

            labels[i] = customtkinter.CTkLabel(self, text=f"{actions[i]}: {keys[i]}", font=("Trebuchet MS", 40), text_color=self.theme["text"], bg_color=self.theme["bg"], fg_color=self.theme["button"],
                                                        anchor="center")
            if (i < 2):
                if (i % 2 == 0):
                    labels[i].grid(column=2, columnspan=2, row=i+3, sticky="news")
                else:
                    labels[i].grid(column=4, columnspan=2, row=i+2, sticky="news")
            else:
                if ((i) % 2 == 0):
                    labels[i].grid(column=1, columnspan=2, row=i+3, sticky="news")
                else:
                    labels[i].grid(column=4, columnspan=2, row=i+2, sticky="news")

    def create_labels(self):

        self.splash = customtkinter.CTkLabel(self, text_color=("white"), bg_color="#8560D1", anchor='center', fg_color="transparent", text="KEY BINDS", font=("Yu Mincho Demibold", 85))
        self.splash.grid(column=2, columnspan=3, row=0, rowspan=3, sticky="news")

        self.depth = 'distance'
        self.speed = "speed"
        self.down = "down"
        self.right = "right"
        self.shoot = "shoot"
        self.leave = "leave"

        self.back = customtkinter.CTkButton(self, text_color="white", bg_color="transparent", fg_color="#655482", text="RETURN TO GAME", font=("Trebuchet MS", 40), border_spacing=5, border_width=5, border_color="lightgrey", hover_color="lightgrey", anchor="center", command=self.destroy)
        self.back.grid(column=2, columnspan=3, row=12, rowspan=1, sticky="news")

    ## don't look please ##
    # def bind_k(self, pressed):
    #     scrapped until further notice
    #     command=lambda action=actions[i]: self.bind_k(action, pygame.key.get_pressed())


customtkinter.set_appearance_mode("system")
# Call the menu and keep it running once the file is ran
app = App()
app.mainloop()