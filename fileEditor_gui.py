from tkinter import *
import tkinter as tk
from tkinter import filedialog
import os

import fileEditor_func

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #setting the Frame configuration
        self.master = master
        #gives the GUI frame a title
        self.master.title("File Editor")
        #defines the width, height, x-position and y-position of the GUI frame
        self.master.geometry('800x500+500+200')

        #Label for the Listbox widget
        self.fileBoxLbl = tk.Label(self.master, text="List of text files", font=('Arial', 14))
        self.fileBoxLbl.grid(row=0, column=0, pady=10)
        #Listbox widget that lists the files in the source directory
        self.fileBox = tk.Listbox(self.master, width=30, bd=2, activestyle="none", exportselection=0)
        self.fileBox.grid(row=1, column=0, padx=20, stick=N)
        #calls the "onSelect" function, displaying the info for the currently selected item
        self.fileBox.bind('<<ListboxSelect>>', lambda event: fileEditor_func.onSelect(self, event))

        #Button widget for choosing source directory
        self.saveBtn = tk.Button(self.master, width=15, text="Save To File")
        self.saveBtn.grid(row=2, column=1, pady=10)

        #Label for the Text widget
        self.txtBoxLbl = tk.Label(self.master, text="Text Editor", font=('Arial', 14))
        self.txtBoxLbl.grid(row=0, column=1, pady=10)
        #Entry widget for editing the contents of a .txt file
        self.txtBox = tk.Text(self.master, width=40, height=10, bd=2)
        self.txtBox.grid(row=1, column=1, stick=N)

        #Button widget for choosing source directory
        self.sourceBtn = tk.Button(self.master,width=12, text="Choose Folder", command=lambda:fileEditor_func.chooseFolder(self))
        self.sourceBtn.grid(row=2, column=0, pady=10)

        #Label above the "detailsDateCreated" Label
        self.detailsDateCreatedLbl = tk.Label(self.master, text="Date Created", font=('Arial underline', 12))
        self.detailsDateCreatedLbl.grid(row=3, column=0, padx=20, pady=10)
        #Label that holds the date the file was created
        self.detailsDateCreated = tk.Entry(self.master, width=20)
        self.detailsDateCreated.grid(row=4, column=0, padx=20, pady=10)

        #Label above the "detailsDateModified" Label
        self.detailsDateModifiedLbl = tk.Label(self.master, text="Date Modified", font=('Arial underline', 12))
        self.detailsDateModifiedLbl.grid(row=5, column=0, padx=10, pady=10)
        #Label that holds the date the file was created
        self.detailsDateModifiedLbl = tk.Entry(self.master, width=20)
        self.detailsDateModifiedLbl.grid(row=6, column=0, padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
