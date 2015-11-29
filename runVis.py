import time

__author__ = 'aferral'

from tkintertable.Tables import TableCanvas
from tkintertable.TableModels import TableModel

from SearchCriteria import *
from ventanaAntecedentes import *
from librerias.querys.queryList import *

listaSearch = []
resultSearch = []

#Por alguna razon no busca bien con este rut 10324885 tiene asociado 2 encuentra 1 (problema BD no interfaz)


#Que pasa con multiples enfermedades
#Que pasa con multiples frames

#Funcionalidad opcional
#Exportar a excel
#Actualizacion de codigo mediante git
#Backup automatico y recuperacion
#Documentacion
#Claves y usuarios


idColumnName = "IdRadio"



class GraficInterfaceDb:
    def __init__(self,parent):

        self.listEnfermedad = ['a',"d","c"]
        self.listMedicamentos = ['a',"d","c"]
        self.listObserver = []
        self.actualizarListas()
        self.actualrow = 0
        self.rowEvent = 99

        #Ventana de tablas y entradas
        self.r1 = parent
        self.r = Frame(self.r1)
        self.r1.wm_title("Ventana de busqueda")
        self.group = LabelFrame(self.r,bd=0)
        # self.group.grid(row=0,column=0,sticky=NW, padx=5, pady=5)
        self.group.pack(side=LEFT)
        self.r.pack(expand=True, fill='x',side=LEFT)

        # Ventana que muestra antecedesntes y informacion especifica de radiografia
        self.a = Frame(self.r1,padx=20, pady=20)
        self.b = VentanaDetalles(self.a)
        self.b.setWindow(self)
        self.a.pack(side=RIGHT)

        #Filtrar por id
        self.putInPlace(IdSearch)
        #Filtrar por nombre
        self.putInPlace(NameSearch)
        #Filtrar por apellido
        self.putInPlace(LastNameSearch)
        #Filtrar por Rut
        self.putInPlace(RutSearch)
        #Filtrar por sexo
        self.putInPlace(SexoSearch)
        #Filtrar por Enfermedad y confirmado comboBox
        self.listObserver.append(self.putInPlace(Enfermedadearch))
        #Filtro confirmado
        self.putInPlace(ConfirmadoSearch)
        #Tipo de radiografia
        self.putInPlace(TipoRadioSearch)
        #Fecha inicio fecha final
        self.putInPlace(FechaSearch)
        #Fuma
        self.putInPlace(FumaSearch)
        #Medicamento
        self.listObserver.append(self.putInPlace(MedicamentoSearch))
        #Mostrar resultados
        marco11 = Frame(self.r)

        bSearch = Button(marco11, text="Busqueda", command=self.doQuery)
        bSearch.pack(padx=5, pady=5)

        lResultados = Label(marco11, text="Resultados de query: ")
        lResultados.pack(padx=5, pady=5)

        # marco11.grid(row=self.actualrow, column=0,sticky=W, padx=5, pady=5)
        marco11.pack()
        self.actualrow+=1

        marco12 = Frame(self.r)
        self.model = TableModel()
        self.table = TableCanvas(marco12, self.model,
                            cellwidth=120, cellbackgr='#e3f698',
                            thefont=('Arial',9),rowheight=18, rowheaderwidth=30,
                            rowselectedcolor='yellow', editable=False)
        self.table.createTableFrame()
        # marco12.grid(row=self.actualrow,column=0,sticky=W, padx=5, pady=5)
        marco12.pack(expand=False, fill='x')
        self.actualrow += 1

        self.actualizarListas()




        self.r1.bind("<Button-1>",self.changeCurrentId)


    def getEnfList(self):
        print "Lista de enfermedad "+str(self.listEnfermedad)
        return self.listEnfermedad
    def getMedList(self):
        return self.listMedicamentos



    #Si quieres gridear creo que aqui es un buen lugar
    def putInPlace(self, claseBusqueda):
        

        #SI ACA COLOCAS TRUE TODOS LOS COMPONENTES NO HACEN PACK Y SE GUARDAN EN LISTA self.listaComponente
        #Puedes cambiar tanto el parent como el grid
        objetoNuevo = claseBusqueda(self.group,True)
        cont = 1
        #Ejemplo de como se podrian sacar los componentes
        for comp in objetoNuevo.listaComponente:
            comp.grid(row=self.actualrow,column=cont)
            # comp.pack()
            cont+=1
        listaSearch.append(objetoNuevo)

        self.actualrow+=1

        return objetoNuevo

    def getCurrentIdRadio(self):
        try:
            print self.table.get_currentRecord()
            return self.table.get_currentRecord()[idColumnName]
        except:
            return None


    def actualizarListas(self):

        self.listEnfermedad = auxProcessList(queryListaEnf,"")
        self.listMedicamentos = auxProcessList(queryListaMed,"")

        for element in self.listObserver:
            element.update(self)

    def changeCurrentId(self,event):
        print "Antiguo ",self.rowEvent," real ",self.table.currentrow

        if (self.rowEvent != self.table.currentrow):
            self.rowEvent = self.table.currentrow
            print("Evento activado")
            self.b.setValues(event)
        pass

    def doQuery(self):
        self.actualizarListas()
        print "Im about to query"
        resultSearch = []
        for element in listaSearch:
            if(element.isActive()):
                result = element.giveFilterResults()
                print result
                if (len(resultSearch) != 0):
                    set1 = set(result)
                    set2 = set(resultSearch)
                    set3 = set1 & set2
                    print set3
                    resultSearch = set3
                else:
                    resultSearch = result

        self.showResultInTable(resultSearch)
        return

    def showResultInTable(self,lista):
        data = {}
        resultQuery = []

        #Ahora esta mostrando todas las radiografias que encuentra con criterios (incluso si no tieneen enf asociada)
        contador = 0
        columnNames = {}

        if(len(lista) != 0):
            resultQuery = askDb(queryMostrar,(tuple(lista),))
            resultQuery2 = askDb(metaquery,(tuple(lista),))
            for index,name in enumerate(resultQuery2):
                columnNames[index] = name[0]

        for element in resultQuery:
            temp = zip(element,range(len(element)))
            tempDic = {}
            for atomicVal in temp:
                print atomicVal
                tempDic[str(columnNames[atomicVal[1]])] = str(atomicVal[0])
            data[str(contador)] = tempDic
            contador+=1
        self.model.setupModel({})
        self.model.importDict(data)
        self.table.redrawTable()

        self.b.setValues(0)
        return

