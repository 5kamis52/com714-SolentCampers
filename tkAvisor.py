import tkinter as tk

class AdvisorWindow:
    def __init__(self, root):
        self.window = tk.Toplevel(root)

        label1 = tk.Label(text="Welcome To Solent Camper!")
        label1.pack(side=tk.TOP, pady=(20,0))

        label2 = tk.Label(text="As Advisr, You Can Search For Camping Sites and Vans..")
        label2.pack(side=tk.TOP, pady=(5,0))

        self.window.title('Advisor - Solent Campers')
        self.window.geometry("400x500+400+100")