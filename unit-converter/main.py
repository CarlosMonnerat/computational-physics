from tkinter import *
from tkinter import ttk

# Pillow Import
from PIL import ImageTk, Image

#colors
cor01 = '#3b3b3b'     # Black
cor02 = '#ffffff'     # White
cor03 = '#48b3e0'     # Blue

window = Tk()
window.title('Meson Pi Software')
window.geometry('650x260')
window.configure(bg = cor01)

# --------------------- Frames for Window --------------
frame_up = Frame(window, width=450, height=50, bg=cor02, pady=0, padx=3, relief='flat')
frame_up.place(x=2, y=2)

frame_left = Frame(window, width=450, height=220, bg=cor02, pady=0, padx=3, relief='flat')
frame_left.place(x=2, y=54)

frame_right = Frame(window, width= 198, height=260, bg=cor02, pady=0, padx=3, relief='flat')
frame_right.place(x=454, y=2)

# --------------------- Styles for Window --------------
style = ttk.Style(window)
style.theme_use("clam")

# --------------------- Labels for Frame_up --------------
l_app_name = Label(frame_up, text='Measurement Units Calculator', height=1, padx=0, relief='flat',
                    anchor='center', font=('Ivy 15 bold'), bg=cor02, fg=cor03)
l_app_name.place(x=50, y=10)

# --------------------- Settings Frame_left --------------
# Weigth Button
img_0 = Image.open('icons/weight.png')
img_0 = img_0.resize((50,50))
img_0 = ImageTk.PhotoImage(img_0)
btn_0 = Button(frame_left, text='Weight', image=img_0, compound=LEFT, width=130, height=50, relief='flat',
               overrelief='solid', anchor='nw', font=('Ivy 10 bold'), bg=cor03, fg=cor02)
btn_0.grid(row=0, column=0, sticky=NSEW, pady=5, padx=5)

# Time Button
img_1 = Image.open('icons/time.png')
img_1 = img_1.resize((50,50))
img_1 = ImageTk.PhotoImage(img_1)
btn_1 = Button(frame_left, text='Time', image=img_1, compound=LEFT, width=130, height=50, relief='flat',
               overrelief='solid', anchor='nw', font=('Ivy 10 bold'), bg=cor03, fg=cor02)
btn_1.grid(row=0, column=1, sticky=NSEW, pady=5, padx=5)

# Length Button
img_2 = Image.open('icons/length.png')
img_2 = img_2.resize((50,50))
img_2 = ImageTk.PhotoImage(img_2)
btn_2 = Button(frame_left, text='Length', image=img_2, compound=LEFT, width=130, height=50, relief='flat',
               overrelief='solid', anchor='nw', font=('Ivy 10 bold'), bg=cor03, fg=cor02)
btn_2.grid(row=0, column=2, sticky=NSEW, pady=5, padx=5)

# Square Button
img_3 = Image.open('icons/square.png')
img_3 = img_3.resize((50,50))
img_3 = ImageTk.PhotoImage(img_3)
btn_3 = Button(frame_left, text='Square', image=img_3, compound=LEFT, width=130, height=50, relief='flat',
               overrelief='solid', anchor='nw', font=('Ivy 10 bold'), bg=cor03, fg=cor02)
btn_3.grid(row=1, column=0, sticky=NSEW, pady=5, padx=5)



window.mainloop()
