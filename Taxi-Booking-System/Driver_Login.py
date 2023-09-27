from sqlite3.dbapi2 import Cursor, Row # type: ignore
from tkinter import * #importing tkinter
import sqlite3 #importing sqlite3
from PIL import Image, ImageTk #importing PIL
from tkinter import messagebox #importing messagebox
import Driver_viewBooking #importing Driver_viewBooking.py
import mysql.connector #importing mysql.connector


class DriverLoginClass(): #class for Driver Login
     def __init__(self): #constructor
        self.root=Tk() #creating object of Tk class
        self.root.title("Driver Login Page") #title of the window
        self.root.geometry("1800x700+0+0") #size of the window

        self.bg = ImageTk.PhotoImage(file="images\path.png") #path of the image
        self.bg_image = Label(self.root, image=self.bg).place(x=30, y=-30) #placing the image

        self.Email = StringVar() #creating object of StringVar class
        self.Password = StringVar() #creating object of StringVar class

        Driver_Login = Label(text="Driver Login",font=("georgia", 18), padx=36, pady=10, bg="#A0E4CB", borderwidth=12) #creating label
        Driver_Login.place(x=485, y=90, height=35,width=500) #placing the label

        Driver_Email = Label(text="Email:",font=("georgia", 18), padx=36, pady=10, bg="#D7E9B9", borderwidth=12) #creating label
        Driver_Email.place(x=485, y=190, height=35,width=196)
        Driver_Email_val = Entry(textvariable=self.Email, font=("georgia", 18))
        Driver_Email_val.place(x=700, y=190, height=35, width=300)

        Driver_Password = Label(text="Password:",font=("georgia", 18), padx=36, pady=10, bg="#D7E9B9", borderwidth=12)
        Driver_Password.place(x=485, y=250, height=35)
        Driver_Password_val = Entry( show="*", textvariable=self.Password, font=("georgia", 16))
        Driver_Password_val.place(x=700, y=250, height=35, width=300)

        DriverLog_Button = Button( text=" Login ", command=self.DriverLog, font=("georgia", 18), height=1, width=7,bg="#D7E9B9", borderwidth=10)
        DriverLog_Button.place(x=585, y=340)

        DriverExi_Button = Button( text="Exit ", command= exit, font=("georgia", 18),height=1, width=7,bg="#D7E9B9", borderwidth=10)
        DriverExi_Button.place(x=750, y=340)


     def DriverLog(self): #function for Driver Login
        con = mysql.connector.connect(host = 'localhost' ,username = 'root', password = 'xyz', database = 'taxi_database') #connecting to database
        cur=con.cursor() #creating object of cursor class
        con.commit() #commiting the changes
        if self.Email =="" or self.Password == "": #checking if the fields are empty
                messagebox.showerror("* All Fields are required!!!", parent=self.root) #showing error message
        else:
            try:
                cur.execute("SELECT * FROM driver_credentials WHERE D_Email=%s and D_Password=%s", (self.Email.get(), self.Password.get())) #executing the query
                row=cur.fetchone() #fetching the data
                if row==None: #checking if the data is empty
                    messagebox.showerror('Error','Invalid Credentials!!', parent=self.root) #showing error message
                else:
                    messagebox.showinfo('Success','Welcome To Taxi Booking System!!, Have a safe drive!',  parent=self.root) #showing success message
                    self.root.destroy() #destroying the window
                    self.new_obj = Driver_viewBooking.DriverVieBookingClass() #creating object of DriverVieBookingClass class
                con.close() #closing the connection
            except Exception as ex: #handling exception
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root) #showing error message

if __name__=="__main__": #main function
    obj = DriverLoginClass()
    mainloop()
