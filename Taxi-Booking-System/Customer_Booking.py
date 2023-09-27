import sys # import sys module
sys.path.append( ".") # add current directory to path
from tkinter import * # import tkinter module
from tkinter import messagebox, ttk # import messagebox and ttk from tkinter
import mysql.connector # import mysql connector
from tkcalendar import * # import tkcalendar
from datetime import *  # import datetime
from tkinter.ttk import Style, Treeview # import style and treeview from tkinter.ttk
from PIL import Image, ImageTk # import image and imageTk from PIL
import PIL # import PIL

class CustBookingSystemClass(): # create class
    def __init__(self): # create constructor
        root=Tk()
        self.root=root # create root
        self.root.title("Customrt Booking system") # set title
        self.root.geometry("1800x700+0+0")

        self.bg=ImageTk.PhotoImage(file="images\path.png")
        self.bg_image=Label(self.root, image=self.bg).pack(side=TOP)
   
        self.booking_id=IntVar() # create booking id variable
        self.customer_name=StringVar() # create customer name variable
        self.booking_date=StringVar() # create booking date variable
        self.pickup_date=StringVar() # create pickup date variable
        self.pickup_time=StringVar() # create pickup time variable
        self.pickup_location=StringVar() # create pickup location variable
        self.dropoff_location=StringVar() # create dropoff location variable
        self.no_taxis=StringVar() # create no of taxis variable
        self.credit_card_no=StringVar() # create credit card no variable
        self.driver_name=StringVar() # create driver name variable
        self.driver_licenes_plate=StringVar() # create driver license plate variable
        
        # create current date label
        current_Date = Label(root, text="Current date: " + datetime.now().strftime('%Y/%m/%d'),  font= 'georgia 13', bg='#E7AB79').place(x  = 700, y = 5)
 
        
        Booking_Frame=Frame(self.root, bg="white") # create booking frame
        Booking_Frame.place(x=50, y=30, height=640, width=520) # set booking frame

        # setting the background image 
        self.image = PIL.Image.open(r"images\reg-back.png")
        self.img = ImageTk.PhotoImage(self.image)
        self.l = Label(Booking_Frame,image=self.img)
        self.l.pack()

        # create heading
        Heading = Label(Booking_Frame, text= 'Customer Booking', font= 'georgia 20', bg='#E7AB79')
        Heading.place(x=80, y=50,width=350)

        # create name label
        Name_ = Label(Booking_Frame, text="Customer name :", font=("georgia", 18), bg="#E7AB79").place(x=20, y=120, height=30,width=200)
        Name_val = Entry(Booking_Frame, font=("georgia", 18), textvariable=self.customer_name,  bg="#CFD2CF").place(x=260, y=120, height=30, width=170)

        # create booking date label
        Booking_date = Label(Booking_Frame, text="Booking date :", font=("georgia", 18), bg="#E7AB79").place(x=20, y=160, height=30,width=200)
        Booking_date_val = DateEntry(Booking_Frame,state = "readonly",font=("georgia", 18), textvariable=self.booking_date,  bg="#CFD2CF").place(x=260, y=160, height=30, width=170)

        # create pickup date label
        Pickup_date = Label(Booking_Frame, text="Pickup date :", font=("georgia", 18), bg="#E7AB79").place(x=20, y=200, height=30,width=200)
        Pickup_date_val = DateEntry(Booking_Frame,state = "readonly",font=("georgia", 18), textvariable=self.pickup_date,  bg="#CFD2CF").place(x=260, y=200, height=30, width=170)

        # create pickup time label
        Pickup_time= Label(Booking_Frame, text="Pickup time :", font=("georgia", 18), bg="#E7AB79").place(x=20, y=240, height=30,width=200)
        Pickup_time_val = Entry(Booking_Frame, font=("georgia", 18), textvariable=self.pickup_time, bg="#CFD2CF").place(x=260, y=240, height=30, width=170)

        # create pickup location label
        Pickup_Location = Label(Booking_Frame, text="Pickup Location :", font=("georgia", 18), bg="#E7AB79").place(x=20, y=280, height=30,width=200)
        Pickup_Location_val = Entry(Booking_Frame, font=("georgia", 18), textvariable=self.pickup_location, bg="#CFD2CF").place(x=260, y=280, height=30, width=170)

        # create dropoff location label
        Dropoff_location = Label(Booking_Frame, text="Dropoff Location :", font=("georgia", 18), bg="#E7AB79").place(x=20, y=320, height=30,width=200)
        Dropoff_location_val = Entry(Booking_Frame,font=("georgia", 18), textvariable=self.dropoff_location,  bg="#CFD2CF").place(x=260, y=320, height=30, width=170)

        # create no of taxis label
        Taxi_ = Label(Booking_Frame, text="Taxi's required :", font=("georgia", 18), bg="#E7AB79").place(x=20, y=360, height=30,width=200)
        Taxi_val = Entry(Booking_Frame,font=("georgia", 18), textvariable=self.no_taxis,  bg="#CFD2CF").place(x=260, y=360, height=30, width=170)

        # create credit card label
        Credit_ = Label(Booking_Frame, text="Credit Card : ", font=("georgia", 18), bg="#E7AB79").place(x=20, y=400, height=30,width=200)
        Credit_val = Entry(Booking_Frame, font=("georgia", 18), textvariable=self.credit_card_no,bg="#CFD2CF").place(x=260, y=400, height=30, width=170)

        
        # Buttons
        self.book_Button = Button(self.root, text= 'Book', font= ("georgia", 12), command= self.book,bg="#A0E4CB", borderwidth=10).place(x=70, y=530,width=78)
        self.update_Button = Button(self.root, text= 'Update', font= ("georgia", 12), command= self.update,bg="#A0E4CB", borderwidth=10).place(x=157, y=530,width=90)
        self.cancel_Button = Button(self.root, text= 'Cancel', font= ("georgia", 12), command= self.delete,bg="#A0E4CB", borderwidth=10).place(x=257, y=530,width=90)
        self.logout_Button = Button(self.root, text= 'Logout', font = ("georgia", 12), command=exit,bg="#A0E4CB", borderwidth=10).place(x=357, y=530,width=90)
        self.reset_Button = Button(self.root, text= 'Clear', font = ("georgia", 12), command= self.clear,bg="#A0E4CB", borderwidth=10).place(x=460, y=530,width=90)
 
        
        # create frame for view 
        frame_view=Frame(self.root, bg="grey") 
        frame_view.place(x=660, y=30, height=640, width=750)
        
        # create style for table
        style = Style()
        style.theme_use('default')
        style.configure("frame_view",
        background="grey",  
        foreground="black",
        rowheight=30,
        fieldbackground="grey")
        
        # create heading for table
        Heading = Label(frame_view, text= 'Your Booking Details', font= 'georgia 20', bg='#E7AB79')
        Heading.place(x=760, y=0,width=350) 
        
        # create scroll bar for table
        scrolly=Scrollbar(frame_view,orient=VERTICAL)
        scrollx=Scrollbar(frame_view,orient=HORIZONTAL) 
        
        # create table
        self.booking_Table=ttk.Treeview(frame_view,columns=("booking_id","customer_name", "booking_date","pickup_date", "pickup_time", "pickup_address", "dropoff_destination", "no_taxis", "creditcard_number"), yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.booking_Table.xview)
        scrolly.config(command=self.booking_Table.yview)
        
        # create heading for table
        self.booking_Table.heading("booking_id",text="booking ID")
        self.booking_Table.heading("customer_name",text="Customer name")
        self.booking_Table.heading("booking_date",text="Booking date")
        self.booking_Table.heading("pickup_date",text="Pickup date")
        self.booking_Table.heading("pickup_time",text="Pickup time")
        self.booking_Table.heading("pickup_address",text="Pickup location")
        self.booking_Table.heading("dropoff_destination",text="Dropoff location")
        self.booking_Table.heading("no_taxis",text="Taxi's required")
        self.booking_Table.heading("creditcard_number",text="Credit Card no.")

        # show the headings of the table
        self.booking_Table["show"]="headings"
        self.booking_Table.column("booking_id",width=100)
        self.booking_Table.column("customer_name",width=100)
        self.booking_Table.column("booking_date",width=100)
        self.booking_Table.column("pickup_date",width=100)
        self.booking_Table.column("pickup_time",width=100)
        self.booking_Table.column("pickup_address",width=100)
        self.booking_Table.column("dropoff_destination",width=100)
        self.booking_Table.column("no_taxis",width=100)
        self.booking_Table.column("creditcard_number",width=100)

        # show the table
        self.booking_Table.pack(fill=BOTH,expand=1)
        self.booking_Table.bind("<ButtonRelease-1>",self.get_data)
        self.show() 
        
        
    def show(self):
        # connecting to the database
        con = mysql.connector.connect(host = 'localhost' ,username = 'root', password = 'xyz', database = 'taxi_database')
        cur=con.cursor()
        try:
            cur.execute("select * from booking_details") # select all the data from the table
            rows=cur.fetchall() # fetch all the data from the table
            self.booking_Table.delete(*self.booking_Table.get_children()) # delete all the data from the table
            for row in rows: # insert all the data into the table 
                self.booking_Table.insert('',END,values=row) 

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root) # show error message if any error occurs
          
          
    def get_data(self,ev):  # get data from the table
        f=self.booking_Table.focus()
        content=(self.booking_Table.item(f))
        row=content['values']
        self.booking_id.set([0]),
        self.customer_name.set(row[1]),
        self.booking_date.set(row[2]),
        self.pickup_date.set(row[3]),
        self.pickup_time.set(row[4]),
        self.pickup_location.set(row[5]),
        self.dropoff_location.set(row[6]),
        self.no_taxis.set(row[7]),
        self.credit_card_no.set(row[8]),


    def book(self): # book the taxi
        # connecting to the database
        con = mysql.connector.connect(host = 'localhost' ,username = 'root', password = 'xyz', database = 'taxi_database')
        cur=con.cursor()
        cur.execute("INSERT INTO booking_details (Customer_Name, Booking_Date, Pickup_Date, Pickup_Time, Pickup_Location, Dropoff_Location, Taxi_required, Credit_Card_No) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                    (self.customer_name.get(),
                     self.booking_date.get(),
                     self.pickup_date.get(),
                     self.pickup_time.get(),
                     self.pickup_location.get(),
                     self.dropoff_location.get(),
                     self.no_taxis.get(),
                     self.credit_card_no.get()
                    ))
        con.commit() # commit the changes
        messagebox.showinfo("success", "congratulations! booking done successfully", parent=self.root)
        con.close() # close the connection
        
        
    def update(self): # update the booking
        # connecting to the database
        con = mysql.connector.connect(host = 'localhost' ,username = 'root', password = 'xyz', database = 'taxi_database')
        cur=con.cursor()
        cur.execute("UPDATE Booking SET Customer_Name=?, Pickup_Date=?, Pickup_Time=?, Pickup_Location=?, Dropoff_Location=?, Taxi_required=?, Credit_Card_No=? WHERE Booking_ID = ?",
                    (
                     self.customer_name.get(),
                     self.booking_date.get(),
                     self.pickup_date.get(),
                     self.pickup_time.get(),
                     self.pickup_location.get(),
                     self.dropoff_location.get(),
                     self.no_taxis.get(),
                     self.credit_card_no.get()
                    ))
        con.commit() # commit the changes
        messagebox.showinfo("success", "your data is updated", parent=self.root)
        con.close() # close the connection
        

    def delete(self): # delete the booking
        # connecting to the database
        con = mysql.connector.connect(host = 'localhost' ,username = 'root', password = 'xyz', database = 'taxi_database')
        cur=con.cursor()
        op=messagebox.askyesno("Confirm", "Do you want to delete?",parent=self.root)
        if op==True:
            cur.execute("delete from booking_details where Booking_Date=?", (self.booking_date.get(),))
            con.commit() # commit the changes
            messagebox.showinfo("Delete","booking Deleted Successfully",parent=self.root)
            self.clear() # clear the data
            self.show() # show the data
    
 
    def clear(self): # clear the data
        self.customer_name.set(""),                                  
        self.booking_date.set(""),
        self.pickup_date.set(""),
        self.pickup_time.set(""),
        self.pickup_location.set(""),
        self.dropoff_location.set(""),
        self.no_taxis.set(""),
        self.credit_card_no.set("")  
 

    def viewconfirm(self): # view the confirm booking

        self.root2 = Toplevel() # create a new window
        self.root2.title("confirm booking") # title of the window
        self.root2.geometry("1800x800+0+0") # size of the window
        self.root2.focus_force() # focus on the window
        
        #frame
        frame_view=Frame(self.root2, bg="white")
        frame_view.place(x=50, y=20, height=500, width=1200)
        
        #title
        title=Label( frame_view, text="Your Confirm Booking Details", font=("impact", 20, "bold"), bg="white")
        title.place(x=120, y=15)  
        
        #scroollbar
        scrollx=Scrollbar(frame_view,orient=HORIZONTAL) 
        scrolly=Scrollbar(frame_view,orient=VERTICAL)
       
        
        #create tables 
        self.admin_Table=ttk.Treeview(frame_view,columns=("Admin_Id", "Bookingconfirmation_Id","Customer_Name", "Booking_Date","Pickup_Date", "Pickup_Time", "Pickup_Location", "Dropoff_Date", "Dropoff_Location", "Taxi_required", "Driver_Name", "Driver_Licenes_Plate"), yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.admin_Table.xview)
        scrolly.config(command=self.admin_Table.yview)
        
        #heading
        self.admin_Table.heading("admin_id", text="adming ID")
        self.admin_Table.heading("bookingconfirmation_id",text="confirmation ID")
        self.admin_Table.heading("customer_name",text="Customer name")
        self.admin_Table.heading("booking_date",text="Booking date")
        self.admin_Table.heading("pickup_date",text="Pickup date")
        self.admin_Table.heading("pickup_time",text="Pickup time")
        self.admin_Table.heading("pickup_location",text="Pickup address")
        self.admin_Table.heading("dropoff_location",text="Dropoff destination")
        self.admin_Table.heading("no_taxis",text="No of cars required")
        self.admin_Table.heading("driver_name", text="driver name")
        self.admin_Table.heading("driver_licenes_plate", text="driver licences plate")

        self.admin_Table["show"]="headings"
        self.admin_Table.column("admin_id", width=100)
        self.admin_Table.column("bookingconfirmation_id",width=100)
        self.admin_Table.column("customer_name",width=100)
        self.admin_Table.column("booking_date",width=100)
        self.admin_Table.column("pickup_date",width=100)
        self.admin_Table.column("pickup_time",width=100)
        self.admin_Table.column("pickup_location",width=100)
        self.admin_Table.column("dropoff_location",width=100)
        self.admin_Table.column("no_taxis",width=100)
        self.admin_Table.column("driver_name", width=100)
        self.admin_Table.column("driver_licenes_plate", width=100)

        self.admin_Table.pack(fill=BOTH,expand=1) # fill the table
        self.admin_Table.bind("<ButtonRelease-1>",self.get_data1) # get the data
        self.show1() # show the data
        
 
    # def show1(self): # show the data
    #     # connecting to the database
    #     con = mysql.connector.connect(host = 'localhost' ,username = 'root', password = 'xyz', database = 'taxi_database')
    #     cur=con.cursor()
    #     try:
    #         cur.execute("select * from admin_page")
    #         rows=cur.fetchall()
    #         self.admin_Table.delete(*self.admin_Table.get_children()) # delete the data
    #         for row in rows: # insert the data
    #             self.admin_Table.insert('',END,values=row)

    #     except Exception as ex:
    #         messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root) # show the error message
            
    def get_data1(self,ev): # get the data
        f=self.admin_Table.focus() # get the focus
        content=(self.admin_Table.item(f))
        row=content['values']
        self.var_admin_id.set([0]),
        self.var_booking_id.set([1]),
        self.var_customer_name.set(row[2]),
        self.var_booking_date.set(row[3]),
        self.var_pickup_date.set(row[4]),
        self.var_pickup_time.set(row[5]),
        self.var_pickup_address.set(row[6]), # set the data
        self.var_dropoff_destination.set(row[7]),
        self.var_no_of_car_required.set(row[8]),
        self.var_driver_name.set(row[9]),
        self.var_driver_licenes_plate.set(row[10]) # set the data
            
    
        
      
if __name__=="__main__":  
        
    obj = CustBookingSystemClass() # create the object
    mainloop() # run the program
