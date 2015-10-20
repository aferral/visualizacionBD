import tkMessageBox
from librerias.Calendar import SecondFrame

__author__ = 'aferral'
from Tkinter import *
import ttk
import WidgetContainer
from librerias.SearchCriteria import auxProcessList
from librerias.SearchCriteria import askDb
from librerias.querys.queryList import *
class vistaRadio:
    def __init__(self,Frame):
        self.refWidget = {}

        self.varIdEn = StringVar()
        self.pacienteValue = StringVar()
        self.varFrame = StringVar()
        self.varComentario = StringVar()
        self.varF1 = StringVar()
        self.varF1.set('Today')

        self.procedenciaValue = StringVar()


        Label(Frame.interior(), text = 'Id:').grid(row=1,column=0,sticky=W, padx=5, pady=5)
        Entry(Frame.interior(), textvariable=self.varIdEn).grid(row=1,column=1,sticky=W, padx=5, pady=5)

        Label(Frame.interior(), text="Paciente:").grid(row=2,column=0,sticky=W, padx=5, pady=5)

        self.pacienteCombo = ttk.Combobox(Frame.interior(), textvariable=self.pacienteValue,
                                state='readonly')
        self.pacienteCombo['values'] = ()
        self.pacienteCombo.grid(row=2,column=1,sticky=W, padx=5, pady=5)

        self.refWidget['PacienteCombo'] = self.pacienteCombo


        self.groupEnf = LabelFrame(Frame.interior(),bd=0)
        self.groupEnf.grid(row=3,column=0,sticky=NW)

        self.groupEnfCombo = LabelFrame(Frame.interior(),bd=0)
        self.groupEnfCombo.grid(row=3,column=1,sticky=NW)

        self.groupEnfB = LabelFrame(Frame.interior(),bd=0)
        self.groupEnfB.grid(row=3,column=2,sticky=NW)

        Label(self.groupEnf, text="Enfermedad:").grid(row=0,column=5,sticky=NE, padx=5, pady=5)



        self.contEnf = []
        cont = WidgetContainer.Contenedor(self.groupEnfCombo)
        cont.add(ttk.Combobox,"Enfermedad",True,state='readonly').grid(row=0,column=0,sticky=W, padx=5, pady=5)
        cont.add(ttk.Combobox,"Confirmado",True,state='readonly').grid(row=1,column=0,sticky=W, padx=5, pady=5)
        cont.add(Entry,"Comentario",True,).grid(row=2,column=0,sticky=W, padx=5, pady=5)
        cont.grid(row=1,column=0,sticky=W, padx=5, pady=5)
        self.contEnf.append(cont)


        Button(self.groupEnfB,text="+",command= lambda: self.expPlus(self.contEnf,self.groupEnfCombo)
                               ).grid(row=0,column=2,sticky=NE, padx=5, pady=5)
        Button(self.groupEnfB,text="-",command= lambda: self.expMinus(self.contEnf)
                                ).grid(row=0,column=3,sticky=NE, padx=5, pady=5)

        Label(Frame.interior(),text = 'Frames \n>1 usar (;) :').grid(row=4,column=0,sticky=W, padx=5, pady=5)


        Entry(Frame.interior(),textvariable=self.varFrame).grid(row=4,column=1,sticky=W, padx=5, pady=5)

        # Create and pack the dropdown ComboBox.
        Label(Frame.interior(), text="Zona:").grid(row=5,column=0,sticky=W, padx=5, pady=5)
        self.zonaValue = StringVar()
        self.zonaCombo = ttk.Combobox(Frame.interior(), textvariable=self.zonaValue,
                                state='readonly')

        self.zonaCombo.grid(row=5,column=1,sticky=W, padx=5, pady=5)


       # Create and pack the dropdown ComboBox.
        Label(Frame.interior(), text="Tipo:").grid(row=6,column=0,sticky=W, padx=5, pady=5)
        self.tipoValue = StringVar()
        self.tipoCombo = ttk.Combobox(Frame.interior(), textvariable=self.tipoValue,
                                state='readonly')
        self.tipoCombo.grid(row=6,column=1,sticky=W, padx=5, pady=5)

        Label(Frame.interior(), text="Fecha").grid(row=7,column=0,sticky=W, padx=5, pady=5)

        Label(Frame.interior(), textvariable = self.varF1).grid(row=7,column=1,sticky=W, padx=5, pady=5)
        Button(Frame.interior(),text="Cambiar",command=
        lambda: self.createWindowsAndBind(self.updateF1)).grid(row=7,column=1,sticky=E, padx=5, pady=5)

        Label(Frame.interior(), text="Procedencia:").grid(row=8,column=0,sticky=W, padx=5, pady=5)

        self.procedenciaCombo = ttk.Combobox(Frame.interior(), textvariable=self.procedenciaValue,
                                state='readonly')
        self.procedenciaCombo.grid(row=8,column=1,sticky=W, padx=5, pady=5)


        Label(Frame.interior(),text = 'Comentario:').grid(row=9,column=0,sticky=W, padx=5, pady=5)

        Entry(Frame.interior(),textvariable=self.varComentario).grid(row=9,column=1,sticky=W, padx=5, pady=5)

        pass

    def update(self):


        # Actualiza enfermedas, Confirmados
        listaEnf = auxProcessList(queryEnfName,"")
        listaConf = ("True","False")
        for contenedor in self.contEnf:
            print "Actualizando contenedor"
            contenedor.update("Enfermedad",listaEnf)
            contenedor.update("Confirmado",listaConf)
        self.zonaCombo['values'] = tuple(auxProcessList(queryRadiZone,""))
        self.tipoCombo['values'] = tuple(auxProcessList(queryTipos,""))
        self.procedenciaCombo['values'] = tuple(auxProcessList(queryProcedencia,""))
        pass

    def expPlus(self,lista,where):
        newRow = lista[0].clone(where)
        newRow.grid(row=len(lista)+1,column=0, padx=5, pady=5)
        lista.append(newRow)
        self.update()
        pass
    def expMinus(self,lista):
        if len(lista) == 1:
            return
        disable = lista.pop()
        disable.grid_forget()
        self.update()
        pass

    def getData(self):
        dataOut = {}
        dataOut['id'] = str(self.varIdEn.get())
        dataOut['FechaN'] = str(self.varF1.get())
        dataOut['Zona'] = str(self.zonaValue.get())
        dataOut['Proc'] = str(self.procedenciaValue.get())
        dataOut['Tipo'] = str(self.tipoValue.get())
        dataOut['Comentario'] = str(self.varComentario.get())
        dataOut['PacName'] = str(self.pacienteValue.get().split(",")[0])
        dataOut['PacApell'] = str(self.pacienteValue.get().split(",")[1])
        dataOut['PacRun'] = str(self.pacienteValue.get().split(",")[2])
        dataOut['ContEnf'] = self.contEnf
        dataOut['FrameList'] = self.varFrame.get().split(";")

        return dataOut

    def createWindowsAndBind(self,fun):
        print fun
        sf = SecondFrame(Toplevel())
        sf.setCallback(fun)
    def updateF1(self,x):
        self.varF1.set(x.strftime('%Y-%m-%d'))
        return
    def getWidget(self,palabra):
        return self.refWidget[palabra]

    def recreateFromId(self,idToSearch):

        #Consigue info de radiografia

        result = askDb(queryGetRadioInfo,(idToSearch,))
        print result
        if len(result) == 0:
            return
        result = result[0]
        #Actualiza campos simples

        self.varIdEn.set(result[0])
        self.varF1.set(result[1])
        self.zonaValue.set(result[2])
        self.procedenciaValue.set(result[3])
        self.tipoValue.set(result[4])
        self.varComentario.set(result[5])

        self.pacienteValue.set(str(result[7])+","+str(result[8])+","+str(result[6]))


        #Consigue enfermedades asociadas
        resultEnf = askDb(queryRepresentaFromId, (idToSearch,))
        template = self.contEnf[0]
        self.contEnf = [template]
        for index,enfermedad in enumerate(resultEnf):
            container = self.contEnf[index]
            container.set("Enfermedad", enfermedad[0])
            container.set("Confirmado", 'True' if enfermedad[1] else 'False')
            container.set("ComentarioVar", enfermedad[2])
            self.expPlus(self.contEnf,self.groupEnf)
        self.expMinus(self.contEnf)
        #Actualiza y crea los combox asociados

        #Consigue frames asociadas
        resultFrames = askDb(queryFrames,(idToSearch,))
        stringR = " "
        for frame in resultFrames:
            stringR =stringR+frame[0]+";"
        stringR = stringR[1:-1]
        self.varFrame.set(stringR)

        self.update()

    def deleteCurrentRelations(self):#Mata las relaciones de Enfermedas y Frames asociadas a la id Actual
        idActual = int(self.varIdEn.get())
        askDb(queryDeleteFrames,(idActual,))
        askDb(queryDeleteEnfRelation,(idActual,))

        pass
    def deleteCurrentRadio(self): #Destruye la radiografia con la idActualmente ingresada
        idActual = int(self.varIdEn.get())
        askDb(queryDeleteRadio,(idActual,))
        pass

    def clean(self):
        self.varIdEn.set('')
        self.varF1.set('')
        self.zonaValue.set('')
        self.procedenciaValue.set('')
        self.tipoValue.set('')
        self.varComentario.set('')

        self.pacienteValue.set('')

        while len(self.contEnf) > 1:
            self.expMinus(self.contEnf)
        container = self.contEnf[0]
        container.set("Enfermedad", '')
        container.set("Confirmado", '')
        container.set("ComentarioVar", '')

        self.varFrame.set('')

        self.update()

    def crearRadio(self):
        #Consigue informacion de radiografia
        try:
            data = self.getData()
            valId = data['id']
            valFecha = data['FechaN']
            valZona = data['Zona']
            valProc = data['Proc']
            valTipo = data['Tipo']
            valComent = data['Comentario']
            valPacName = data['PacName']
            valPacApell = data['PacApell']
            valPacRun = data['PacRun']

            contenedorEnf = data['ContEnf']
            lsitaFrame = data['FrameList']

            params = (valId,valFecha,valZona,valProc,valTipo,valComent,valPacRun,valPacName,valPacApell,)
        except Exception, e :
            print str(e)
            tkMessageBox.showinfo("Resultado","Status: "+str(e))
            return
        try:
            askDb(queryInsertRadio,params)
            tkMessageBox.showinfo("Resultado","Status: "+"Radiografia agregada")
        except Exception, e:
            print str(e)
            tkMessageBox.showinfo("Resultado","Status: "+str(e))



        #Agrega las distintas enfermedades y los distintos frames
        for contenedor in contenedorEnf:
            valorEnf = contenedor.get('Enfermedad')
            valorConf = contenedor.get('Confirmado')
            valorComent = contenedor.get('Comentario')
            if valorEnf != '':
                askDb(queryAddEnfToRad, (valorEnf,valorConf,valId,valorComent,))

        #Agrega los distintos frames
        for elem in lsitaFrame:
            stringTemp = elem.strip()
            askDb(queryAddFrame,(stringTemp,valId,))

        return int(valId)

    def edit(self):
        #Consigue informacion de radiografia
        data = self.getData()
        valId = data['id']
        valFecha = data['FechaN']
        valZona = data['Zona']
        valProc = data['Proc']
        valTipo = data['Tipo']
        valComent = data['Comentario']
        valPacName = data['PacName']
        valPacApell = data['PacApell']
        valPacRun = data['PacRun']

        contenedorEnf = data['ContEnf']
        lsitaFrame = data['FrameList']

        params = (valId,valFecha,valZona,valProc,valTipo,valComent,valPacRun,valPacName,valPacApell,valId,)

        try:
            askDb(queryUpdateRadio,params)
            print "Radiografia editada exitosamente"
        except Exception, e:
            print str(e)
            print "Error en Query"

        #Borrar relaciones enfermedad, borrar relaciones frames
        self.deleteCurrentRelations()

        #Setea que estamos usando esta id
        currentId = valId

        #Agrega las distintas enfermedades y los distintos frames
        for contenedor in contenedorEnf:
            valorEnf = contenedor.get('Enfermedad')
            valorConf = contenedor.get('Confirmado')
            valorComent = contenedor.get('Comentario')
            valorId = str(currentId)

            askDb(queryAddEnfToRad, (valorEnf,valorConf,valorId,valorComent,))

        #Agrega los distintos frames
        for elem in lsitaFrame:
            stringTemp = elem.strip()
            askDb(queryAddFrame,(stringTemp,str(currentId)))