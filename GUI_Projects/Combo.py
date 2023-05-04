from tkinter import *
from tkinter.ttk import *

def print_text():
    print(hour_combo.get())


window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

hour_combo = Combobox(window)
hour_combo['values'] = (0, 1, 2, 3, 4, 5)
hour_combo.current(0)  # set the selected item
hour_combo.grid(column=0, row=0)

btn = Button(window, text="Print", command=print_text)
btn.grid(column=1, row=0)

window.mainloop()
