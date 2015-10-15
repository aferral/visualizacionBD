__author__ = 'aferral'
from Tkinter import *
import ttk
from copy import copy

#Esto permite hacer plantillas de widgets, guarda sus instrucciones de creacion y los recrea. Tambien tiene diccionario
#para sacar valores facil y actualizacion

class Contenedor(Frame):
    def __init__(self, master=None):
        self.master = master;
        Frame.__init__(self,master)
        self.dict = {}
        self.inside = []
        self.inst = []
        pass
    def add(self,widgetClass,palabra,modo, *args, **kwargs): #Las maravillas de python
        #Lo retorno si lo quieres gridear SE GRIDEA RESPECTO A ESTO SI (Es un frame)
        temp = widgetClass(self, *args, **kwargs)
        self.dict[palabra] = temp
        self.inside.append(temp)
        self.inst.append((widgetClass,palabra,modo,args,kwargs))
        return temp

        pass
    def get(self,palabra):
        return self.dict[palabra].get()
    def update(self,palabra,lista):
        elem = self.dict[palabra]
        if isinstance(elem,ttk.Combobox):
            elem['values'] = tuple(lista)
        pass
    def clone(self,where):
        temp = Contenedor(where)
        c=0

        for (widgetClass,palabra,modo,args,kwargs) in self.inst:
            widget = temp.add(widgetClass,palabra,modo,*args,**kwargs)
            widget.grid(row=0,column=c)
            c+=1
            pass
        return temp

