
from PIL import Image 
import customtkinter
import os
  
# img = Image.open(os.path.join("Images", "Rectangle 1.png"))
# rgba = img.convert("RGBA") 
# datas = rgba.getdata() 
  
# newData = [] 
# for item in datas: 
#     if item[0] == 0 and item[1] == 0 and item[2] == 0:  # finding black colour by its RGB value 
#         # storing a transparent value when we find a black colour 
#         newData.append((255, 255, 255, 0)) 
#     else: 
#         newData.append(item)  # other colours remain unchanged 
  
# rgba.putdata(newData) 
# rgba.save("transparent_image.png", "PNG") 

image = Image.open("transparent_image.png")
image_i = customtkinter.CTkImage(image, size=(500,500))

win = customtkinter.CTk(fg_color="grey")

pic = customtkinter.CTkLabel(win, text='C.A.K.E', image=image_i, text_color="red")
pic.grid(column=0, row=0)

text = customtkinter.CTkLabel(win, text="weirdo", text_color="red", bg_color="transparent", fg_color="transparent")
text.grid(column=0, row=0)



win.mainloop()