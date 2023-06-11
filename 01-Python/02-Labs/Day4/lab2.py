# tkinter-radio-ex.py

import tkinter as tk
from tkinter import messagebox

def change_lbl():
    global pin_config
    output = str()
    for c in pin_config:
       if c.get()=="input":
            output += "0"
       else:
            output += "1"
    
    # TODO: string should be reversed
    output = output[::-1]
    output = "0b" + output
    messagebox.showinfo(title="config", message = output)

root = tk.Tk()
root.geometry("300x300+400+400")

radio_values = {
    "output":"output",
    "input":"input"
}

pin_config =  list()

for i in range(8):
    pin_config.append(tk.StringVar())


# print(pin_config)

for i in range(8):
    for j,(key, value) in enumerate(radio_values.items()):
        tk.Radiobutton(root, text = key,value = value, variable = pin_config[i] ).grid(padx=10, row=i, column=j)
    

lbl = tk.Label(root, text = "initial")
btn = tk.Button(root, text = "Submit" , command = change_lbl )

lbl.grid(row=9, column=0)
btn.grid(row=10, column=0)

root.mainloop()