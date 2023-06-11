from tkinter import *

def ButtonPressTracker():
    ButtonPressTracker.counter +=1 
    print("The button pressed" , ButtonPressTracker.counter)
ButtonPressTracker.counter =0

def PrintmyName():
    print("Mohamed Galal")


# construct main window through calling TK()
# window_1 = tk.Tk() for other python versions  
window_1 = Tk() 

# adding title to the window 

window_1.title("welcome ITI ")

# controlling window geometry in pixles 
window_1.geometry('1000x500')   # width X heoght 

# Adding button to a specific window with a specific name and specific button name 
label_1  =Label(window_1 , text = "GELO")

# Adding a photo image object to use image 
#photo_1 = PhotoImage(file='images.png')

# editing of the image resizing of it 
# resizing decreased by increasing the number 
#photo_1 = photo_1.subsample(1,1)

B_1  =Button(window_1 , text = "Close the window" , background= 'blue' ,fg="black", bd = '10' , command = window_1.destroy)
B_1.pack(side = TOP)

B_1  =Button(window_1 , text = "Print My name" , bd = '5' , command = PrintmyName)
B_1.pack(side = LEFT)

B_3  =Button(window_1 , text = "RIGHT", background= 'blue' , bd = '5')
B_3.place(relx=0.5,rely=0.5,anchor=E)


B_1  =Button(window_1 , text = "Increment The button" , bd = '5' , command = ButtonPressTracker)
B_1.pack(side = BOTTOM)

label_1.pack(side = TOP)

# Call the main loop which is used when the application is ready to run to keep the code displaying 
window_1.mainloop()