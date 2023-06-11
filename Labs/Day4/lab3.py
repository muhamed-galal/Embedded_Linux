import tkinter as tk
from tkinter import messagebox

def change_LBL():
    global name
    global labl
    labl.configure(text = name.get())
    messagebox.showwarning(title= "info",message = "Label changed")

root =tk.Tk()
root.geometry("200x200+400+400")
root.title("GALAL WORK")

name = tk.StringVar()
ent=tk.Entry(root,textvariable=name,show="*")
labl=tk.Label(root,text="Pass")
btn=tk.Button(root,text ="Submit",command=change_LBL) 


ent.pack(pady=50,padx=50)
labl.pack(side="top")
btn.pack(padx=10,pady=10)

# difference between entry and textbox
''' textbox flexible can be used for rich text '''
#entry for simple form
root.mainloop() 

