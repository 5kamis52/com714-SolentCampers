import tkMain
import os


# create data directory if not exist
if not os.path.exists('data'):
    os.mkdir('data')

#start main program
mainWindow = tkMain.MainWindow()
mainWindow.window.mainloop()