import mysql.connector
import sqlite3 # Import sqlite3

con = mysql.connector.connect(host = 'localhost' ,username = 'root', password = 'Richa@3217', database = 'taxi_database')
cur=con.cursor()
try:
    cur.execute("select * from admin_page")
    rows=cur.fetchall()
    self.admin_Table.delete(*self.admin_Table.get_children()) # delete the data
    for row in rows: # insert the data
        self.admin_Table.insert('',END,values=row)

except Exception as ex:
    messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root) # show the error message
    