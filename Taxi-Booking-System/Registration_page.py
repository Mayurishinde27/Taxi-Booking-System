from tkinter import * #importing tkinter
import sqlite3 #importing sqlite3
import re #importing regular expression
from PIL import Image, ImageTk #importing PIL
import PIL #importing PIL
from tkinter import messagebox #importing messagebox
from Login_System import MainLoginClass #importing Login_System
from tkinter import ttk #importing ttk
import mysql.connector #importing mysql.connector

class RegistrationPageClass(): #creating class
    def __init__(self): #creating constructor
        self.root=Tk() #creating object of Tk
        self.root.title("Registration page") #title of the page
        self.root.geometry("1300x700+100+0") #size of the page
        self.root.configure(background="#E7AB79") #background color of the page
        # self.root.configure(background="white") #background color of the page

        self.Name=StringVar() #creating object of StringVar
        self.Address=StringVar() #creating object of StringVar
        self.Phonenumber=IntVar() #creating object of IntVar
        self.Email=StringVar() #creating object of StringVar
        self.CreditCardNo=IntVar() #creating object of IntVar
        self.Password=StringVar() #creating object of StringVar


        Reg_Frame = Frame(self.root, bg="#59C1BD") #defining frame
        Reg_Frame.place(x=360, y=10, height=680, width=600) #position of the frame
        
        self.image = PIL.Image.open(r"images\reg-back.png") #opening image
        self.img = ImageTk.PhotoImage(self.image) #converting image to tkinter image
        self.l = Label(Reg_Frame,image=self.img) #defining label
        self.l.pack() #packing label


        Heading = Label(Reg_Frame, text= 'Registration', font= 'georgia 20', bg='#E7AB79') #defining label
        Heading.place(x=150, y=50,width=300)

        Name_ = Label(Reg_Frame, text="Name :", font=("georgia", 18), bg="#E7AB79").place(x=30, y=150, height=30,width=200) #defining label
        Name_val = Entry(Reg_Frame, font=("georgia", 18), textvariable=self.Name,  bg="#CFD2CF").place(x=260, y=150, height=30,width=300)

        Address_ = Label(Reg_Frame, text="Address :", font=("georgia", 18), bg="#E7AB79").place(x=30, y=200, height=30,width=200) #defining label
        Address_val = Entry(Reg_Frame, font=("georgia", 18), textvariable=self.Address,  bg="#CFD2CF").place(x=260, y=200, height=30,width=300)

        Phone_= Label(Reg_Frame, text="Phone :", font=("georgia", 18), bg="#E7AB79").place(x=30, y=250, height=30,width=200) #defining label
        Phone_val = Entry(Reg_Frame, font=("georgia", 18), textvariable=self.Phonenumber, bg="#CFD2CF").place(x=260, y=250, height=30,width=300)
      
        Email_ = Label(Reg_Frame, text="Email :", font=("georgia", 18), bg="#E7AB79").place(x=30, y=300, height=30,width=200) #defining label
        Email_val = Entry(Reg_Frame, font=("georgia", 12), textvariable=self.Email, bg="#CFD2CF").place(x=260, y=300, height=30, width=300)  
   
        Credit_ = Label(Reg_Frame, text="Credit Card : ", font=("georgia", 18), bg="#E7AB79").place(x=30, y=350, height=30,width=200)
        Credit_val = Entry(Reg_Frame, font=("georgia", 18), textvariable=self.CreditCardNo,bg="#CFD2CF").place(x=260, y=350, height=30,width=300)

        Password_ = Label(Reg_Frame, text="Password :", font=("georgia", 18), bg="#E7AB79").place(x=30, y=400, height=30,width=200)
        Password_val = Entry(Reg_Frame, font=("georgia", 18),show="*", textvariable=self.Password,bg="#CFD2CF").place(x=260, y=400, height=30,width=300)

        Register_Button=Button(Reg_Frame, text="Register", command=self.Check_details, font=("georgia", 18, "bold"), bg="#E7AB79",borderwidth=4).place(x=150, y=520, height=50)
        Login_Button=Button(Reg_Frame, text="Login", command=self.Log, font=("georgia", 18, "bold"), bg="#E7AB79",borderwidth=4).place(x=350, y=520, width= 100, height=50)
        
        
        Your_Name = self.Name.get()  #getting name
        address = self.Address.get() #getting address
        Phone_no = self.Phonenumber.get()   #getting phone number
        Mail_id = self.Email.get() #getting email
        Credit_details = self.CreditCardNo.get() #getting credit card number
        Password_details = self.Password.get() #getting password
    
            

    def check(self): #function to check email
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' #regex for email
        if(re.fullmatch(regex, self.Email.get())): 
            return True
        else:
            return False

    def Check_details(self): #function to check details

        if self.check(): #calling check function
            if (self.Name.get() == "") or (self.Address.get() == "") or (self.Phonenumber.get() == "") or (self.Email.get() == "") or (self.Password.get() == "") or (self.CreditCardNo.get() == ""):
                messagebox.showerror("Error","Fields Can Not Be EMPTY",parent=self.root) 

            try:
                #connecting to database
                con = mysql.connector.connect(host = 'localhost' ,username = 'root', password = 'xyz', database = 'taxi_database')
                cur=con.cursor()
                cur.execute("INSERT INTO customer_reg (Name, Address, Phone_no, Email, Credit_Card, Password) values(%s,%s, %s,%s, %s,%s)",
                            (
                             self.Name.get(),
                             self.Address.get(),
                             self.Phonenumber.get(),
                             self.Email.get(),
                             self.CreditCardNo.get(),
                             self.Password.get(),
                            ))
                con.commit() #commiting changes
                con.close() #closing connection
                messagebox.showinfo("Success","You have registered successfully!!", parent=self.root)
                self.Remove_details() #calling remove details function
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def Remove_details(self): #function to remove details
        self.Name.set(""), 
        self.Address.set(""),
        self.Phonenumber.set(""),
        self.Email.set(""),
        self.CreditCardNo.set(""),
        self.Password.set(""),
                
        
    def Log(self): #function to login
        self.root.destroy()
        self.new_obj = MainLoginClass()
                
           
        
if __name__=="__main__":         
    obj = RegistrationPageClass() #creating object
    mainloop()
