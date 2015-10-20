import WidgetContainer

__author__ = 'aferral'
import Pmw
from fillDb import *
from SearchCriteria import *

queryIdAdiccion = 'SELECT "IdSustanciaAdiccion" FROM "SustanciaAdiccion" WHERE "NombreSustanciaAdiccion" = %s '
queryMedName =  'SELECT "NombreMedicamento" FROM "Medicamento" '
querySustanciaAlergia =  'SELECT DISTINCT "NombreSustanciaAlergia" FROM "SustanciaAlergia" ORDER BY "NombreSustanciaAlergia" '
querySustanciaAdiccion =  'SELECT DISTINCT "NombreSustanciaAdiccion" FROM "SustanciaAdiccion" ORDER BY "NombreSustanciaAdiccion" '
queryIdMed = 'SELECT "IdMedicamento" FROM "Medicamento" WHERE "NombreMedicamento" = %s '
queryIdAlergia = 'SELECT "IdSustanciaAlergia" FROM "SustanciaAlergia" WHERE "NombreSustanciaAlergia" = %s'

class vistaAntecedentes:
    def __init__(self,parent):

        self.checkTrabajo = IntVar()
        self.checkMed = IntVar()
        self.checkAlergia = IntVar()
        self.checkAdiccion = IntVar()
        self.checkComentario = IntVar()
        self.checkIntervencion = IntVar()

        self.varTrabajo = StringVar()
        self.medicamentoValue = StringVar()
        self.alergiaValue = StringVar()
        self.adiccionValue = StringVar()
        self.varComentario = StringVar()
        self.varOperation = StringVar()
        self.varDr = StringVar()

        self.varF2 = StringVar()
        self.varF2.set('Today')


        ##Trabajo
        self.groupTrabajo = Pmw.Group(parent.interior(), tag_text = 'Trabajo')

        self.groupTrabajo.pack(fill = 'both', expand = 1, padx = 5, pady = 5)

        Checkbutton(self.groupTrabajo.interior(), variable=self.checkTrabajo).grid(
            row=0,column=0,sticky=W, padx=5, pady=5)

        self.contTrabajos = []
        cont = WidgetContainer.Contenedor(self.groupTrabajo.interior())
        cont.add(Entry,"Trabajo",True).grid(row=0,column=2)
        cont.grid(row=0,column=1)
        self.contTrabajos.append(cont)


        Button(self.groupTrabajo.interior(),text="+",command= lambda:
        self.plusField(self.contTrabajos,self.groupTrabajo.interior())
               ).grid(row=0,column=3,sticky=E, padx=5, pady=5)
        Button(self.groupTrabajo.interior(),text="-", command= lambda:
        self.minus(self.contTrabajos)
               ).grid(row=0,column=4,sticky=E, padx=5, pady=5)
        ######################################################################


        ##Medicamentos
        self.groupMedicamentos = Pmw.Group(parent.interior(), tag_text = 'Medicamentos')
        self.groupMedicamentos.pack(fill = 'both', expand = 1, padx = 5, pady = 5)


        Checkbutton(self.groupMedicamentos.interior(), variable=self.checkMed
                    ).grid(row=0,column=0,sticky=W, padx=5, pady=5)

        self.contMedicamentos = []
        cont = WidgetContainer.Contenedor(self.groupMedicamentos.interior())
        cont.add(ttk.Combobox,"Medicamento",True,state='readonly').grid(row=0,column=2)
        cont.grid(row=0,column=1)
        self.contMedicamentos.append(cont)


        Button(self.groupMedicamentos.interior(),text="+",command= lambda:
        self.plusField(self.contMedicamentos,self.groupMedicamentos.interior())
               ).grid(row=0,column=3,sticky=E, padx=5, pady=5)
        Button(self.groupMedicamentos.interior(),text="-", command= lambda:
        self.minus(self.contMedicamentos)
               ).grid(row=0,column=4,sticky=E, padx=5, pady=5)
        #########################################################################


        ##Alergia
        self.groupAlergia = Pmw.Group(parent.interior(), tag_text = 'Alergia')
        self.groupAlergia.pack(fill = 'both', expand = 1, padx = 5, pady = 5)


        Checkbutton(self.groupAlergia.interior(), variable=self.checkAlergia
                    ).grid(row=0,column=0,sticky=W, padx=5, pady=5)


        self.contAlergia = []
        cont = WidgetContainer.Contenedor(self.groupAlergia.interior())
        cont.add(ttk.Combobox,"Alergia",True,state='readonly').grid(row=0,column=2)
        cont.grid(row=0,column=1,sticky=W, padx=5, pady=5)
        self.contAlergia.append(cont)

        Button(self.groupAlergia.interior(),text="+",command= lambda:
        self.plusField(self.contAlergia,self.groupAlergia.interior())
               ).grid(row=0,column=3,sticky=E, padx=5, pady=5)
        Button(self.groupAlergia.interior(),text="-", command= lambda:
        self.minus(self.contAlergia)
               ).grid(row=0,column=4,sticky=E, padx=5, pady=5)
        ##########################################################################


        ##Adiccion
        self.groupAdiccion = Pmw.Group(parent.interior(), tag_text = 'Adiccion')
        self.groupAdiccion.pack(fill = 'both', expand = 1, padx = 5, pady = 5)


        Checkbutton(self.groupAdiccion.interior(), variable=self.checkAdiccion).grid(row=0,column=0,sticky=W, padx=5, pady=5)

        self.contAdiccion = []
        cont = WidgetContainer.Contenedor(self.groupAdiccion.interior())
        cont.add(ttk.Combobox,"Adiccion",True,state='readonly').grid(row=0,column=2,sticky=W, padx=5, pady=5)
        cont.grid(row=0,column=1,sticky=W, padx=5, pady=5)
        self.contAdiccion.append(cont)

        Button(self.groupAdiccion.interior(),text="+",command= lambda:
        self.plusField(self.contAdiccion,self.groupAdiccion.interior())
               ).grid(row=0,column=3,sticky=E, padx=5, pady=5)
        Button(self.groupAdiccion.interior(),text="-", command= lambda:
        self.minus(self.contAdiccion)
               ).grid(row=0,column=4,sticky=E, padx=5, pady=5)
        ########################################################################

        self.groupComentario = Pmw.Group(parent.interior(), tag_text = 'Comentario')
        self.groupComentario.pack(fill = 'both', expand = 1, padx = 5, pady = 5)

        Checkbutton(self.groupComentario.interior(), variable=self.checkComentario).grid(row=0,column=0,sticky=W, padx=5, pady=5)
        Entry(self.groupComentario.interior(),textvariable = self.varComentario).grid(row=0,column=3)

       #########################################################################


        self.group3 = Pmw.Group(parent.interior(), tag_text = 'Intervenciones')
        self.group3.pack(fill = 'both', expand = 1, padx = 5, pady = 5)


        Checkbutton(self.group3.interior(), variable=self.checkIntervencion).grid(row=0,column=0,sticky=W, padx=5, pady=5)


        Label(self.group3.interior(),text = 'Fecha:').grid(row=0,column=1,sticky=W, padx=5, pady=5)

        Label(self.group3.interior(), textvariable = self.varF2).grid(row=0,column=1,sticky=W, padx=5, pady=5)
        Button(self.group3.interior(),text="Cambiar",
                            command= lambda: self.createWindowsAndBind(self.updateF2)).grid(row=0,column=2,sticky=E, padx=5, pady=5)


        Label(self.group3.interior(),text = 'Nombre Intervencion:').grid(row=1,column=1,sticky=W, padx=5, pady=5)


        Entry(self.group3.interior(), textvariable = self.varOperation).grid(row=1,column=2,sticky=W, padx=5, pady=5)

        Label(self.group3.interior(), text = 'Doctor:').grid(row=2,column=1,sticky=W, padx=5, pady=5)

        Entry(self.group3.interior(), textvariable = self.varDr).grid(row=2,column=2,sticky=W, padx=5, pady=5)



    def update(self):

        #Actualiza listas de antecedentes


        listaMed = auxProcessList(queryMedName,"")
        for contenedor in self.contMedicamentos:
            contenedor.update('Medicamento',listaMed)

        listaAlerg = auxProcessList(querySustanciaAlergia,"")
        for contenedor in self.contAlergia:
            contenedor.update('Alergia',listaAlerg)

        listaAdiccion = auxProcessList(querySustanciaAdiccion,"")
        for contenedor in self.contAdiccion:
            contenedor.update('Adiccion',listaAdiccion)



    def recreateFromId(self,idRadio):
        #Revisar en En Contexto de conseguir IdAntecedentes
        listaIdAnt = tuple(auxProcessList(querySearchIdAnt,(idRadio,)))
        if len(listaIdAnt) == 0:
            return

        #TODO UPDATE THIS SHIT

        #Por cada tabla ver si las ids estan en tabla.
        #Generar un trabajo si esta activado

        queryVerifyTrabajo = 'SELECT "NombreTrabajo" FROM "Trabajo" WHERE "IdAntecedentes" in %s'
        queryVerifyMedicamento = 'SELECT "IdMedicamento" FROM "Prescripcion Medica" WHERE "IdAntecedentes" in %s'
        queryVerifyAlergias = 'SELECT "IdSustancia" FROM "Alergico" WHERE "IdAntecedentes" in %s'
        queryVerifyAdicciones = 'SELECT "IdSustancia" FROM "Adiccion" WHERE "IdAntecedentes" in %s'

        queryNombreMedicamento = 'SELECT "NombreMedicamento" FROM "Medicamento" WHERE "IdMedicamento" = %s '
        queryNombreAlergia = 'SELECT "NombreSustanciaAlergia" FROM "SustanciaAlergia" WHERE "IdSustanciaAlergia" = %s '
        queryNombreAdiccion = 'SELECT "NombreSustanciaAdiccion" FROM "SustanciaAdiccion" WHERE "IdSustanciaAdiccion" = %s '

        queryOtrosComentario = 'SELECT "Comentario" FROM "Otros" WHERE "IdAntecedentes" in %s '
        queryIntervencion = 'SELECT "FechaOperacion", "NombreOperacion", "DrOperacion" FROM "Intervencion" ' \
                            'WHERE "IdAntecedentes" in %s '

        #Trabajo
        listaMatchTrabajo = askDb(queryVerifyTrabajo,(listaIdAnt,))

        self.cleanAllContainers(self.contTrabajos)
        for i,match in enumerate(listaMatchTrabajo):
            contenedor = self.contTrabajos[i]
            stringTrabajo = match[0]
            contenedor.set('TrabajoVar',stringTrabajo)
            self.plusField(self.contTrabajos,self.groupTrabajo.interior())
        self.minus(self.contTrabajos)

        #Medicamento

        listaMatchMedicamentos = askDb(queryVerifyMedicamento,(listaIdAnt,))
        self.cleanAllContainers(self.contMedicamentos)
        for i,match in enumerate(listaMatchMedicamentos):
            contenedor = self.contMedicamentos[i]
            idMed = match[0]
            stringMedicamento = askDb(queryNombreMedicamento,(idMed,))[0][0]
            contenedor.set('MedicamentoVar',stringMedicamento)
            self.plusField(self.contMedicamentos,self.groupMedicamentos.interior())
        self.minus(self.contMedicamentos)

        #Alergias
        listaMatchAlergias = askDb(queryVerifyAlergias,(listaIdAnt,))
        self.cleanAllContainers(self.contAlergia)
        for i,match in enumerate(listaMatchAlergias):
            contenedor = self.contAlergia[i]
            idAlerg = match[0]
            stringSusAlergia = askDb(queryNombreAlergia,(idAlerg,))[0][0]
            contenedor.set('AlergiaVar',stringSusAlergia)
            self.plusField(self.contAlergia,self.groupAlergia.interior())
        self.minus(self.contAlergia)

        #Adiccion
        listaMatchAdicciones = askDb(queryVerifyAdicciones,(listaIdAnt,))
        self.cleanAllContainers(self.contAdiccion)
        for i,match in enumerate(listaMatchAdicciones):
            contenedor = self.contAdiccion[i]
            idAdiccion = match[0]
            stringAdiccion = askDb(queryNombreAdiccion,(idAdiccion,))[0][0]
            contenedor.set('AdiccionVar',stringAdiccion)
            self.plusField(self.contAdiccion,self.groupAdiccion.interior())
        self.minus(self.contAdiccion)


        #Intervencion
        resultIntervencion = askDb(queryIntervencion,(listaIdAnt,))
        if len(resultIntervencion) > 0:
            result = resultIntervencion[0]
            self.varF2.set(result[0])
            self.varOperation.set(result[1])
            self.varDr.set(result[2])

        resultComent = askDb(queryOtrosComentario,(listaIdAnt,))
        if len(resultComent) > 0:
            result = resultComent[0]
            self.varComentario.set(result[0])
        pass

    def editFromCurrent(self,idRadio):
        self.deleteAllFromId(idRadio)
        self.createFromId(idRadio)
        pass
    def deleteAllFromId(self,idRadio):

        if idRadio == '':
            return

        listaAnt = tuple(askDb(querySearchIdAnt,(idRadio,)))
        #Borrar en contexto de
        askDb(queryDeleteEnContexto,(idRadio,))
        #Borrar cada relacion de Antecedentes
        #Trabajo
        askDb(queryDeleteAntTrabajo,(listaAnt,))
        #Medicamento
        askDb(queryDeleteAntMedicamento,(listaAnt,))
        #Alergia
        askDb(queryDeleteAntAlergia,(listaAnt,))
        #Adiccion
        askDb(queryDeleteAntAdiccion,(listaAnt,))
        #Otros
        askDb(queryDeleteAntOtros,(listaAnt,))
        #Intervencion
        askDb(queryDeleteAntIntervencion,(listaAnt,))
        #Borrar Tabla antecedentes
        askDb(queryDeleteAntecedentes,(listaAnt,))
        pass

    def createFromId(self,idTouse):
        #Generar un trabajo si esta activado
        if(self.checkTrabajo.get() == 1):
            print "Ahora tenemos activado el checkboxTrabajo"
            for contenedor in self.contTrabajos:
                stringTrabajo = contenedor.get('Trabajo')
                idCreated = generarTrabajo(True,trabajo=stringTrabajo)
                joinAntecedenteRadiografia(idCreated,idTouse)
        #Generar un medicamento si esta activado
        if(self.checkMed.get() == 1):
            print "Ahora tenemos activado el checkboxMedicamenteo"
            for contenedor in self.contMedicamentos:
                #Debo buscar id Correpondiente a seleccion
                params = (contenedor.get('Medicamento'),)
                idMed = askDb(queryIdMed,params)[0][0]
                print "Id med resultante "+str(idMed)
                idCreated = generarMedPres(True,idMed=str(idMed))
                joinAntecedenteRadiografia(idCreated,idTouse)
        #Generar un alergia si esta activado
        if(self.checkAlergia.get() == 1):
            print "Ahora tenemos activado el checkboxAlergia"
            for contenedor in self.contAlergia:
                #Debo buscar id Correpondiente a seleccion
                params = (contenedor.get('Alergia'),)
                idAlergia = askDb(queryIdAlergia,params)[0][0]
                print "Id Alergia resultante "+str(idAlergia)
                idCreated = generaraUnAlergico(1,1,True,idSus= str(idAlergia) )
                joinAntecedenteRadiografia(idCreated, idTouse)

        #Generar un adiccion si esta activado
        if(self.checkAdiccion.get() == 1):
            print "Ahora tenemos activado el checkBoxAdiccioon"
            for contenedor in self.contAdiccion:
                #Debo buscar id Correpondiente a seleccion
                params = (contenedor.get('Adiccion'),)
                idAdiccion = askDb(queryIdAdiccion,params)[0][0]
                print "Id Adiccion resultante "+str(idAdiccion)
                idCreated = generaraUnAdiccion(1,1,True,idSus = str(idAdiccion),month='2')
                joinAntecedenteRadiografia(idCreated, idTouse)
        #Generar un intervencion si esta activado
        if self.checkIntervencion.get() == 1:
            idCreated = generaraUnIntervencion(True,date = self.varF2.get(), operation = self.varOperation.get(), dr = self.varDr.get())
            joinAntecedenteRadiografia(idCreated, idTouse)
        #Generar comentario
        if self.checkComentario.get() == 1:
            idCreated = generarUnComentario(True,comment=self.varComentario.get())
            joinAntecedenteRadiografia(idCreated, idTouse)
        pass


    def plusField(self,contArray,where):
        newRow = contArray[0].clone(where)
        newRow.grid(row=len(contArray),column=1, padx=5, pady=5)
        contArray.append(newRow)
        self.update()
        return newRow


    def minus(self,aArray):
        if len(aArray) == 1:
            return
        disable = aArray.pop()
        disable.grid_forget()
        self.update()

    def updateF2(self,x):
        self.varF2.set(x.strftime('%Y-%m-%d'))
        return

    def createWindowsAndBind(self,fun):
        print fun
        sf = SecondFrame(Tkinter.Toplevel())
        sf.setCallback(fun)

    def cleanAllContainers(self,containerList):
        while len(containerList) > 1:
            self.minus(containerList)
        pass
