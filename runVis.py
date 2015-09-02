__author__ = 'aferral'


from Tkinter import *
import ttk
from tkintertable.Tables import TableCanvas
from tkintertable.TableModels import TableModel
from SearchCriteria import *
from test3 import *
listaSearch = []
resultSearch = []
#Crear la cosa de la primary keys
#ESta enfocado en busqueda de radiografias

#Por alguna razon no busca bien con este rut 10324885 tiene asociado 2 encuentra 1 (problema BD no interfaz)

#Activar busqueda por query en cada uno de los tipos de filotr

#Una vez con todas la ids de busqueda mandar a show que actualiza la tablas excel
#En estas solo toma una id por fila de la tabla radiografias x enfermedades
#Esta mete todas enfermedades en una sola comulna cosa de un idRadio por fila
#De hacerle click expande paciente asociado y antecedetse de radiografias
#Hacer not null confirmado (para que sea binario)
#Fuma es un nuevo antecedente y es not null
#Radiografias es un atributo (opt)
#Como quitar ambiguedad de nombres

#La busqueda de nombres parece no funcionar


#Funcionalidad opcional
#Exportar a excel
#Backup automatico y recuperacion
#Documentacion
#Claves y usuarios

class GraficInterfaceDb:
    def __init__(self):

        self.listEnfermedad = ['a',"d","c"]
        self.listMedicamentos = ['a',"d","c"]
        self.listObserver = []

        self.actualizarListas()

        r = Tk()

        r.wm_title("Ventana de busqueda")

        lTextoEntrada = Label(r, text="Ventana de busqueda")
        lTextoEntrada.grid(row=0,column=1)

        #Filtrar por id
        marco00=Frame(r)
        listaSearch.append(IdSearch(marco00))
        marco00.grid(row=0,column=0)

        #Filtrar por nombre
        marco01=Frame(r)
        listaSearch.append(NameSearch(marco01))
        marco01.grid(row=1,column=0)


        #Filtrar por Rut
        marco02=Frame(r)
        listaSearch.append(RutSearch(marco02))
        marco02.grid(row=2,column=0)

        #Filtrar por sexo
        marco03=Frame(r)
        listaSearch.append(SexoSearch(marco03))
        marco03.grid(row=3,column=0)

        #Filtrar por Enfermedad y confirmado comboBox
        marco04=Frame(r)

        barraEnf = Enfermedadearch(marco04, self.listEnfermedad)
        self.listObserver.append(barraEnf)
        listaSearch.append(barraEnf)
        marco04.grid(row=4,column=0)


        #Tipo de radiografia
        marco05=Frame(r)
        listaSearch.append(TipoRadioSearch(marco05))
        marco05.grid(row=5,column=0)

        #Fecha inicio fecha final
        marco06=Frame(r)
        listaSearch.append(FechaSearch(marco06))
        marco06.grid(row=6,column=0)

        #Fuma
        marco09 = Frame(r)
        listaSearch.append(FumaSearch(marco09))
        marco09.grid(row=9,column=0)


        #Medicamento
        marco10 = Frame(r)
        barraMedic= MedicamentoSearch(marco10,self.listMedicamentos)
        self.listObserver.append(barraMedic)
        listaSearch.append(barraMedic)
        marco10.grid(row=10,column=0)

        #Mostrar resultados
        marco11 = Frame(r)

        bSearch = Button(marco11, text="Busqueda",command=self.doQuery)
        bSearch.pack()

        lResultados = Label(marco11,text="Resultados de query: ")
        lResultados.pack()
        bExportExcel = Button(marco11, text="Exportar a excel")
        bExportExcel.pack()
        marco11.grid(row=11,column=0)

        marco12 = Frame(r)
        self.model = TableModel()
        self.table = TableCanvas(marco12, self.model,
                            cellwidth=60, cellbackgr='#e3f698',
                            thefont=('Arial',9),rowheight=18, rowheaderwidth=30,
                            rowselectedcolor='yellow', editable=True)
        self.table.createTableFrame()
        marco12.grid(row=12,column=0)

        self.b = VentanaDetalles(Tkinter.Toplevel())
        self.b.setWindow(self)
        r.bind("<Button-1>",self.b.setValues)
        r.mainloop()

    def getEnfList(self):
        return self.listEnfermedad
    def getMedList(self):
        return self.listMedicamentos
    def getCurrentIdRadio(self):
        try:
            print self.table.get_currentRecord()
            return self.table.get_currentRecord()["IdRadio11"]
        except:
            return None


    def actualizarListas(self):
        query1 =  'SELECT DISTINCT "NombreE" FROM "Enfermedad" ORDER BY "NombreE" '
        query2 =  'SELECT "NombreMedicamento" FROM "Medicamento" '
        self.listEnfermedad = auxProcessList(query1,"")
        self.listMedicamentos = auxProcessList(query2,"")

        for element in self.listObserver:
            element.update(self)


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
                #resultSearch += result

        self.showResultInTable(resultSearch)
        return

    def showResultInTable(self,lista):
        data = {}

        #Ahora esta mostrando todas las radiografias que encuentra con criterios (incluso si no tieneen enf asociada)
        contador = 0
        query = 'select * from "Radiografia" LEFT OUTER JOIN "Representa" ON ("Radiografia"."IdRadio" = "Representa"."IdRadio") WHERE "Radiografia"."IdRadio" in %s'
        columnNames = {0:"IdRadio11", 1:"Fecha", 2:"Zona", 3:"Procedencia", 4:"Tipo", 5:"Comentario", 6:"RunPaciente",
                       7:"NombrePaciente", 8:"IdRadio22",9:"NombreEnfermedad",10:"Confirmado",11:"Comentario",12:"Evolucion",13:"Agudeza"}

        if(len(lista) != 0):
            resultQuery = askDb(query,(tuple(lista),))
        else:
            data = {}

            self.model.importDict(data)
            self.model.setupModel({})
            self.table.redrawTable()

            return
        #Aca es posible que falle si los nombre se las columnas no estan correctos
        for element in resultQuery:
            temp = zip(element,range(len(element)))
            tempDic = {}
            for atomicVal in temp:
                tempDic[str(columnNames[atomicVal[1]])] = str(atomicVal[0])
            data[str(contador)] = tempDic
            contador+=1
        self.model.setupModel({})
        self.model.importDict(data)
        self.table.redrawTable()


        return

a = GraficInterfaceDb()
