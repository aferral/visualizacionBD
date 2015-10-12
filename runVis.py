__author__ = 'aferral'

from tkintertable.Tables import TableCanvas
from tkintertable.TableModels import TableModel

from librerias.SearchCriteria import *
from ventanaAntecedentes import *

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

queryMostrar = 'select "IdRadio","Fecha","Zona","Procedencia","Tipo","RUNPaciente","NombresPaciente", ' \
                '"ApellidosPaciente","NombreE","Confirmado" from "Radiografia" ' \
                'JOIN "Representa" USING ( "IdRadio" ) WHERE "Radiografia"."IdRadio" in %s'
metaquery = 'CREATE TEMP TABLE tmp126 AS ( ' + queryMostrar + " ) ;" + "SELECT column_name " \
        "FROM  information_schema.columns WHERE  table_name = 'tmp126' ORDER  BY ordinal_position"

idColumnName = "('IdRadio',)"

queryListaEnf =  'SELECT DISTINCT "NombreE" FROM "Enfermedad" ORDER BY "NombreE" '
queryListaMed =  'SELECT "NombreMedicamento" FROM "Medicamento" '

class GraficInterfaceDb:
    def __init__(self):

        self.listEnfermedad = ['a',"d","c"]
        self.listMedicamentos = ['a',"d","c"]
        self.listObserver = []
        self.actualizarListas()
        self.actualrow = 0

        self.r = Tk()
        self.r.wm_title("Ventana de busqueda")
        self.group = LabelFrame(self.r,bd=0)
        self.group.grid(row=0,column=0,sticky=NW)


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
        bSearch.pack()

        lResultados = Label(marco11, text="Resultados de query: ")
        lResultados.pack()
        bExportExcel = Button(marco11, text="Exportar a excel")
        bExportExcel.pack()
        marco11.grid(row=self.actualrow, column=0)
        self.actualrow+=1

        marco12 = Frame(self.r)
        self.model = TableModel()
        self.table = TableCanvas(marco12, self.model,
                            cellwidth=60, cellbackgr='#e3f698',
                            thefont=('Arial',9),rowheight=18, rowheaderwidth=30,
                            rowselectedcolor='yellow', editable=True)
        self.table.createTableFrame()
        marco12.grid(row=self.actualrow,column=0)
        self.actualrow+=1

        self.actualizarListas()

        self.b = VentanaDetalles(Tkinter.Toplevel())
        self.b.setWindow(self)

        self.r.bind("<Button-1>",self.b.setValues)
        self.r.mainloop()

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
            columnNames = resultQuery2

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
