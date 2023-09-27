
from tkinter import * # Importing tkinter module
from PIL import Image, ImageTk # Importing Image
from tkinter import messagebox # Importing messagebox
import mysql.connector #importing mysql connector
import Admin_Page # Importing Admin_Page

class AdminLoginClass(): # Admin Login Class
     def __init__(self):
        self.root=Tk()
        self.root.title("Admin Login page") # Setting the title of the window
        self.root.geometry("1800x700+0+0") # Setting the size of the window
        
        
        self.bg=ImageTk.PhotoImage(file="images\path.png") # Setting the background image
        self.bg_image=Label(self.root, image=self.bg).place(x=30, y=-30)
        
        self.Email=StringVar() # Setting the variables for the entry fields
        self.Password=StringVar()   # Setting the variables for the entry fields

        Admin_Login = Label(text="Admin Login",font=("georgia", 18), padx=36, pady=10, bg="#A0E4CB", borderwidth=12) # Setting the label for the Admin Login
        Admin_Login.place(x=485, y=90, height=35,width=500)

        Admin_Email = Label(text="Email:",font=("georgia", 18), padx=36, pady=10, bg="#D7E9B9", borderwidth=12) # Setting the label for the Admin Email
        Admin_Email.place(x=485, y=190, height=35,width=196)
        Admin_Email_val = Entry(textvariable=self.Email, font=("georgia", 18))
        Admin_Email_val.place(x=700, y=190, height=35, width=300)

        Admin_Password = Label(text="Password:",font=("georgia", 18), padx=36, pady=10, bg="#D7E9B9", borderwidth=12) # Setting the label for the Admin Password``
        Admin_Password.place(x=485, y=250, height=35)
        Admin_Password_val = Entry( show="*", textvariable=self.Password, font=("georgia", 16))
        Admin_Password_val.place(x=700, y=250, height=35, width=300)
        
        AdminLog_Button = Button( text=" Login ", command=self.AdminLog, font=("georgia", 18), height=1, width=7,bg="#D7E9B9", borderwidth=10) # Setting the label for admin logout
        AdminLog_Button.place(x=585, y=340)
        
        AdminExi_Button = Button( text="Exit ", command= exit, font=("georgia", 18),height=1, width=7,bg="#D7E9B9", borderwidth=10)
        AdminExi_Button.place(x=750, y=340)
    
    
     def AdminLog(self): # Admin Login
        
        con = mysql.connector.connect(host = 'localhost' ,username = 'root', password = 'xyz', database = 'taxi_database')
        cur=con.cursor()
        con.commit()
        if self.Email =="" or self.Password == "":
                messagebox.showerror('Error',"* All Fields are required!!!", parent=self.root)
        else:
            try: # Exception handling
                cur.execute('SELECT * FROM admin_credentials WHERE Email=%s and Password=%s', (self.Email.get(), self.Password.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error','Invalid Credentials!!', parent=self.root)
                else:
                    messagebox.showinfo('Success','Welcome To the Admin System!',  parent=self.root)
                    self.root.destroy()
                    self.new_object = Admin_Page.AdminPageClass()
                con.close()

            except Exception as ex: # Exception handling
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)



if __name__=="__main__": # Main function
    obj = AdminLoginClass() #creating the object
    mainloop()
