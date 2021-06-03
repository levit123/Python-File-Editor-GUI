from tkinter import *
import tkinter as tk
from tkinter import filedialog
import os
import datetime

def chooseFolder(self):
	srcPath = filedialog.askdirectory()
	fileList = os.listdir(srcPath)
	for item in fileList:
		self.fileBox.insert(END, item)

def onSelect(self, event):
	varList = event.widget
	select = varList.curselection()[0]
	value = varList.get(select)