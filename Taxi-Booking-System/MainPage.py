import sys # import sys module
sys.path.append( ".") # add current directory to path
from tkinter import * # import all from tkinter module
from tkinter import messagebox # import messagebox from tkinter module
from PIL import Image, ImageTk # import Image and ImageTk from PIL module
from Registration_page import RegistrationPageClass # import RegistrationPageClass from Registration_page module
from Login_System import MainLoginClass # import MainLoginClass from Login_System module

# Main Page
class MainPageClass: # create class MainPageClass
    def __init__(self): # create constructor
        self.root=Tk() # create object of Tk class
        self.root.title("welcome to taxi booking system") # set title of window
        self.root.geometry("1300x700+0+0") # set geometry of window

        self.backimg=ImageTk.PhotoImage(file="images\Taxicab2.png") # set image
        self.bg_image=Label(self.root, image=self.backimg).place(x=30, y=-30) # set image on window


        Home_Button = Button(self.root, text="Login ", command=self.Log, font=("georgia", 16), padx=36, pady=10, bg="#D7E9B9", borderwidth=12) # create button
        Home_Button.place(x=100, y=100)
        Home_Button = Button(self.root, text="Register", command=self.Reg,  font=("georgia", 15), padx=30, pady=10, bg= "#FAEAB1", borderwidth=12) # create button
        Home_Button.place(x=100, y=200)
        Home_Button = Button(self.root, text="Exit ", command=self.Exi, font=("georgia", 17), padx=44, pady=7, bg="#FAAB78", borderwidth=12) # create button
        Home_Button.place(x=100, y=300)


    def Log(self): # create method
        self.root.destroy() # destroy window
        self.new_obj = MainLoginClass() # create object of MainLoginClass

    def Reg(self): # create method
        self.root.destroy() # destroy window
        self.new_obj = RegistrationPageClass() # create object of RegistrationPageClass

    def Exi(self): # create method
        self.root.destroy() # destroy window
        self.exit() # call exit method


if __name__=="__main__":
    obj = MainPageClass() # create object of MainPageClass
    mainloop() # call mainloop method
