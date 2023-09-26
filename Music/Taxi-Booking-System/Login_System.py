import sys #importing sys module
sys.path.append( ".") #adding the current directory to the path
from tkinter import * #importing all the widgets
import sqlite3 #importing sqlite3 module
from tkinter import messagebox #importing messagebox from tkinter
from PIL import Image, ImageTk #importing Image and ImageTk from PIL
from Customer_Login import CustLoginClass #importing CustLoginClass from Customer_Login.py
from Admin_Login import AdminLoginClass #importing AdminLoginClass from Admin_Login.py
from Driver_Login import DriverLoginClass #importing DriverLoginClass from Driver


class MainLoginClass(): #creating a class
    def __init__(self): #constructor
        self.root=Tk() #creating a root window
        self.root.title("Login system") #setting the title of the window
        self.root.geometry("1300x700+0+0") #setting the geometry of the window
        
        self.bg = ImageTk.PhotoImage(file="images\path.png") #setting the background image
        self.bg_image=Label(self.root, image=self.bg).place(x=30, y=-30) #placing the background image
        
        Main_Button = Button(self.root, text="Log in as ", font=("georgia", 16), padx=95, pady=10, bg="#D36B00", borderwidth=12) #creating a button
        Main_Button.place(x=450, y=100) #placing the button
        Main_Button = Button(self.root, text="Customer ", command=self.customer_login, font=("georgia", 16), padx=36, pady=10, bg="#D7E9B9", borderwidth=12) #creating a button
        Main_Button.place(x=500, y=200)
        Main_Button = Button(self.root, text="Driver", command=self.driver_login,  font=("georgia", 15), padx=57, pady=10, bg= "#FAEAB1", borderwidth=12) #creating a button
        Main_Button.place(x=500, y=300)

        Main_Button = Button(self.root, text="Admin ", command=self.admin_login, font=("georgia", 17), padx=48, pady=7, bg="#FAAB78", borderwidth=12) #creating a button
        Main_Button.place(x=500, y=400)


    def customer_login(self): #creating a function
        self.root.destroy() #destroying the root window
        self.new_obj = CustLoginClass()

    def driver_login(self): #creating a function
        self.root.destroy() #destroying the root window
        self.new_obj = DriverLoginClass() #creating a new object

    def admin_login(self): #creating a function
        self.root.destroy() #destroying the root window
        self.new_obj = AdminLoginClass() #creating a new object


if __name__=="__main__": #main function
    obj = MainLoginClass() #creating an object
    mainloop() #running the mainloop


