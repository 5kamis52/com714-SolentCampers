import tkinter as tk
import tkAvisor
import tkCustomer
import tkAdmin

class MainWindow:
    def __init__(self):
        self.window = tk.Tk()

        label1 = tk.Label(self.window, text="Welcome To Solent Camper!")
        label1.pack(side=tk.TOP, pady=(20,0))

        button1 = tk.Button(self.window, text="Customer", height=5, width=20, command=self.showCustomerWindow)
        button1.pack(side=tk.LEFT, padx=(10, 10))

        button2 = tk.Button(self.window, text="Advisor", height=5, width=20, command=self.showAdvisorWindow)
        button2.pack(side=tk.LEFT, padx=(10, 10))

        button3 = tk.Button(self.window, text="Administrator", height=5, width=20, command=self.showAdminWindow)
        button3.pack(side=tk.LEFT, padx=(10, 10))

        self.window.title('Solent Campers')
        self.window.geometry("500x250+400+150")

    def showAdvisorWindow(self):
        advisorWindow = tkAvisor.AdvisorWindow(self.window)
        advisorWindow.window.mainloop()

    def showCustomerWindow(self):
        customerWindow = tkCustomer.CustomerWindow(self.window)
        customerWindow.window.mainloop()

    def showAdminWindow(self):
        adminWindow = tkAdmin.AdminWindow(self.window)
        adminWindow.window.mainloop()