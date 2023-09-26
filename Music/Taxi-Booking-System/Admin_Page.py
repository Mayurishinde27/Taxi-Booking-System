
from tkinter import *  # Import tkinter
import sqlite3 # Import sqlite3
from tkinter import ttk, messagebox # Import ttk and messagebox from tkinter
import mysql.connector # Import mysql.connector
from PIL import Image, ImageTk # Import image and imageTk from PIL
import PIL # Import PIL
from tkcalendar import * # Import tkcalendar
from datetime import *  # Import datetime

class AdminPageClass(): # Create a class
    def __init__(self):
        root=Tk() # Create a root window
        self.root=root # Set the root window
        self.root.title("Admin Booking Area") # Set the title of the root window
        self.root.geometry("1800x700+0+0") # Set the size of the root window
        
        self.bg = ImageTk.PhotoImage(file="images\path.png") # Set the background image
        self.bg_image = Label(self.root, image=self.bg).pack(side=TOP) # Set the background image
         

        Admin_Frame = Frame(self.root, bg="white") # Create a frame
        Admin_Frame.place(x=50, y=30, height=640, width=520) # Set the frame

        # Set the background image
        self.image = PIL.Image.open(r"images\reg-back.png") 
        self.img = ImageTk.PhotoImage(self.image)
        self.l = Label(Admin_Frame,image=self.img)
        self.l.pack()

        # Set the variables
        self.admin_id=IntVar()
        self.customer_name=StringVar()
        self.pickup_date=StringVar()
        self.pickup_time=StringVar()
        self.pickup_location=StringVar()
        self.dropoff_location=StringVar()
        self.no_taxis=StringVar()
        self.credit_card_no=StringVar()
        self.driver_name=StringVar()
        self.driver_licenes_plate=StringVar()

        # Set the heading
        Heading = Label(Admin_Frame, text= 'Admin Page', font= 'georgia 20', bg='#E7AB79')
        Heading.place(x=80, y=30,width=350)

        # Set the labels and entries
        Name_ = Label(Admin_Frame, text="Customer name :", font=("georgia", 18), bg="#E7AB79").place(x=20, y=120, height=30,width=200)
        Name_val = Entry(Admin_Frame, font=("georgia", 18), textvariable=self.customer_name,  bg="#CFD2CF").place(x=260, y=120, height=30, width=170)

        Pickup_date = Label(Admin_Frame, text="Pickup date :", font=("georgia", 18), bg="#E7AB79").place(x=20, y=170, height=30,width=200)
        Pickup_date_val = DateEntry(Admin_Frame,state = "readonly",font=("georgia", 18), textvariable=self.pickup_date,  bg="#CFD2CF").place(x=260, y=170, height=30, width=170)

        Pickup_time= Label(Admin_Frame, text="Pickup time :", font=("georgia", 18), bg="#E7AB79").place(x=20, y=210, height=30,width=200)
        Pickup_time_val = Entry(Admin_Frame, font=("georgia", 18), textvariable=self.pickup_time, bg="#CFD2CF").place(x=260, y=210, height=30, width=170)
      
        Pickup_Location = Label(Admin_Frame, text="Pickup Location :", font=("georgia", 18), bg="#E7AB79").place(x=20, y=250, height=30,width=200)
        Pickup_Location_val = Entry(Admin_Frame, font=("georgia", 18), textvariable=self.pickup_location, bg="#CFD2CF").place(x=260, y=250, height=30, width=170)

        Dropoff_location = Label(Admin_Frame, text="Dropoff Location :", font=("georgia", 18), bg="#E7AB79").place(x=20, y=290, height=30,width=200)
        Dropoff_location_val = Entry(Admin_Frame,font=("georgia", 18), textvariable=self.dropoff_location,  bg="#CFD2CF").place(x=260, y=290, height=30, width=170)

        Taxi_ = Label(Admin_Frame, text="Taxi's required :", font=("georgia", 18), bg="#E7AB79").place(x=20, y=330, height=30,width=200)
        Taxi_val = Entry(Admin_Frame,font=("georgia", 18), textvariable=self.no_taxis,  bg="#CFD2CF").place(x=260, y=330, height=30, width=170)

        Driver_N = Label(Admin_Frame, text="Driver's name : ", font=("georgia", 18), bg="#E7AB79").place(x=20, y=370, height=30,width=200)
        Driver_N_val = Entry(Admin_Frame, font=("georgia", 18), textvariable=self.driver_name,bg="#CFD2CF").place(x=260, y=370, height=30, width=170)

        Driver_L = Label(Admin_Frame, text="licences no : ", font=("georgia", 18), bg="#E7AB79").place(x=20, y=410, height=30,width=200)
        Driver_L_val = Entry(Admin_Frame, font=("georgia", 18), textvariable=self.driver_licenes_plate,bg="#CFD2CF").place(x=260, y=410, height=30, width=170)

        # Set the buttons
        
        confirm_Button = Button(Admin_Frame, text= "Confirm", command=self.confirm, font=("georgia", 17), bg="#D7E9B9", borderwidth=3).place(x=50, y=530, height=30, width=100)

        Bill_Button = Button(Admin_Frame, text= "Bill", command=self.bill, font=("georgia", 18), bg="#D7E9B9", borderwidth=3).place(x=180, y=530, height=30, width=100)
        
        clear_Button = Button(Admin_Frame, text= "Clear", command=self.clear, font=("georgia", 18), bg="#D7E9B9", borderwidth=3).place(x=310, y=530, height=30, width=100)


        # Set the frame for the table
        Admin_FrameView = Frame(self.root, bg="white")
        Admin_FrameView.place(x=600, y=30, height=640, width=800)
        
        # Set the heading for the table
        title=Label( Admin_FrameView, text="Your Booking Details", font=("impact", 20, "bold"), bg="white")
        title.place(x=120, y=15)  
        
        # Set the table
        scrolly=Scrollbar(Admin_FrameView,orient=VERTICAL)
        scrollx=Scrollbar(Admin_FrameView,orient=HORIZONTAL) 
        
        # Set the table
        self.admin_Table=ttk.Treeview(Admin_FrameView,columns=("admin_id","customer_name","pickup_date", "pickup_time", "pickup_location", "dropoff_location", "no_taxis", "driver_name", "driver_licenes_plate"), yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.admin_Table.xview)
        scrolly.config(command=self.admin_Table.yview)
        
        self.admin_Table.heading("admin_id", text="adming ID")
        self.admin_Table.heading("customer_name",text="Customer name")
        self.admin_Table.heading("pickup_date",text="Pickup date")
        self.admin_Table.heading("pickup_time",text="Pickup time")
        self.admin_Table.heading("pickup_location",text="Pickup address")
        self.admin_Table.heading("dropoff_location",text="Dropoff destination")
        self.admin_Table.heading("no_taxis",text="No of cars required")
        self.admin_Table.heading("driver_name", text="driver name")
        self.admin_Table.heading("driver_licenes_plate", text="driver licences plate")

        self.admin_Table["show"]="headings"
        self.admin_Table.column("admin_id", width=100)
        self.admin_Table.column("customer_name",width=100)
        self.admin_Table.column("pickup_date",width=100)
        self.admin_Table.column("pickup_time",width=100)
        self.admin_Table.column("pickup_location",width=100)
        self.admin_Table.column("dropoff_location",width=100)
        self.admin_Table.column("no_taxis",width=100)
        self.admin_Table.column("driver_name", width=100)
        self.admin_Table.column("driver_licenes_plate", width=100)

        self.admin_Table.pack(fill=BOTH,expand=1)
        self.admin_Table.bind("<ButtonRelease-1>",self.get_data)
        self.show() 
        
        #showing the data
    def show(self): # function to show the data in the table
        # connection to the database
        con = mysql.connector.connect(host = 'localhost' ,username = 'root', password = 'Richa@3217', database = 'taxi_database')
        cur=con.cursor()
        try:
            cur.execute("select * from admin_page")
            rows=cur.fetchall()
            self.admin_Table.delete(*self.admin_Table.get_children())
            for row in rows:
                self.admin_Table.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    #getting data
    def get_data(self,ev):
        f=self.admin_Table.focus()
        content=(self.admin_Table.item(f))
        row=content['values']
        self.admin_id.set([0]),
        self.customer_name.set(row[1]),
        self.pickup_date.set(row[2]),
        self.pickup_time.set(row[3]),
        self.pickup_location.set(row[4]),
        self.dropoff_location.set(row[5]),
        self.no_taxis.set(row[6]),
        self.driver_name.set(row[7]),
        self.driver_licenes_plate.set(row[8])
        
    def clear(self): #clear function
        self.customer_name.set("",), #clearing the entry box
        self.pickup_date.set(""),
        self.pickup_time.set(""),
        self.pickup_location.set(""),
        self.dropoff_location.set(""),
        self.no_taxis.set(""),
        self.driver_name.set(""),
        self.driver_licenes_plate.set("")
        
        
    def confirm(self): #confirm function
        # connection to the database
        con = mysql.connector.connect(host = 'localhost' ,username = 'root', password = 'Richa@3217', database = 'taxi_database')
        cur=con.cursor() #cursor is used to execute the query
        cur.execute("INSERT INTO admin_page (Customer_Name,Pickup_Date, Pickup_Time, Pickup_Location, Dropoff_Location, Taxi_required, Driver_Name, Driver_Licenes_Plate) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                    (self.customer_name.get(),
                     self.pickup_date.get(),
                     self.pickup_time.get(),
                     self.pickup_location.get(),
                     self.dropoff_location.get(),
                     self.no_taxis.get(),
                     self.driver_name.get(),
                     self.driver_licenes_plate.get()
                    ))
        con.commit() #commit is used to save the changes
        messagebox.showinfo("success", "congratulations! booking confirmed successfully", parent=self.root)
        con.close() #close the connection
        
        
        Admin_FrameView=Frame(self.root, bg="white") #frame for the view
        Admin_FrameView.place(x=560, y=30, height=640, width=770)


    def bill(self): #bill function
        self.root=Toplevel() #creating a new window
        self.root.title("Billing System") #title of the window
        self.root.geometry("700x630+600+10")
        self.root.config(bg="#FAEAB1")

        self.bg1=ImageTk.PhotoImage(file="images\purple.png")
        self.bg_image=Label(self.root, image=self.bg1).pack(side=TOP)
        
        self.distance=StringVar()
        self.amount=IntVar()
        self.total=IntVar()
        self.name=StringVar()
        
        #setting the labels
        Customer_name = Label(self.root, text="Customer Name :", bg="#FAEAB1", font=("georgia", 18)).place(x=50, y=50)
        Customer_name_val = Entry(self.root, textvariable=self.name, font=("georgia", 14)).place(x=300, y=50)
        
        Total_KM = Label(self.root, text="Total KM travel:", bg="#FAEAB1", font=("georgia", 18)).place(x=50, y=100)
        Total_KM_val = Entry(self.root, textvariable=self.distance, font=("georgia", 14)).place(x=300, y=100)
        
        Price_KM = Label(self.root, text="Price pr KM", bg="#FAEAB1", font=("georgia", 18)).place(x=50, y=150)
        Price_KM_val = Entry(self.root, textvariable=self.amount, font=("georgia", 14)).place(x=300, y=150)
        
        # setting the button
        Multipy_Button = Button(self.root, command=self.multiply, text="Multiply").place(x=300, y=200)
        
        Total_amt = Label(self.root, text="Total amount $", bg="#FAEAB1", font=("georgia", 18)).place(x=50, y=250)
        Total_amt_val = Entry(self.root, textvariable=self.total, font=("georgia", 14)).place(x=300, y=250)
        
        Final_amt = Label(self.root, text="Your total amount : ", bg="#FAEAB1", font=("georgia", 18)).place(x=50, y=300)
        Final_amt_val = Entry(self.root, textvariable=self.total, font=("georgia", 14)).place(x=300, y=300, width=250)

    def multiply(self): #multiply function

         val1 = int(self.distance.get()) #getting the value from the entry box
         val2 = int(self.amount.get()) #getting the value from the entry box
         total = val1*val2 #multiplying the values
         self.total.set(str(total)) #setting the value in the entry box
         con = mysql.connector.connect(host = 'localhost' ,username = 'root', password = 'Richa@3217', database = 'taxi_database')
         cur=con.cursor()
         cur.execute("INSERT INTO bill (Customer_Name, Total_Distance, Charge_per_KM, Total_price ) values(%s, %s,%s,%s)",
                    (self.name.get(), 
                     self.distance.get(),
                     self.amount.get(),
                     self.total.get()
                    )) #updating or inserting data into the database
         con.commit()
         messagebox.showinfo("success", "Billing is Done", parent=self.root)
         con.close()

      
if __name__=="__main__":    
        
    obj = AdminPageClass() #creating object of the class
    mainloop() # runnig the mainloop 