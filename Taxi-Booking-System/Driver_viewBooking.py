from tkinter import * # import all from tkinter module
import sqlite3 # import sqlite3 module
from tkinter import ttk, messagebox # import ttk and messagebox from tkinter
import mysql.connector # import mysql.connector
from tkinter.ttk import Style, Treeview # import style and treeview from tkinter.ttk
from PIL import Image, ImageTk # import image and imageTk from PIL
import PIL # import PIL

class DriverVieBookingClass():
    def __init__(self):
        root=Tk()  
        self.root=root
        self.root.title("Driver's View Booking System")
        self.root.geometry("1800x700+0+0")

        self.bg=ImageTk.PhotoImage(file="images\path.png")
        self.bg_image=Label(self.root, image=self.bg).pack(side=TOP)
        
    
        self.admin_id=StringVar()
        self.booking_id=StringVar()
        self.customer_name=StringVar()
        self.booking_date=StringVar()
        self.pickup_date=StringVar()
        self.pickup_time=StringVar()
        self.pickup_address=StringVar()
        self.dropoff_destination=StringVar()
        self.no_of_car_required=StringVar()
        self.driver_name=StringVar()
        self.driver_licenes_plate=StringVar()
        
        ##### LABEL 
        label=Label(self.root, text="Booking List", font=("georgia", 20), fg="dark red").place(x=550, y=40)
        label=Label(self.root, text="Have a nice day and safe trip!", font=("georgia", 20), fg="dark red").place(x=470, y=80)
        
        #showing details 
        #frame
        frame_view=Frame(self.root, bg="white")
        frame_view.place(x=50, y=150, height=500, width=1200)
        
        #title
        style = Style()

        style.theme_use('default')
        
        style.configure("frame_view",
        background="grey",  
        foreground="black",
        rowheight=30,
        fieldbackground="grey")
        
        Heading = Label(frame_view, text= 'Your Booking Details', font= 'georgia 20', bg='#E7AB79')
        Heading.place(x=760, y=0,width=350) 
        
        scrolly=Scrollbar(frame_view,orient=VERTICAL)
        scrollx=Scrollbar(frame_view,orient=HORIZONTAL) 
        
        
        #create tables 
        self.admin_Table=ttk.Treeview(frame_view,columns=("admin_id","customer_name","pickup_date", "pickup_time", "pickup_location", "dropoff_location", "no_taxis", "driver_name", "driver_licenes_plate"), yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
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
        
    def show(self):
        con = mysql.connector.connect(host = 'localhost' ,username = 'root', password = 'xyz', database = 'taxi_database')
        cur=con.cursor()
        try:
            cur.execute("select * from admin_page")
            rows=cur.fetchall()
            self.admin_Table.delete(*self.admin_Table.get_children())
            for row in rows:
                self.admin_Table.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            
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
      
if __name__=="__main__":  
        
    obj=DriverVieBookingClass()
    mainloop()
