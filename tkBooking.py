import tkinter as tk

class BookingWindow:
    def __init__(self, root, data):
        self.window = tk.Toplevel(root)
        self.window.grab_set()

        label1 = tk.Label(self.window, text="Welcome To Solent Camper!")
        label1.pack(side=tk.TOP, pady=(20,0))

        label2 = tk.Label(self.window, text="Booking Summary")
        label2.pack(side=tk.TOP, pady=(5,0))

        label3 = tk.Label(self.window, text="Booking ID: " + str(data[0]))
        label3.pack(side=tk.TOP, pady=(20,5))

        label3 = tk.Label(self.window, text="Booking Date: " + str(data[4]))
        label3.pack(side=tk.TOP, pady=(0,5))

        label4 = tk.Label(self.window, text="Camp Name: " + str(data[1]))
        label4.pack(side=tk.TOP, pady=(0,5))

        label4 = tk.Label(self.window, text="Region: " + str(data[2]))
        label4.pack(side=tk.TOP, pady=(0,5))

        label4 = tk.Label(self.window, text="Camper Van Type: " + str(data[3]))
        label4.pack(side=tk.TOP, pady=(0,5))


        self.window.title('Booking Summary - Solent Campers')
        self.window.geometry("400x350+400+100")
