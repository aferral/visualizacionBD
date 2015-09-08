# -*- coding: cp1252 -*-
import Tkinter
import Pmw
from Tkinter import *
import ttk
from Calendar import *
import VentanaExtra


import psycopg2

class Demo:
    def __init__(self, parent):
        
        self.parent = parent


        #################################################

        # Create the Balloon for this toplevel.
        self.balloon = Pmw.Balloon(parent)

        # Create and install the MenuBar.
        menuBar = Pmw.MainMenuBar(parent,
                balloon = self.balloon)
        parent.configure(menu = menuBar)
        self.menuBar = menuBar

        # Add some buttons to the MainMenuBar.
        menuBar.addmenu('File', 'Close this window or exit')
        menuBar.addmenuitem('File', 'command', 'Close this window',
                command = PrintOne('Action: close'),
                label = 'Close')
        menuBar.addmenuitem('File', 'separator')
        menuBar.addmenuitem('File', 'command', 'Exit the application',
                command = PrintOne('Action: exit'),
                label = 'Exit')

        menuBar.addmenu('Edit','asd')
        menuBar.addmenuitem('Edit', 'command', 'Delete the current selection',
                command = lambda: self.newWindow("Medicamento"),
                label = 'Medicamento')
        menuBar.addmenuitem('Edit', 'command', 'Delete the current selection',
                command = lambda: self.newWindow("Alergia"),
                label = 'Alergia')
        menuBar.addmenuitem('Edit', 'command', 'Delete the current selection',
                command = lambda: self.newWindow("Droga"),
                label = 'Droga')

        menuBar.addmenu('Options', 'Set user preferences')
        menuBar.addmenuitem('Options', 'command', 'Set general preferences',
                command = PrintOne('Action: general options'),
                label = 'General...')




        #############################################################################




        
        # Create and pack the NoteBook.
        self.notebook = Pmw.NoteBook(parent)
        self.notebook.pack(fill = 'both', expand = 1, padx = 10, pady = 10)

        # Add the "Gemerañ" page to the notebook.
        self.page = self.notebook.add('General')
        self.notebook.tab('General').focus_set()

        # Create the "Paciente" contents of the page.
        self.group = Pmw.Group(self.page, tag_text = 'Paciente')
        self.group.pack(fill = 'both', expand = 1, padx = 10, pady = 10)

        self.varCheckRut = IntVar()
        Checkbutton(self.group.interior(), variable=self.varCheckRut).grid(row=0,column=0)
        self.run = Label(self.group.interior(), 
            text = 'RUT:').grid(row=0,column=1,sticky=W, padx=5, pady=5)
        self.runentry = Entry(self.group.interior())
        self.runentry.grid(row=0,column=2)
        
        self.varCheckNombre = IntVar()
        Checkbutton(self.group.interior(), variable=self.varCheckNombre).grid(row=1,column=0)
        self.nombre = Label(self.group.interior(), 
            text = 'Nombre:')
        self.nombre.grid(row=1,column=1,sticky=W, padx=5, pady=5)
        self.nombreentry = Entry(self.group.interior())
        self.nombreentry.grid(row=1,column=2)


        #Button "Filtro"
        self.filtrar = Button(self.group.interior(),text="Filtrar",
                            command= self.filtrar).grid(row=1,column=3,sticky=W, padx=5, pady=5)

        self.varSexo = IntVar()
        Checkbutton(self.group.interior(), variable=self.varSexo).grid(row=2,column=0)
        self.sexo= Label(self.group.interior(), 
            text="Sexo:").grid(row=2,column=1,sticky=W, padx=5, pady=5)
        self.boolsexo = IntVar()
        self.radiobuttonm=Radiobutton(self.group.interior(), text="M", variable=self.boolsexo, value=1).grid(row=2,column=2,sticky=W)
        self.radiobuttonh=Radiobutton(self.group.interior(), text="H", variable=self.boolsexo, value=2).grid(row=2,column=2,sticky=E)

        self.varFechaNac = IntVar()
        Checkbutton(self.group.interior(), variable=self.varFechaNac).grid(row=3,column=0)
        self.fechanac= Label(self.group.interior(), text="FechaNac:").grid(row=3,column=1,sticky=W, padx=5, pady=5)
        self.varF0 = StringVar()
        self.varF0.set('Today')

        self.fechanacdate= Label(self.group.interior(), textvariable = self.varF0).grid(row=3,column=2,sticky=W, padx=5, pady=5)
        self.datechange0 = Button(self.group.interior(),text="Cambiar",
                            command= lambda: self.createWindowsAndBind(self.updateF0))
        self.datechange0.grid(row=3,column=1,sticky=E, padx=5, pady=5)

        self.crearPaciente = Button(self.group.interior(),text="Crear",
                            command= self.crear).grid(row=4,column=2,sticky=E, padx=5, pady=5)
                
        
        
        

        # Create the "Radiografia" contents of the page.
        self.group1 = Pmw.Group(self.page, tag_text = 'Radiografia')
        self.group1.pack(fill = 'both', expand = 1, padx = 10, pady = 10)

        self.paciente= Label(self.group1.interior(), text="Paciente:").grid(row=0,column=0,sticky=W, padx=5, pady=5)
        self.pacienteValue = StringVar()
        self.pacienteCombo = ttk.Combobox(self.group1.interior(), textvariable=self.pacienteValue,
                                state='readonly')
        self.pacienteCombo['values'] = ()
        self.pacienteCombo.grid(row=0,column=1)
        
        
        self.ids = Label(self.group1.interior(), 
            text = 'Id:').grid(row=1,column=0,sticky=W, padx=5, pady=5)
        self.idsentry = Entry(self.group1.interior())
        self.idsentry.grid(row=1,column=1)

        self.frame = Label(self.group1.interior(), 
            text = 'Frames:').grid(row=2,column=0,sticky=W, padx=5, pady=5)
        self.frameentry = Entry(self.group1.interior()).grid(row=2,column=1)
        
        
        self.enfermedad= Label(self.group1.interior(), text="Enfermedad:").grid(row=3,column=0,sticky=W, padx=5, pady=5)
        self.enfermedadValue = StringVar()
        self.enfermedadCombo = ttk.Combobox(self.group1.interior(), textvariable=self.enfermedadValue,
                                state='readonly')
        self.enfermedadCombo['values'] = ('Enfermedad1', 'Enfermedad2', 'Enfermedad3', 'Enfermedad4')
        self.enfermedadCombo.current(0)
        self.enfermedadCombo.grid(row=3,column=1)

        # Create and pack the dropdown ComboBox.
        self.zona= Label(self.group1.interior(), text="Zona:").grid(row=4,column=0,sticky=W, padx=5, pady=5)
        self.zonaValue = StringVar()
        self.zonaCombo = ttk.Combobox(self.group1.interior(), textvariable=self.zonaValue,
                                state='readonly')
        self.zonaCombo['values'] = ('cornsilk1', 'snow1', 'seashell1', 'antiquewhite1')
        self.zonaCombo.current(0)
        self.zonaCombo.grid(row=4,column=1)

        


        
       # Create and pack the dropdown ComboBox.
        self.tipo= Label(self.group1.interior(), text="Tipo:").grid(row=5,column=0,sticky=W, padx=5, pady=5)
        self.tipoValue = StringVar()
        self.tipoCombo = ttk.Combobox(self.group1.interior(), textvariable=self.tipoValue,
                                state='readonly')
        self.tipoCombo['values'] = ('Radiografia', 'Escaner', 'Resonancia')
        self.tipoCombo.current(0)
        self.tipoCombo.grid(row=5,column=1)

        self.fecha= Label(self.group1.interior(), text="Fecha").grid(row=6,column=0,sticky=W, padx=5, pady=5)
        self.varF1 = StringVar()
        self.varF1.set('Today')
        self.fechadate= Label(self.group1.interior(), textvariable = self.varF1).grid(row=6,column=1,sticky=W, padx=5, pady=5)
        self.datechange1 = Button(self.group1.interior(),text="Cambiar",
                            command= lambda: self.createWindowsAndBind(self.updateF1)).grid(row=6,column=1,sticky=E, padx=5, pady=5)

        self.procedencia= Label(self.group1.interior(), text="Procedencia:").grid(row=7,column=0,sticky=W, padx=5, pady=5)
        self.procedenciaValue = StringVar()
        self.procedenciaCombo = ttk.Combobox(self.group1.interior(), textvariable=self.procedenciaValue,
                                state='readonly')
        self.procedenciaCombo['values'] = ('Ambulatorio', 'procedencia1', 'procedencia2')
        self.procedenciaCombo.current(0)
        self.procedenciaCombo.grid(row=7,column=1)

        
        self.comentario0 = Label(self.group1.interior(), 
                text = 'Comentario:').grid(row=8,column=0,sticky=W, padx=5, pady=5)
        self.comentarioentry0 = Entry(self.group1.interior()).grid(row=8,column=1)

        


        # Add another page
        self.page1 = self.notebook.add('Antecedentes')

        # Create the "Antecedentes" contents of the page.
        self.group2 = Pmw.Group(self.page1, tag_text = 'Antecedentes')
        self.group2.pack(fill = 'both', expand = 1, padx = 10, pady = 10)

        self.var1 = IntVar()
        Checkbutton(self.group2.interior(), variable=self.var1).grid(row=0,column=0,sticky=W, padx=5, pady=5)
        
        self.trabajo = Label(self.group2.interior(), 
                text = 'Trabajo:').grid(row=0,column=1,sticky=W, padx=5, pady=5)
        self.trabjoentry = Entry(self.group2.interior()).grid(row=0,column=2)


        self.var2 = IntVar()
        Checkbutton(self.group2.interior(), variable=self.var2).grid(row=1,column=0,sticky=W, padx=5, pady=5)
        
        self.medicamentos= Label(self.group2.interior(), text="Medicamentos:").grid(row=1,column=1,sticky=W, padx=5, pady=5)
        self.medicamentoValue = StringVar()
        self.medicamentoCombo = ttk.Combobox(self.group2.interior(), textvariable=self.medicamentoValue,
                                state='readonly')
        self.medicamentoCombo['values'] = ('ibuprofeno','etc')
        self.medicamentoCombo.current(0)
        self.medicamentoCombo.grid(row=1,column=2)


        self.var3 = IntVar()
        Checkbutton(self.group2.interior(), variable=self.var3).grid(row=2,column=0,sticky=W, padx=5, pady=5)
        
        self.alergia= Label(self.group2.interior(), text="Alergias:").grid(row=2,column=1,sticky=W, padx=5, pady=5)
        self.alergiaValue = StringVar()
        self.alergiaCombo = ttk.Combobox(self.group2.interior(), textvariable=self.alergiaValue,
                                state='readonly')
        self.alergiaCombo['values'] = ('bichos','etc')
        self.alergiaCombo.current(0)
        self.alergiaCombo.grid(row=2,column=2)


        self.var4 = IntVar()
        Checkbutton(self.group2.interior(), variable=self.var4).grid(row=3,column=0,sticky=W, padx=5, pady=5)
        
        self.adiccion= Label(self.group2.interior(), text="Adiccion:").grid(row=3,column=1,sticky=W, padx=5, pady=5)
        self.adiccionValue = StringVar()
        self.adiccionCombo = ttk.Combobox(self.group2.interior(), textvariable=self.adiccionValue,
                                state='readonly')
        self.adiccionCombo['values'] = ('PastaBase','etc')
        self.adiccionCombo.current(0)
        self.adiccionCombo.grid(row=3,column=2)

        
        self.comentario1 = Label(self.group2.interior(), 
                text = 'Comentario:').grid(row=4,column=1,sticky=W, padx=5, pady=5)
        self.comentarioentry1 = Entry(self.group2.interior()).grid(row=4,column=2)
        

        self.group3 = Pmw.Group(self.page1, tag_text = 'Intervenciones')
        self.group3.pack(fill = 'both', expand = 1, padx = 10, pady = 10)

        self.var5 = IntVar()
        Checkbutton(self.group3.interior(), variable=self.var5).grid(row=0,column=0,sticky=W, padx=5, pady=5)
        

        self.fechaint = Label(self.group3.interior(), 
                text = 'Fecha:').grid(row=0,column=1,sticky=W, padx=5, pady=5)
        self.varF2 = StringVar()
        self.varF2.set('Today')
        self.fechaintdate= Label(self.group3.interior(), textvariable = self.varF2).grid(row=0,column=1,sticky=W, padx=5, pady=5)
        self.fechaintbutton = Button(self.group3.interior(),text="Cambiar",
                            command= lambda: self.createWindowsAndBind(self.updateF2)).grid(row=0,column=2,sticky=E, padx=5, pady=5)

        self.nombreop = Label(self.group3.interior(), 
                text = 'Nombre Intervencion:').grid(row=1,column=1,sticky=W, padx=5, pady=5)
        self.nombreopentry = Entry(self.group3.interior()).grid(row=1,column=2)

        self.doc = Label(self.group3.interior(), 
                text = 'Doctor:').grid(row=2,column=1,sticky=W, padx=5, pady=5)
        self.docentry = Entry(self.group3.interior()).grid(row=2,column=2)

        self.notebook.setnaturalsize()

        self.statusValue= StringVar()
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
        self.buttonBox.add('Crear', command = self.genesisdetodo)


        # Make all the buttons the same width.
        self.buttonBox.alignbuttons()


        self.checkboxes=[self.var1,self.var2,self.var3,self.var4,self.var5]

        self.actualizaListas()

    def callback(self, tag):
        # This is called whenever the user clicks on a button
        # in a single select RadioSelect widget.
        print 'Button', tag, 'was pressed.'

    def updateF0(self,x):
        self.varF0.set(x.strftime('%Y-%m-%d'))
        return

    def updateF1(self,x):
        self.varF1.set(x.strftime('%Y-%m-%d'))
        return

    def updateF2(self,x):
        self.varF2.set(x.strftime('%Y-%m-%d'))
        return

    def createWindowsAndBind(self,fun):
        print fun
        sf = SecondFrame(Tkinter.Toplevel())
        sf.setCallback(fun)

    def genesisdetodo(self):
        print 'You play to be GOD'
        #filtrar por los checkboxes
        #self.var1,self.var2,self.var3,self.var4,self.var5 son los Tkinter.IntVar() :D
        #hacer el filtro de que se crea
        for var in self.checkboxes:
            print var.get()


        query = 'INSERT INTO "Radiografia"("IdRadio", "Fecha", "Zona", "Procedencia", ' \
                '"Tipo", "Comentario", "RUNPaciente", "NombrePaciente") VALUES (%s, %s, %s, %s, %s, %s, %s, %s);'
        params = (str(self.idsentry.get()),str(self.varF1.get()),str(self.zonaValue.get()),str(self.procedenciaValue.get()),
                  str(self.tipoValue.get()),str("Esto es comentaro")
                  ,str(self.pacienteValue.get().split(",")[1]),str(self.pacienteValue.get().split(",")[0]),)
        askDb(query,params)

    def filtrar(self):
        #crea al paciente
        varSexo = 'M'
        if self.varSexo.get():
            print "Filtro por sexo activado"
            varSexo = 'M'
            if self.boolsexo.get() == 1:
                varSexo = 'H'
        print "Se esta creando al nuevo Paciente"
        print "Agregando con rut ",self.runentry.get()
        print "nombre ",self.nombreentry.get()
        print "Sexo ",self.boolsexo.get()
        print "FechaNac ",self.varF0.get()


        query6 = 'SELECT "Nombre","RUN" FROM "Paciente" WHERE "Sexo" = %s ORDER BY RANDOM() LIMIT 40 '
        listRes = askDb(query6,(str(varSexo),))
        for i in range(len(listRes)):
            listRes[i] = listRes[i][0]+","+str(listRes[i][1])
        self.pacienteCombo['values'] = tuple(listRes)
        self.pacienteCombo.current(0)

    def crear(self):

        #crea al paciente
        varSexo = 'M'
        if self.boolsexo.get() == 1:
            varSexo = 'H'
        print "Se esta creando al nuevo Paciente"
        print "Agregando con rut ",self.runentry.get()
        print "nombre ",self.nombreentry.get()
        print "Sexo ",self.boolsexo.get()
        print "FechaNac ",self.varF0.get()

        query = 'INSERT INTO "Paciente"( "Nombre", "RUN", "FechaNac", "Sexo") VALUES (%s, %s, %s, %s)'
        params = (str(self.nombreentry.get()),str(self.runentry.get()),str(self.varF0.get()),str(varSexo),)
        askDb(query,params)

    def actualizaListas(self):

        query1 =  'SELECT DISTINCT "NombreE" FROM "Enfermedad" ORDER BY "NombreE" '
        query2 =  'SELECT "NombreMedicamento" FROM "Medicamento" '
        query3 =  'SELECT DISTINCT "Zona" FROM "Radiografia" ORDER BY "Zona" '
        query4 =  'SELECT DISTINCT "NombreSustancia" FROM "Sustancia" ORDER BY "NombreSustancia" '
        query5 = 'SELECT DISTINCT "Procedencia" FROM "Radiografia" ORDER BY "Procedencia" '

        self.enfermedadCombo['values'] = tuple(auxProcessList(query1,""))
        #self.enfermedadCombo.current(0)

        self.medicamentoCombo['values'] = tuple(auxProcessList(query2,""))
        #self.medicamentoCombo.current(0)

        self.zonaCombo['values'] = tuple(auxProcessList(query3,""))
        #self.zonaCombo.current(0)

        self.alergiaCombo['values'] = tuple(auxProcessList(query4,""))
        #self.alergiaCombo.current(0)

        self.adiccionCombo['values'] = tuple(auxProcessList(query4,""))
        #self.adiccionCombo.current(0)

        self.procedenciaCombo['values'] = tuple(auxProcessList(query5,""))
        #self.procedenciaCombo.current(0)

        query6 = 'SELECT "Nombre","RUN" FROM "Paciente" ORDER BY RANDOM() LIMIT 5 '
        self.pacienteCombo['values'] = tuple(auxProcessList(query6,""))
        #self.pacienteCombo.current(0)

        pass

    def newWindow(self, tipo):
        t = Tkinter.Toplevel(self.parent)
        ventana = VentanaExtra.Demo(t,tipo)
        pass


def auxProcessList(StringQuery,param):
    try:
        listRes = askDb(StringQuery,param)

        for i in range(len(listRes)):
            listRes[i] = listRes[i][0]
        return listRes
    except :
        return []

def askDb(stringQuery,params):
    result = []
    conn = psycopg2.connect(database='radiografiasUchile',
                            host='localhost',
                            port=5432 ,
                            password = '58132154',
                            user='postgres')

    cursor = conn.cursor()
    print "String Query : ",stringQuery
    print "Params ",params
    cursor.execute(stringQuery,params)
    try:
        result = cursor.fetchall()
    except:
        result = []
    conn.commit()
    cursor.close()
    conn.close()

    return result



class PrintOne:
    def __init__(self, text):
        self.text = text

    def __call__(self):
        print self.text


root = Tkinter.Tk()
demo = Demo(root)
root.mainloop()
