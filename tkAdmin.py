import tkinter as tk

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
        campFrame = tk.Frame(self.window, width=400, height=100, bg='blue')
        campFrame.pack(side=tk.TOP, pady=(10,20))
        campFrame.pack_propagate(0)

        topFrame = tk.Frame(campFrame, width=400, height=30)
        topFrame.pack(side=tk.TOP)
        topFrame.pack_propagate(0)

        label1 = tk.Label(topFrame, text="Add a Camp Site.")
        label1.pack(side=tk.LEFT, padx=(10,0))

        middleFrame = tk.Frame(campFrame, width=400, height=70)
        middleFrame.pack(side=tk.TOP)
        middleFrame.pack_propagate(0)

        self.campNameField = tk.Text(middleFrame, height=1, width=20)
        self.campNameField.pack(side=tk.TOP, pady=(00,5))

        self.campRegionField = tk.Text(middleFrame, height=1, width=20)
        self.campRegionField.pack(side=tk.TOP, pady=(0,10))

        button = tk.Button(middleFrame, text="Add New Site", height=1, width=15)
        button.pack(side=tk.TOP)


    def displayCamperVanForm(self):
        camperFrame = tk.Frame(self.window, width=400, height=80, bg='green')
        camperFrame.pack(side=tk.TOP, pady=(10,20))

        topFrame = tk.Frame(camperFrame, width=400, height=30)
        topFrame.pack(side=tk.TOP)
        topFrame.pack_propagate(0)

        label1 = tk.Label(topFrame, text="Add a Camper Van.")
        label1.pack(side=tk.LEFT, padx=(10,0))

        middleFrame = tk.Frame(camperFrame, width=400, height=50)
        middleFrame.pack(side=tk.TOP)
        middleFrame.pack_propagate(0)

        self.camperTypeField = tk.Text(middleFrame, height=1, width=20)
        self.camperTypeField.pack(side=tk.TOP, pady=(0,10))

        button = tk.Button(middleFrame, text="Add New Van", height=1, width=15)
        button.pack(side=tk.TOP)