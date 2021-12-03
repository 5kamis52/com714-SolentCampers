import tkinter as tk
import tkinter.messagebox
from enums import CamperType, CampRegion
import csv, os, classBooking, random
import tkBooking
from datetime import date

class AdvisorWindow:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.grab_set()

        label1 = tk.Label(self.window, text="Welcome To Solent Camper!")
        label1.pack(side=tk.TOP, pady=(20,0))

        label2 = tk.Label(self.window, text="As Advisr, You Can Search For Camping Sites and Vans..")
        label2.pack(side=tk.TOP, pady=(5,0))

        self.regionName = tk.StringVar()
        self.regionName.set(CampRegion.RegionA.name)

        self.vanType = tk.StringVar()
        self.vanType.set(CamperType.Small.name)

        self.campName = tk.StringVar()
        self.campName.set("")

        self.campList = []

        labelvan = tk.Label(self.window, text="Van Type")
        labelvan.pack(side=tk.TOP, pady=(5,0))

        optionVan = tk.OptionMenu(self.window, self.vanType, *[e.name for e in CamperType])
        optionVan.pack(side=tk.TOP)

        labelregion = tk.Label(self.window, text="Region")
        labelregion.pack(side=tk.TOP, pady=(5,0))

        optionRegion = tk.OptionMenu(self.window, self.regionName, *[e.name for e in CampRegion], command=self.campRegionSelected)
        optionRegion.pack(side=tk.TOP)
        
        labelcamp = tk.Label(self.window, text="Camp Name")
        labelcamp.pack(side=tk.TOP, pady=(5,0))

        self.optionCamp = tk.OptionMenu(self.window, self.campName, self.campList)   

        self.bookButton = tk.Button(self.window, text="Book", command=self.saveBooking)

        self.window.title('Advisor - Solent Campers')
        self.window.geometry("400x350+400+100")

    def campRegionSelected(self, region):

        for e in CampRegion:
            if e.name == region:
                region = e.value
                break

        camps = []
        if not os.path.isfile('data/camps.csv'):
            tkinter.messagebox.showerror(master=self.window, title="Sorry", message="Data Files Do Not Exist or are unreadable. Contact Administrator")
            return
        else:
            f = open('data/camps.csv', 'r')
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                if int(row[2]) == region:
                    camps.append(row)

            f.close()

            if not len(camps) == 0:
                self.campList = camps
                self.campName.set(camps[0][1])
                self.displayCampName()
            else:
                tkinter.messagebox.showerror(master=self.window, title="Sorry", message="No Camping Site Added in this region. Contact Administrator.")
                return

    def displayCampName(self):
        menu = self.optionCamp["menu"]
        menu.delete(0, "end")
        for value in self.campList:
            menu.add_command(label=value[1], command=lambda v=value[1]: self.campName.set(v))

        self.optionCamp.pack(side=tk.TOP, pady=(0,30))
        self.bookButton.pack(side=tk.TOP)

    def saveBooking(self):
        bookingID = random.randint(100,999)
        campID = 0
        for camp in self.campList:
            if camp[1] == self.campName.get():
                campID = camp[0]
                
        newBooking = classBooking.Booking(bookingID, campID, self.vanType.get(), self.regionName.get(), date.today())
        newBooking.writeBookingData()

        bookingWindow = tkBooking.BookingWindow(self.window, [bookingID, self.campName.get(), self.vanType.get(), self.regionName.get(), date.today()])