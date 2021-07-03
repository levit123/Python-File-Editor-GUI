from tkinter import *
import tkinter as tk
from tkinter import filedialog
import os
import datetime

#function for letting the user choose the folder containing the files
def chooseFolder(self):
	#user selects the path to the folder
	srcPath = filedialog.askdirectory()
	#sets the variable to the selected path
	self.sourceFolder = srcPath
	#grabs the list of files in the source folder
	fileList = os.listdir(srcPath)
	#clears anything currently in the Listbox widget
	self.fileBox.delete(0, END)
	#inserts the name of each file in the folder into the Listbox widget
	for item in fileList:
		self.fileBox.insert(END, item)

#function for handling the item the user selects in the Listbox widget
def onSelect(self, event):
	#grabs the selected item from the ListBox widget
	fileName = self.fileBox.get(ANCHOR)
	#gets the full path of the file, including the path leading up to the file, and the file name
	fullPath = self.sourceFolder + '/' + fileName

	#gets the creation time of the file in st_ctime format
	ctime = os.stat(fullPath).st_ctime
	#converts the st_ctime to a datetime format
	creationTime = datetime.datetime.fromtimestamp(ctime)
	#clears anything currently in the Entry widget for the date created
	self.detailsDateCreated.delete(0, END)
	#inserts the creation time in the Entry widget
	self.detailsDateCreated.insert(END, creationTime)

	#gets the modification time of the file in mtime format
	mtime = os.path.getmtime(fullPath)
	#converts the mtime to a datetime format
	modTime = datetime.datetime.fromtimestamp(mtime)
	#clears anything currently in the Entry widget for the date modified
	self.detailsDateModified.delete(0, END)
	#inserts the modification time in the Entry widget
	self.detailsDateModified.insert(END, modTime)

	#clears anything currently in the Text widget
	self.txtBox.delete('1.0', END)
	#if the selected file is a .txt file, display the contents of the .txt file in the Text widget
	if fullPath.endswith('.txt'):
		f = open(fullPath, 'r')
		fileText = f.read()
		self.txtBox.insert(END, fileText)