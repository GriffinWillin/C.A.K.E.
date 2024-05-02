####################################################################################################
# author: Joseph Henson
# date: 04/17/2024
# description: A set of menus for a simple game similar to space invaders
############################################# Imports ##############################################

import customtkinter
import pygame
import os
from PIL import Image, ImageTk
from time import sleep

pygame.mixer.init()
music = True

class MainMenu(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, bg_color=("#90CAF9"), border_width=2, fg_color=("transparent"), height=600, width=1024)
        # App.get_background(master, 'brighttrain.jpeg')
        pngs = ["C.A.K.E_", "Ellipse 1", "R", "slices", "Start", "Stop"]
        images = []


        image = Image.open(os.path.join("Images", f"{pngs[0]}.png"))
        image_i = customtkinter.CTkImage(image, size=(150,150))
        images.append(image_i)

        image = Image.open(os.path.join("Images", f"{pngs[1]}.png"))
        image_i = customtkinter.CTkImage(image, size=(450,450))
        images.append(image_i)

        image = Image.open(os.path.join("Images", f"{pngs[2]}.png"))
        image_i = customtkinter.CTkImage(image, size=(150,150))
        images.append(image_i)

        image = Image.open(os.path.join("Images", f"{pngs[3]}.png"))
        image_i = customtkinter.CTkImage(image, size=(450,90))
        images.append(image_i)

        image = Image.open(os.path.join("Images", f"{pngs[4]}.png"))
        image_i = customtkinter.CTkImage(image, size=(350,350))
        images.append(image_i)

        image = Image.open(os.path.join("Images", f"{pngs[5]}.png"))
        image_i = customtkinter.CTkImage(image, size=(350,350))
        images.append(image_i)

        ################################################################################################################################

        self.splash = customtkinter.CTkLabel(master, text="C.A.K.E", text_color="#EE5A57", bg_color="#90CAF9", anchor='center', fg_color="transparent", font=("Yu Mincho Demibold", 190))
        self.splash.place(x=self.winfo_screenwidth()//2+200, y=self.winfo_screenheight()//2, anchor="center")
        # self.splash.grid(column=0, columnspan=6, row=0, rowspan=1)

        self.diagram = customtkinter.CTkLabel(master, image=images[1], text="", padx=15, anchor='center')
        self.diagram.grid(column=1, columnspan=7, row=3, rowspan=4)

        self.add_slice = customtkinter.CTkButton(master, text_color="white", fg_color="#655482", bg_color="transparent", text="+", font=("Trebuchet MS", 30), anchor="center", command=exit)
        self.add_slice.grid(column=1, columnspan=3, row=15, rowspan=6, sticky="news")
        
        self.remove_slice = customtkinter.CTkButton(master, text_color="white", fg_color="#655482", bg_color="transparent", text="-", font=("Trebuchet MS", 30), anchor="center", command=exit)
        self.remove_slice.grid(column=5, columnspan=3, row=15, rowspan=6, sticky="news")
        
        self.slice_num = customtkinter.CTkLabel(master, image=images[3], text="", anchor="center")
        self.slice_num.grid(column=1, columnspan=7, row=9, sticky="news")

        self.slice = customtkinter.CTkLabel(master, text=f"1", font=("Trebuchet MS", 85), anchor="center", text_color="red")
        self.slice.grid(column=2, columnspan=5, row=13, sticky="news")

        self.themes = customtkinter.CTkButton(master, text_color="white", fg_color="#655482", text="select a theme", font=("Trebuchet MS", 30), anchor="center", command=exit)
        self.themes.grid(column=20, columnspan=2, row=0, rowspan=3, pady=(10), sticky="news")
        
        self.options = customtkinter.CTkButton(master, text_color="white", fg_color="#655482", text="info", font=("Trebuchet MS", 30), anchor="center", command=exit)
        self.options.grid(column=23, columnspan=2, row=0, rowspan=3, pady=(10), sticky="news")

        self.start = customtkinter.CTkButton(master, text_color="white", fg_color="green", text="START", font=("Trebuchet MS", 30), anchor="center", command=exit)
        self.start.grid(column=10, columnspan=10, row=8, rowspan=13, sticky="news")

        self.leave = customtkinter.CTkButton(master, text_color="white", fg_color="red", text="EXIT", font=("Trebuchet MS", 30), anchor="center", command=exit)
        self.leave.grid(column=20, columnspan=5, row=8, rowspan=13, sticky="news")
    
class App(customtkinter.CTk):
    '''
    A class that serves as the basis for all menu operations
    '''
    def __init__(self):
        global status
        super().__init__(fg_color="#90CAF9")
        # self.bg_music = pygame.mixer.Sound(os.path.join("Music", "guitar chill.mp3"))
        # self.bg_music.set_volume(0.4)
        # self.bg_music.play(-1)
        self.wm_attributes("-fullscreen", True)
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        self.build_grid(25, 25)
        self.frame = MainMenu(master=self)
        self.slices = 0
        self.DIAGRAMS = [2, 4, 6, 8, 10] # list that changes the image to the amount of slices

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
        n = 2
        self.frame.slice_num.configure()
    
    def game_start(self):
        pygame.mixer.stop()
        if (music):
            game_music = pygame.mixer.Sound(os.path.join("Music", "gameloopfixed.mp3"))
            game_music.set_volume(0.4)
            game_music.play(-1, fade_ms=1000)
        # start_cutting()

    def theme_select(self):
        pick = CharacterSelect(self)
        pick.attributes("-topmost", True)
        pick.mainloop()

    def open_settings(self):
        options = Settings(self)
        options.attributes("-topmost", True)
        options.mainloop()

class Settings(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(fg_color="#8560D1")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        App.build_grid(self, 8, 20)
        # App.get_background(self, "brighttrain.jpeg")
        self.build_menu()
        self.master = master
        self.wm_attributes("-fullscreen", self.master.status)
        
        if (music):
            mute = "MUTE"
        else:
            mute = "UNMUTE"
        
        self.OPTIONS = {self.cut_depth:"CUT DEPTH", self.cut_speed:"CUT SPEED", self.mute:f"{mute}", self.info:"INFO"}
        self.setup_options(list(self.OPTIONS.keys()), list(self.OPTIONS.values()))
        
    def setup_options(self, buttons:list = [], names:list = []):

        for i in range(len(buttons)):
            buttons[i].configure(self, text=names[i], font=("Trebuchet MS", 30), text_color='white', bg_color="transparent", fg_color="#655482", hover_color="lightgrey", border_width=5, border_spacing=5, border_color="lightgrey",
                                                        anchor="center")
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

        self.splash = customtkinter.CTkLabel(self, text="OPTIONS", text_color=("white"), bg_color="#8560D1", anchor='center', fg_color="transparent", font=("Yu Mincho Demibold", 85))
        self.splash.grid(column=3, columnspan=3, row=0, sticky="news")

        self.cut_depth = customtkinter.CTkButton(self, command=self.depth)
        self.cut_speed = customtkinter.CTkButton(self, command=self.speed)
        # self.other = customtkinter.CTkButton(self, command=self.credit)
        self.info = customtkinter.CTkButton(self, command=self.list_info)
        if (music):
            self.mute = customtkinter.CTkButton(self, command=self.sound_off)
        else:
            self.mute = customtkinter.CTkButton(self, command=self.sound_on)
        # self.arena_toggle = customtkinter.CTkButton(self, command=self.arena_select)
            
        self.back = customtkinter.CTkButton(self, text_color="white", bg_color="transparent", fg_color="#655482", hover_color="lightgrey", text="RETURN TO GAME", font=("Trebuchet MS", 30), border_width=5, border_color="lightgrey", command=self.destroy)
        self.back.grid(column=3, columnspan=3, row=12, rowspan=2, sticky="news")

    # def fs(self):
    #     if (self.master.status == False):
    #         self.master.status = True
    #     else:
    #         self.master.status = False
    #     self.wm_attributes("-fullscreen", self.master.status)
    #     self.master.wm_attributes("-fullscreen", self.master.status)
    def depth(self):
        pass
    def speed(self):
        pass

    def remove_slices(self):
        pass

    def add_slices(self):
        pass

    def list_info(self): # turn this into a help icon?
        list = BindKeys(self)
        self.attributes("-topmost", False)
        list.attributes("-topmost", True)
        list.mainloop()

    def sound_off(self):
        global music
        if(music):
            pygame.mixer.pause()
            self.mute.configure(text = "UNMUTE", command=self.sound_on)
            self.mute.update()
        music = False

    def sound_on(self):
        global music
        pygame.mixer.unpause()
        self.mute.configure(text = "MUTE", command=self.sound_off)
        self.mute.update()
        music = True

    # def arena_select(self): # can turn this into a way to change themes
    #     global arena
        
    #     if (self.bg == 0):
    #         self.bg += 1
    #     else:
    #         self.bg -= 1

        self.arena_toggle.configure(text=f"Current Arena: {self.ARENAS[self.bg]}")
        arena = (os.path.join("Backgrounds", f"{self.ARENAS[self.bg]}.jpeg"))

class CharacterSelect(customtkinter.CTkToplevel): # turn this into a theme select
    def __init__(self, master):
        super().__init__(fg_color="#655482")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        App.build_grid(self, 6, 20)
        App.get_background(self, "brighttrain.jpeg")
        self.create_labels()
        self.master = master
        self.wm_attributes("-fullscreen", self.master.status)
        
        # TURN THIS INTO A DICTIONARY OR AT LEAST A LIST MAYBE USING A FOR LOOP 
        NAMES = ['Doug', 'Parker', 'Dan', 'Josh', 'Greg', 'Jay', 'Sean', 'Cameron', 'Tony', 'Pablo', 'Dominic']
        CHARACTERS = ["wizard", "spider", "cat4x", "frog4x", "gelatine4x", "ghost4x", "horseman4x", "raptor4x", "rockman4x", "skull4x", "spook4x"]
        BUTTONS = [self.wizard, self.spider, self.cat, self.frog, self.gelatine, self.ghost, self.horseman, self.raptor, self.rockman, self.skull, self.spook]
        # character_png = {NAMES[i]:(os.path.join("CHARACTERS", f"{CHARACTERS[i]}.png")) for i in range(len(CHARACTERS))}
        self.setup_selection(BUTTONS, CHARACTERS, NAMES)


    def setup_selection(self, buttons:list = [], images:list = [], names:list = []):

        for i in range(len(buttons)):
            image = Image.open(os.path.join("Images", f"{images[i]}.png"))
            image_i = customtkinter.CTkImage(image, size=(100,100))

            buttons[i] = customtkinter.CTkButton(self, image=image_i, text=names[i], font=("Trebuchet MS", 30), text_color='white', bg_color="transparent", fg_color="#655482", hover_color="lightgrey", border_width=5, border_spacing=5, border_color="lightgrey",
                                                        anchor="center", command=lambda dest=images[i]: self.select(dest))
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

        self.splash = customtkinter.CTkLabel(self, text_color=("white"), bg_color="#8560D1", anchor='center', fg_color="transparent", text="PICK A PLAYER", font=("Yu Mincho Demibold", 85))
        self.splash.grid(column=2, columnspan=3, row=0, rowspan=3, sticky="news")

        self.blue = 'a blue background' # etc
        self.spider = "spider"
        self.cat = "cat"
        self.frog = "frog"
        self.gelatine = "gelatine"
        self.ghost = "ghost"
        self.horseman = "horseman"
        self.raptor = "raptor"
        self.rockman = "rockman"
        self.skull = "skull"
        self.spook = "spook"

        self.back = customtkinter.CTkButton(self, text_color="white", bg_color="transparent", fg_color="#655482", text="RETURN TO GAME", font=("Trebuchet MS", 30), border_spacing=5, border_width=5, border_color="lightgrey", hover_color="lightgrey", anchor="center", command=self.destroy)
        self.back.grid(column=2, columnspan=3, row=16, rowspan=4, sticky="news")

    def select(self, name):
        global character
        character = (os.path.join("Images", f"{name}.png"))

class BindKeys(customtkinter.CTkToplevel):#
    def __init__(self, master):
        super().__init__(fg_color="#655482")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        App.build_grid(self, 6, 20)
        App.get_background(self, "brighttrain.jpeg")
        self.create_labels()
        self.master = master
        self.wm_attributes("-fullscreen", self.master.master.status)
        
        ACTIONS = ["MOVE UP", "MOVE LEFT", "MOVE DOWN", "MOVE RIGHT", "SHOOT", "EXIT GAME"]
        BUTTONS = [self.up, self.left, self.down, self.right, self.shoot, self.leave]
        DEFAULT = ["W", "A", "S", "D", "SPACE", "ESC"]
        # self.DICT = {ACTIONS[i]:DEFAULT[i] for i in range(len(ACTIONS))}
        self.setup_selection(BUTTONS, ACTIONS, DEFAULT)


    def setup_selection(self, labels, actions, keys):

        for i in range(len(labels)):

            labels[i] = customtkinter.CTkLabel(self, text=f"{actions[i]}: {keys[i]}", font=("Trebuchet MS", 40), text_color='white', bg_color="transparent", fg_color="#655482",
                                                        anchor="center")
            if (i < 2):
                if (i % 2 == 0):
                    labels[i].grid(column=1, columnspan=2, row=i+3, sticky="news")
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

        self.up = 'up'
        self.left = "left"
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