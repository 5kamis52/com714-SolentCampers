import tkinter as tk

class CustomerWindow:
    def __init__(self, root):
        self.window = tk.Toplevel(root)

        label1 = tk.Label(self.window, text="Welcome To Solent Camper!")
        label1.pack(side=tk.TOP, pady=(20,0))

        label2 = tk.Label(self.window, text="As Customer, You Can View Existing Bookings..")
        label2.pack(side=tk.TOP, pady=(5,0))

        self.window.title('Customer - Solent Campers')
        self.window.geometry("400x500+400+100")