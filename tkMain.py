import tkinter as tk

class MainWindow:
    def __init__(self):
        self.window = tk.Tk()

        label1 = tk.Label(text="Welcome To Solent Camper!")
        label1.pack(side=tk.TOP, pady=(20,0))

        button1 = tk.Button(self.window, text="Customer", height=5, width=20)
        button1.pack(side=tk.LEFT, padx=(10, 10))

        button2 = tk.Button(self.window, text="Advisor", height=5, width=20)
        button2.pack(side=tk.LEFT, padx=(10, 10))

        button3 = tk.Button(self.window, text="Administrator", height=5, width=20)
        button3.pack(side=tk.LEFT, padx=(10, 10))

        self.window.title('Solent Campers')
        self.window.geometry("500x250+400+150")