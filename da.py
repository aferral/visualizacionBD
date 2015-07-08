from Tkinter import *
from tkintertable.Tables import TableCanvas
from tkintertable.TableModels import TableModel
import tkFileDialog, tkMessageBox, tkSimpleDialog
import tkFont
import math, time
import os, types
import string, copy
import platform

class App:
    def __init__(self, master):
        self.main = Frame(master)
        self.main.pack(fill=BOTH,expand=1)
        master.geometry('600x400+200+100')

root = Tk()
app = App(root)
master = app.main
model = TableModel()
data = {'fila': {'col22':22,'col2':245,'col3':587,'col4':999},'fila2':{'col1':223,'col2':44,'col3':55,'col4':66}}
model.importDict(data)
table = TableCanvas(master, model,
                    cellwidth=60, cellbackgr='#e3f698',
                    thefont=('Arial',12),rowheight=18, rowheaderwidth=30,
                    rowselectedcolor='yellow', editable=True)
table.createTableFrame()

root.mainloop()