from tkinter import *
from tkinter import ttk

# Pillow Import
from PIL import ImageTk, Image

# Colors
cor01 = '#3b3b3b'     # Black
cor02 = '#ffffff'     # White
cor03 = '#48b3e0'     # Blue

window = Tk()
window.title('Meson Pi Software')
window.geometry('650x260')
window.configure(bg=cor01)

# ----------------------------------- Frames for Window -----------------------------
frame_up = Frame(window, width=450, height=50, bg=cor02, pady=0, padx=3, relief='flat')
frame_up.place(x=2, y=2)

frame_left = Frame(window, width=450, height=220, bg=cor02, pady=0, padx=3, relief='flat')
frame_left.place(x=2, y=54)

frame_right = Frame(window, width=198, height=260, bg=cor02, pady=0, padx=3, relief='flat')
frame_right.place(x=454, y=2)

# ------------------------------------- Styles for Window ----------------------------
style = ttk.Style(window)
style.theme_use("clam")

# ------------------------------------ Labels for Frame_up -----------------------------
l_app_name = Label(frame_up, text='Measurement Units Calculator', height=1, padx=0, relief='flat', anchor='center',
                   font='Ivy 15 bold', bg=cor02, fg=cor03)
l_app_name.place(x=50, y=10)

# ---------------------------- Configuring the functionality -------------------------------------
units = {'weight': [{'kg': 1000}, {'hg': 100}, {'dag': 10}, {'g': 1}, {'dg': 0.1}, {'cg': 0.01}, {'mg': 0.001}],
         'time': [{'year': 12}, {'month': 30}, {'day': 24}, {'hour': 60}, {'min': 60}, {'s': 1}, {'ms': 0.001}],
         'length': [{'km': 1000}, {'hm': 100}, {'dam': 10}, {'m': 1}, {'dm': 0.1}, {'cm': 0.01}, {'mm': 0.001}],
         'area': [{'km²': 0.000001}, {'hectare': 0.0001}, {'m²': 1}, {'cm²': 10000}, {'mm²': 1000000}],
         'volume': [{'l': 1000}, {'m³': 1}, {'ml': 1000000}],
         'speed': [{'km/h': 3.6}, {'m/s': 1}, {'mm/s': 0.001}],
         'temperature': [{'ºRa': 491.67}, {'K': 273.15}, {'ºF': 32}, {'ºC': 0}],
         'energy': [{'kJ': 4.184}, {'J': 4184}, {'kcal': 1}, {'cal': 1000}, {'watt hour': 1.16222}],
         'pressure': [{'Bar': 0.00001}, {'Pa': 1}, {'atm': 0.00000986923}]
         }

# ------------------------------------ Configuring Frame_left -------------------------------------
# Weight Button
img_0 = Image.open('icons/weight.png')
img_0 = img_0.resize((50, 50))
img_0 = ImageTk.PhotoImage(img_0)
btn_0 = Button(frame_left, text='Weight', image=img_0, compound=LEFT, width=130, height=50, relief='flat',
               overrelief='solid', anchor='nw', font='Ivy 10 bold', bg=cor03, fg=cor02)
btn_0.grid(row=0, column=0, sticky=NSEW, pady=5, padx=5)

# Time Button
img_1 = Image.open('icons/time.png')
img_1 = img_1.resize((50, 50))
img_1 = ImageTk.PhotoImage(img_1)
btn_1 = Button(frame_left, text='Time', image=img_1, compound=LEFT, width=130, height=50, relief='flat',
               overrelief='solid', anchor='nw', font='Ivy 10 bold', bg=cor03, fg=cor02)
btn_1.grid(row=0, column=1, sticky=NSEW, pady=5, padx=5)

# Length Button
img_2 = Image.open('icons/length.png')
img_2 = img_2.resize((50, 50))
img_2 = ImageTk.PhotoImage(img_2)
btn_2 = Button(frame_left, text='Length', image=img_2, compound=LEFT, width=130, height=50, relief='flat',
               overrelief='solid', anchor='nw', font='Ivy 10 bold', bg=cor03, fg=cor02)
btn_2.grid(row=0, column=2, sticky=NSEW, pady=5, padx=5)

