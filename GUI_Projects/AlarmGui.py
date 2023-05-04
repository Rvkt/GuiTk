import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Label

root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Alarm Clock')

# show the label here

# label = Label(root, text='This is a label', font=("Helvetica", 20))
# label.pack(ipadx=10, ipady=10)
#
#
# # label with a specific font
# label2 = ttk.Label(
#     root,
#     text='A Label with the Helvetica font',
#     font=("Helvetica", 14))
# label2.pack(ipadx=10, ipady=10)

btn = tk.Button(root, text="Click Me")

btn.grid(column=1, row=0)

root.mainloop()
