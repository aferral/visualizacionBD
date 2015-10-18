# -*- coding: cp1252 -*-
import Pmw

import VentanaExtra
from ventanasEdicion import ventanaEditarPaciente
import editRadio
import editAntecedentes
from librerias.SearchCriteria import *

from patronesRecurrentes import filtrarPaciente

from librerias.querys.queryList import *
from ventanasEdicion.DatosRadio import vistaRadio
from ventanasEdicion.modeloAntecedentes import vistaAntecedentes


class Demo:
    def __init__(self, parent):
        self.currentIdRadio = None
        self.parent = parent


        Pmw.aboutversion('1.0')
        Pmw.aboutcopyright('Copyright UchileDB\nAll rights reserved')
        Pmw.aboutcontact(
            'Contacto :\n' +
            '  Informacion de contacto\n' +
            '  Phone: +995096669\n' +
            '  email: andreslago5@hotmail.com\n' +
            '  aferral and argorthas'
        )
        self.about = Pmw.AboutDialog(parent, applicationname = 'My Application')
        self.about.withdraw()


        #################################################

        # Create the Balloon for this toplevel.
        self.balloon = Pmw.Balloon(parent)

        # Create and install the MenuBar.
        menuBar = Pmw.MainMenuBar(parent,
                balloon = self.balloon)
        parent.configure(menu = menuBar)
        self.menuBar = menuBar

        # Add some buttons to the MainMenuBar.
        menuBar.addmenu('Create', 'Close this window or exit')
        menuBar.addmenuitem('Create', 'command', 'Exit the application',
                command = self.createVentanaPaciente,
                label = 'Paciente')

        menuBar.addmenu('Edit','asd')
        menuBar.addmenuitem('Edit', 'command', 'Delete the current selection',
                command = lambda: self.newWindow("Medicamento",
                                                 queryAddMedicamento,queryDeleteMedicamento,
                                                 queryUpdateMedicamento,queryListaMedicamento,
                                                 self.actualizaListas),
                label = 'Medicamento')

        menuBar.addmenuitem('Edit', 'command', 'Delete the current selection',
                command = lambda: self.newWindow("Alergia",queryAddAlergia,
                                                 queryDeleteAlergia,
                                                 queryUpdateAlergia,
                                                 queryListaAlergia,
                                                 self.actualizaListas),
                label = 'Alergia')
        menuBar.addmenuitem('Edit', 'command', 'Delete the current selection',
                command = lambda: self.newWindow("Droga",queryAddDroga,
                                                 queryDeleteDroga,
                                                 queryUpdateDroga,
                                                 queryListaDroga,
                                                 self.actualizaListas),
                label = 'Droga')
        menuBar.addmenuitem('Edit', 'separator')
        menuBar.addmenuitem('Edit', 'command', 'Delete the current selection',
                command = self.editRadio,
                label = 'Radio')
        menuBar.addmenuitem('Edit', 'command', 'Delete the current selection',
                command = self.editAntecedentes,
                label = 'Antecedentes')
        
        menuBar.addmenuitem('Edit', 'separator')
        menuBar.addmenuitem('Edit', 'command', 'Delete the current selection',
                command = lambda: self.newWindow("Procedencia",
                                                 queryAddProce,queryDeleteProce,
                                                 queryUpdateProce,queryListaProce,
                                                 self.actualizaListas),
                label = 'Procedencia')
        menuBar.addmenuitem('Edit', 'command', 'Delete the current selection',
                command = lambda: self.newWindow("Zona",
                                                 queryAddZona,queryDeleteZona,
                                                 queryUpdateZona,queryListaZona,
                                                 self.actualizaListas),
                label = 'Zona')
        menuBar.addmenuitem('Edit', 'command', 'Delete the current selection',
                command = lambda: self.newWindow("Tipo",
                                                 queryAddTipo,queryDeleteTipo,
                                                 queryUpdateTipo,queryListaTipo,
                                                 self.actualizaListas),
                label = 'Tipo')
        menuBar.addmenuitem('Edit', 'separator')
        menuBar.addmenuitem('Edit', 'command', 'Delete the current selection',
                command = lambda: self.newWindow("Tipo",
                                                 queryAddEnfermedad,queryDeleteEnfermedad,
                                                 queryUpdateEnfermedad,queryListaEnfermedad,
                                                 self.actualizaListas),
                label = 'Enfermedad')


        menuBar.addmenu('Help', 'Set user preferences')
        menuBar.addmenuitem('Help', 'command', 'Set general preferences',
                command = self.execute,
                label = 'About')




        #############################################################################

        
        # Create and pack the NoteBook.
        self.notebook = Pmw.NoteBook(parent)
        self.notebook.pack(fill = 'both', expand = 1, padx = 10, pady = 10)

        # Add the "Gemeral" page to the notebook.
        self.page = self.notebook.add('General')
        self.notebook.tab('General').focus_set()

        # Create the "Paciente" contents of the page.
        self.group = Pmw.Group(self.page, tag_text = 'Filtrar personas por RUT :')
        self.group.pack()


        Label(self.group.interior(),
            text = 'RUT sin codigo ver:').grid(row=0,column=0,sticky=W, padx=5, pady=5)
        self.runentry = Entry(self.group.interior())
        self.runentry.grid(row=0,column=1)

        # Create the "Radiografia" contents of the page.
        self.group1 = Pmw.Group(self.page, tag_text = 'Radiografia \nTodos los campos son obligatorios')
        self.group1.pack()

        #---------------Aqui estan las radiografias------------------------------

        self.vistaRadio = vistaRadio(self.group1)

        #Button "Filtro"
        Button(self.group.interior(),text="Filtrar",command= lambda: filtrarPaciente(
            self.runentry,self.vistaRadio.getWidget('PacienteCombo'),None)
               ).grid(row=0,column=2,sticky=W, padx=5, pady=5)

        #Aqui van los antecedentes y la nueva pagina
        # Add another page
        self.page1 = self.notebook.add('Antecedentes')

        self.groupAntecedentes = Pmw.Group(self.page1, tag_text = 'Antecedentes')
        self.groupAntecedentes.pack(fill = 'both', expand = 1, padx = 10, pady = 10)

        #---------------Aqui estan los antecedentes ------------------------------
        self.vistaAntece = vistaAntecedentes(self.groupAntecedentes)

        self.notebook.setnaturalsize()

        self.statusValue = StringVar()
        self.statusValue.set("Status:")
        self.status = Label(parent,textvariable=self.statusValue).pack()


        # Create and pack the ButtonBox.
        self.buttonBox = Pmw.ButtonBox(parent,
                labelpos = 'w',
                label_text = '                                                                                           ',
                frame_borderwidth = 2,
                frame_relief = 'groove')
        self.buttonBox.pack(fill = 'both', expand = 1, padx = 10, pady = 10)

        # Add some buttons to the ButtonBox.
        self.buttonBox.add('Crear', command = self.crearRadiografia)

        # Make all the buttons the same width.
        self.buttonBox.alignbuttons()
        self.actualizaListas()

    def getCurrentIdRadio(self):
        return self.currentIdRadio
    def setCurrentIdRadio(self,newId):
        self.currentIdRadio = newId

    def crearRadiografia(self):

        #Creacion de Radiografia segun su modelo de datos
        try:
            self.setCurrentIdRadio(self.vistaRadio.crearRadio())
            #-------Comienza agregar antecedentes
            self.vistaAntece.createFromId(self.getCurrentIdRadio())
        except Exception,e:
            print str(e)



    def actualizaListas(self): #Actualiza enfermedades, medicamentos, alergias, procedencias

        #Actualiza datos que consiernen a radiografia
        self.vistaRadio.update()
        #Actualiza listas de antecedentes
        self.vistaAntece.update()

        pass

    def newWindow(self, tipo, queryAdd, queryDelet, queryEdit, queryLista,updateFunction):
        t = Tkinter.Toplevel(self.parent)
        ventana = VentanaExtra.Demo(t,tipo, queryAdd, queryDelet, queryEdit,queryLista,updateFunction)
        pass
    
    def execute(self):
        self.about.show()


    ####################################################

    def createVentanaPaciente(self):
        t = Tkinter.Toplevel(self.parent)
        ventana = ventanaEditarPaciente.Demo(t)
        pass
    
    def editAntecedentes(self):
        t = Tkinter.Toplevel(self.parent)
        ventana = editAntecedentes.Demo(t)
        pass
    
    def editRadio(self):
        t = Tkinter.Toplevel(self.parent)
        ventana = editRadio.Demo(t)
        pass
    
    #####################################################



root = Tkinter.Tk()
demo = Demo(root)
root.mainloop()
