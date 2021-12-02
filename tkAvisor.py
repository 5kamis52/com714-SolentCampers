import tkinter as tk
from enums import CamperType, CampRegion
class AdvisorWindow:
    def __init__(self, root):
        self.window = tk.Toplevel(root)

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

        labelvan = tk.Label(self.window, text="Van Type")
        labelvan.pack(side=tk.TOP, pady=(5,0))

        optionVan = tk.OptionMenu(self.window, self.vanType, *[e.name for e in CamperType])
        optionVan.pack(side=tk.TOP)

        labelregion = tk.Label(self.window, text="Region")
        labelregion.pack(side=tk.TOP, pady=(5,0))

        optionRegion = tk.OptionMenu(self.window, self.regionName, *[e.name for e in CampRegion])
        optionRegion.pack(side=tk.TOP)

        self.window.title('Advisor - Solent Campers')
        self.window.geometry("400x500+400+100")