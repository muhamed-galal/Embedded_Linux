import tkinter as tk
from tkinter import messagebox

def check_bin(binary_str):
    isBinary=True
    binary_set={'1','0'}
    input_set=set([b for b in binary_str if b in ('0', '1')])
   # print(input_set)
    if input_set != binary_set:
        isBinary=False
    else:
        isBinary = True    
    return isBinary

def PrepareMessageString(binary_str):
    output = str()
    for i,b in enumerate(binary_str): #iterator in iterable enumarate return tuble of iterable and index
        if b == '0':
            output += ("pin " + str(i) + "->" + "input\n")           
        else:
            output += ("pin " + str(i) + "->" + "output\n")           
    return output

def change_LBL():
    global name
    isbinary=check_bin(name.get())
    if not isbinary:
        messagebox.showwarning(title= "info",message = "not binary")
    else:
       DDRA_CONFIG= PrepareMessageString(name.get())
       messagebox.showinfo(title= "config ", message = DDRA_CONFIG ) 

root =tk.Tk()
root.geometry("200x200+400+400")
root.title("GALAL WORK")

name = tk.StringVar()
ent=tk.Entry(root,textvariable=name)
btn=tk.Button(root,text ="Submit",command=change_LBL) 


ent.pack(pady=50,padx=50)
btn.pack(padx=10,pady=10)

# difference between entry and textbox
''' textbox flexible can be used for rich text '''
#entry for simple form
root.mainloop() 

