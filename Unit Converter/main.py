from tkinter import *
from tkinter import ttk

#colors
cor01 = '#3b3b3b'     # Black
cor02 = '#ffffff'     # White

window = Tk()
window.title('Unit Coverter')
window.geometry('650x260')
window.configure(bg = cor01)

# --------------------- Frames for Window --------------
frame_up = Frame(window, width = 450, height = 50, bg = cor02, pady = 0, padx = 3, relief = 'flat')
frame_up.place(x = 2, y = 2)

frame_left = Frame(window, width = 450, height = 220, bg = cor02, pady = 0, padx = 3, relief = 'flat')
frame_left.place(x = 2, y = 54)

frame_right = Frame(window, width = 198, height = 260, bg = cor02, pady = 0, padx = 3, relief = 'flat')
frame_right.place(x = 454, y = 2)

# --------------------- Styles for Window --------------
style = ttk.Style(window)
style.theme_use("clam")



window.mainloop()
