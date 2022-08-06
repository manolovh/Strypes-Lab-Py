from PIL import Image, ImageTk, ImageFilter
import tkinter as tk

image_1 = Image.open('pyhton.jfif')
image_1 = image_1.resize((460, 460))
image_2 = Image.open('pyhton-fancy.png')
image_2 = image_2.resize((460, 460))

current_img = image_2

root = tk.Tk()
root.title('Image Viewer')
root.geometry('700x500')

def original():
    global current_image
    current_image = current_img
    displayed = ImageTk.PhotoImage(current_image)
    to_display.image = displayed
    to_display.config(image=displayed)

def blur():
    global current_image
    current_image = current_img.filter(ImageFilter.BLUR)
    displayed = ImageTk.PhotoImage(current_image)
    to_display.image = displayed
    to_display.config(image=displayed)

def contour():
    global current_image
    current_image = current_img.filter(ImageFilter.CONTOUR)
    displayed = ImageTk.PhotoImage(current_image)
    to_display.image = displayed
    to_display.config(image=displayed)

def edge_enhance():
    global current_image
    current_image = current_img.filter(ImageFilter.EDGE_ENHANCE)
    displayed = ImageTk.PhotoImage(current_image)
    to_display.image = displayed
    to_display.config(image=displayed)

def emboss():
    global current_image
    current_image = current_img.filter(ImageFilter.EMBOSS)
    displayed = ImageTk.PhotoImage(current_image)
    to_display.image = displayed
    to_display.config(image=displayed)

def rotate_image():
    global current_image
    current_image = current_image.transpose(Image.ROTATE_90)
    displayed = ImageTk.PhotoImage(current_image)
    to_display.image = displayed
    to_display.config(image=displayed)


mainframe = tk.Frame(root)
mainframe.pack(side='top')

original_button = tk.Button(mainframe, text="ORIGIANAL", command=original, width=15)
original_button.pack(side='left')

blur_button = tk.Button(mainframe, text="BLUR", command=blur, width=15)
blur_button.pack(side='left')

contour_button = tk.Button(mainframe, text="CONTOUR", command=contour, width=15)
contour_button.pack(side='left')

edge_enhance_button = tk.Button(mainframe, text="EDGE ENHANCE", command=edge_enhance, width=15)
edge_enhance_button.pack(side='left')

emboss_button = tk.Button(mainframe, text="EMBOSS", command=emboss, width=15)
emboss_button.pack(side='left')

rotate_button = tk.Button(mainframe, text='ROTATE IMAGE', command=rotate_image, width=15)
rotate_button.pack(side='left')

to_display = tk.Label(root, image=ImageTk.PhotoImage(current_img))
to_display.image = ImageTk.PhotoImage(current_img)
to_display.pack(side="bottom")

pic_info = tk.Label(root, text=f'HEIGHT: {current_img.height} PX\n WIDTH: {current_img.width} PX\n'
                               f' MODE: {current_img.mode}')
pic_info.place(x=600, y=200)

root.mainloop()
