import tkinter as tk
from  tkinter import ttk
import os, csv

class CustomerWindow:
    def __init__(self, root):
        self.window = tk.Toplevel(root)

        label1 = tk.Label(self.window, text="Welcome To Solent Camper!")
        label1.pack(side=tk.TOP, pady=(20,0))

        label2 = tk.Label(self.window, text="As Customer, You Can View Existing Bookings..")
        label2.pack(side=tk.TOP, pady=(5,0))

        self.showBookings()        

        self.window.title('Customer - Solent Campers')
        self.window.geometry("400x500+400+100")

    def showBookings(self):
        bookingTable = ttk.Treeview(self.window)
        bookingTable['columns'] = ('id', 'camp', 'van', 'region', 'date')

        bookingTable.column("#0", width=0,  stretch=tk.NO)
        bookingTable.column("id", anchor=tk.CENTER, width=80)
        bookingTable.column("camp",anchor=tk.CENTER, width=80)
        bookingTable.column("van",anchor=tk.CENTER, width=80)
        bookingTable.column("region",anchor=tk.CENTER, width=80)
        bookingTable.column("date",anchor=tk.CENTER, width=80)

        bookingTable.heading("#0",text="",anchor=tk.CENTER)
        bookingTable.heading("id",text="Id",anchor=tk.CENTER)
        bookingTable.heading("camp",text="Camp",anchor=tk.CENTER)
        bookingTable.heading("van",text="Van",anchor=tk.CENTER)
        bookingTable.heading("region",text="Region",anchor=tk.CENTER)
        bookingTable.heading("date",text="Date",anchor=tk.CENTER)

        rows = []
        if os.path.isfile('data/bookings.csv'):
            f = open('data/bookings.csv', 'r', newline='', encoding='utf-8')
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                bookingTable.insert(parent='',index='end',iid=0,text='',values=(row[0], row[1], row[2], row[3], row[4]))
            f.close()

            bookingTable.pack(side=tk.TOP)

            for row in rows:
                row.pack(side=tk.TOP)
        else:
            label3 = tk.Label(self.window, text="Sorry! No Bookings Exist. Contact Advisors.")
            label3.pack(side=tk.TOP, pady=(5,0))