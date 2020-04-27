
import os
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askdirectory


import check_files_main
import check_files_gui



def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))

# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        #this closes app
        self.master.destroy()
        os._exit(0)
        
def ask_directory(self):
    folder = askdirectory()
    self.txt_browse1.insert(0,folder)




if __name__ == "__main__":
    pass
    