# Area Button
img_3 = Image.open('icons/square.png')
img_3 = img_3.resize((50, 50))
img_3 = ImageTk.PhotoImage(img_3)
btn_3 = Button(frame_left, text='Area', image=img_3, compound=LEFT, width=130, height=50, relief='flat',
               overrelief='solid', anchor='nw', font='Ivy 10 bold', bg=cor03, fg=cor02)
btn_3.grid(row=1, column=0, sticky=NSEW, pady=5, padx=5)

# Volume Button
img_4 = Image.open('icons/volume.png')
img_4 = img_4.resize((50, 50))
img_4 = ImageTk.PhotoImage(img_4)
btn_4 = Button(frame_left, text='Volume', image=img_4, compound=LEFT, width=130, height=50, relief='flat',
               overrelief='solid', anchor='nw', font='Ivy 10 bold', bg=cor03, fg=cor02)
btn_4.grid(row=1, column=1, sticky=NSEW, pady=5, padx=5)

# Speed Button
img_5 = Image.open('icons/speed.png')
img_5 = img_5.resize((50, 50))
img_5 = ImageTk.PhotoImage(img_5)
btn_5 = Button(frame_left, text='Speed', image=img_5, compound=LEFT, width=130, height=50, relief='flat',
               overrelief='solid', anchor='nw', font='Ivy 10 bold', bg=cor03, fg=cor02)
btn_5.grid(row=1, column=2, sticky=NSEW, pady=5, padx=5)

# Temperature Button
img_6 = Image.open('icons/temperature.png')
img_6 = img_6.resize((45, 50))
img_6 = ImageTk.PhotoImage(img_6)
btn_6 = Button(frame_left, text='Temperature', image=img_6, compound=LEFT, width=130, height=50, relief='flat',
               overrelief='solid', anchor='nw', font='Ivy 10 bold', bg=cor03, fg=cor02)
btn_6.grid(row=2, column=0, sticky=NSEW, pady=5, padx=5)

# Energy Button
img_7 = Image.open('icons/energy.png')
img_7 = img_7.resize((50, 50))
img_7 = ImageTk.PhotoImage(img_7)
btn_7 = Button(frame_left, text='Energy', image=img_7, compound=LEFT, width=130, height=50, relief='flat',
               overrelief='solid', anchor='nw', font='Ivy 10 bold', bg=cor03, fg=cor02)
btn_7.grid(row=2, column=1, sticky=NSEW, pady=5, padx=5)

# Pressure Button
img_8 = Image.open('icons/pressure.png')
img_8 = img_8.resize((50, 50))
img_8 = ImageTk.PhotoImage(img_8)
btn_8 = Button(frame_left, text='Pressure', image=img_8, compound=LEFT, width=130, height=50, relief='flat',
               overrelief='solid', anchor='nw', font='Ivy 10 bold', bg=cor03, fg=cor02)
btn_8.grid(row=2, column=2, sticky=NSEW, pady=5, padx=5)


# ------------------------------ Labels for Frame_right -----------------------------
l_unit_name = Label(frame_right, text='Unit', width=16, height=2, padx=0, relief='groove', anchor='center',
                    font='Ivy 15 bold', bg=cor02, fg=cor01)
l_unit_name.place(x=0, y=0)

# -------------------------------------------------------------------------------------------------------
l_from = Label(frame_right, text='from', height=1, padx=3, relief='groove', anchor='center',
               font='Ivy 10 bold', bg=cor02, fg=cor01)
l_from.place(x=5, y=70)
c_from = ttk.Combobox(frame_right, width=5, justify='center', font='Ivy 8 bold')
c_from.place(x=50, y=70)

# -------------------------------------------------------------------------------------------------------
l_to = Label(frame_right, text='to', height=1, padx=3, relief='groove', anchor='center',
             font='Ivy 10 bold', bg=cor02, fg=cor01)
l_to.place(x=108, y=70)
c_to = ttk.Combobox(frame_right, width=5, justify='center', font='Ivy 8 bold')
c_to.place(x=135, y=70)

# -------------------------------------------------------------------------------------------------------


# --------------------- Settings Frame_right --------------


window.mainloop()
