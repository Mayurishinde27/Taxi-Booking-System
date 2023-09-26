import sys #importing sys module
sys.path.append( ".") #adding the path of the current directory
from logging import exception #importing exception from logging module
from tkinter import * #importing all from tkinter module
from PIL import Image, ImageTk #importing Image and ImageTk from PIL module
from tkinter import messagebox #importing messagebox from tkinter module
from tkinter import ttk #importing ttk from tkinter module
import mysql.connector #importing mysql.connector module
from Customer_Booking  import CustBookingSystemClass    #importing CustBookingSystemClass from Customer_Booking.py


 
class CustLoginClass(): #creating a class CustLoginClass
     def __init__(self): #creating a constructor
        self.root=Tk() #creating a root object
        self.root.title("Customer Login Page")
        self.root.geometry("1300x700+100+0")

        self.bg=ImageTk.PhotoImage(file="images\path.png") #adding the path of the image
        self.bg_image=Label(self.root, image=self.bg).place(x=30, y=-30) #placing the image
        

        self.Email=StringVar() #creating a string variable
        self.Password=StringVar() #creating a string variable
        self.securityanswer=StringVar()
        self.newpassword=StringVar()
    
        # Labels
        Customer_Login = Label(text="Customer Login",font=("georgia", 18), padx=36, pady=10, bg="#A0E4CB", borderwidth=12) #creating a label
        Customer_Login.place(x=485, y=90, height=35,width=500) #placing the label


        Customer_Email = Label(text="Email:",font=("georgia", 18), padx=36, pady=10, bg="#D7E9B9", borderwidth=12).place(x=485, y=150, height=35,width=196) #creating a label
        Customer_Email_val = Entry(textvariable=self.Email, font=("times new roman", 18)).place(x=700, y=150, height=35, width=300) #creating an entry


        Customer_Password = Label(text="Password:",font=("georgia", 18), padx=36, pady=10, bg="#D7E9B9", borderwidth=12).place(x=485, y=220, height=35) #creating a label
        Customer_Password_val = Entry( show="*", textvariable=self.Password, font=("georgia", 16)).place(x=700, y=220, height=35, width=300) #creating an entry
  
        # Buttons
        CustomerLog_Button = Button( text=" Login ", command=self.CustomerLog, font=("georgia", 18), height=1, width=7,bg="#D7E9B9", borderwidth=10) #creating a button
        CustomerLog_Button.place(x=585, y=400) 
        
        CustomerExi_Button=Button( text="Exit ", command= exit, font=("georgia", 18),height=1, width=7,bg="#D7E9B9", borderwidth=10) #creating a button
        CustomerExi_Button.place(x=750, y=400)
        

     def CustomerLog(self): #creating a function CustomerLog
        con = mysql.connector.connect(host = 'localhost' ,username = 'root', password = 'Richa@3217', database = 'taxi_database')
        cur=con.cursor()#creating a cursor object
        con.commit() #commiting the connection then closing it.
        if self.Email =="" or self.Password == "": #checking if the fields are empty
                messagebox.showerror('Error',"* All Fields are required!!!", parent = self.root)
        else:
            try:
                cur.execute('SELECT * FROM customer_reg WHERE Email=%s and Password=%s', (self.Email.get(), self.Password.get()))
                data = cur.fetchone()
                if data==None:
                    messagebox.showerror('Error','Invalid Credentials!!', parent = self.root)   
                else:
                    messagebox.showinfo('Success','Welcome To Taxi Booking System!!, Have a great day!',  parent = self.root)
                    self.root.destroy()
                    self.new_obj = CustBookingSystemClass()
                con.close()
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

if __name__=="__main__":#creating a main function
    obj = CustLoginClass() #creating an object
    mainloop() #calling the mainloop function
