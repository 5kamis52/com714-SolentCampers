import tkinter as tk
from enums import CamperType, CampRegion

class AdminWindow:
    def __init__(self, root):
        self.window = tk.Toplevel(root)  

        self.displayHeader()
        self.displayCampSiteForm()
        self.displayCamperVanForm()

        self.window.title('Administrator - Solent Campers')
        self.window.geometry("400x350+450+100")

    def displayHeader(self):
        headFrame = tk.Frame(self.window, width=400, height=100)
        headFrame.pack(side=tk.TOP, pady=(10,20))

        label1 = tk.Label(headFrame, text="Welcome To Solent Camper!")
        label1.pack(side=tk.TOP)

        label2 = tk.Label(headFrame, text="As Administrator, You Can Add Camps and Vans..")
        label2.pack(side=tk.TOP)

    def displayCampSiteForm(self):
        campFrame = tk.Frame(self.window, width=400, height=120, bg='blue')
        campFrame.pack(side=tk.TOP, pady=(10,20))
        campFrame.pack_propagate(0)

        topFrame = tk.Frame(campFrame, width=400, height=30)
        topFrame.pack(side=tk.TOP)
        topFrame.pack_propagate(0)

        label1 = tk.Label(topFrame, text="Add a Camp Site.")
        label1.pack(side=tk.LEFT, padx=(10,0))

        middleFrame = tk.Frame(campFrame, width=400, height=90)
        middleFrame.pack(side=tk.TOP)
        middleFrame.pack_propagate(0)

        self.campName = tk.StringVar()
        self.campName.set("")

        self.campNameField = tk.Entry(middleFrame, textvariable=self.campName)
        self.campNameField.pack(side=tk.TOP, pady=(00,5))

        self.region = tk.StringVar()
        self.region.set(CampRegion.RegionA.name)

        self.campRegionField = tk.OptionMenu(middleFrame, self.region, *[e.name for e in CampRegion])
        self.campRegionField.pack(side=tk.TOP, pady=(0,5))

        button = tk.Button(middleFrame, text="Add New Site", height=1, width=15, command=self.saveCamp)
        button.pack(side=tk.TOP)


    def displayCamperVanForm(self):
        camperFrame = tk.Frame(self.window, width=400, height=100, bg='green')
        camperFrame.pack(side=tk.TOP, pady=(10,20))

        topFrame = tk.Frame(camperFrame, width=400, height=30)
        topFrame.pack(side=tk.TOP)
        topFrame.pack_propagate(0)

        label1 = tk.Label(topFrame, text="Add a Camper Van.")
        label1.pack(side=tk.LEFT, padx=(10,0))

        middleFrame = tk.Frame(camperFrame, width=400, height=70)
        middleFrame.pack(side=tk.TOP)
        middleFrame.pack_propagate(0)

        self.vanType = tk.StringVar()
        self.vanType.set(CamperType.Small.name)

        self.camperTypeField = tk.OptionMenu(middleFrame, self.vanType, *[e.name for e in CamperType])
        self.camperTypeField.pack(side=tk.TOP, pady=(0,10))

        button = tk.Button(middleFrame, text="Add New Van", height=1, width=15, command=self.saveVan)
        button.pack(side=tk.TOP)

    def saveVan(self):
        print(self.vanType.get())

    def saveCamp(self):
        if self.campName.get() == "":
            print("Camp Name Can't be Empty")
            return 
            
        print(self.campName.get() + " " + self.region.get())