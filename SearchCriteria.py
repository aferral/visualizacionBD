__author__ = 'aferral'
from Tkinter import *
import psycopg2
import ttk
from Calendar import *
from librerias.querys.queryList import *


def askDb(stringQuery,params):
    result = []
    ## Cambia el nombre de la DB
    conn = psycopg2.connect(database='radiografiasUchile',
                            host='localhost',
                            port=5432 ,
                            password = 'postgres',
                            user='postgres')

    cursor = conn.cursor()
    print "String Query : ",stringQuery
    print "Params ",params
    cursor.execute(stringQuery,params)
    try:
        result = cursor.fetchall()
        print "Result: ",result
    except Exception, e:
        print "No cursor"
    finally:
        cursor.close()
    conn.commit()
    conn.close()

    return result

def auxProcessList(StringQuery,param):
    try:
        listRes = askDb(StringQuery,param)

        for i in range(len(listRes)):
            listRes[i] = listRes[i][0]
        return listRes
    except :
        return []

class AbstractSearchCriteria(object):
    def __init__(self,marco,mode):
        self.listaComponente = []
        self.mode = mode #SI MODO ES TRUE SE ESPERA QUE SE GRIDEE EXTERNAMENTE TODO QUEDA EN self.listaComponente
        self.active = IntVar()
        c = Checkbutton(marco, variable=self.active)
        self.ajusta(c)


        pass
    def ajusta(self,elemento):
        #Usa esto si quieres gridear de forma externa
        if (not self.mode):
            elemento.pack(side=LEFT)
        else:
            self.listaComponente.append(elemento)
    def isActive(self):
        return self.active.get()
    def giveFilterResults(self):
        return []
    def giveComp(self):
        return self.comp

class IdSearch(AbstractSearchCriteria):
    def __init__(self,marco,mode):
        AbstractSearchCriteria.__init__(self, marco,mode)
        marcoF0 = Frame(marco,borderwidth=2, relief=RIDGE)
        lIdRadio = Label(marcoF0, text="IdRadio")
        self.eIdRadio = Entry(marcoF0)

        lIdRadio.pack()
        self.eIdRadio.pack()

        self.ajusta(marcoF0)

    def giveFilterResults(self):
        idToSearch = self.eIdRadio.get()
        params = (str(idToSearch),)
        return auxProcessList(queryIdRadio,params)


class NameSearch(AbstractSearchCriteria):
    def __init__(self, marco,modo):
        AbstractSearchCriteria.__init__(self, marco,modo)
        marcoF0 = Frame(marco,borderwidth=2, relief=RIDGE)
        lNombrePaciente = Label(marcoF0, text="Nombre Paciente")
        self.eNombrePaciente = Entry(marcoF0)

        lNombrePaciente.pack()
        self.eNombrePaciente.pack()

        self.ajusta(marcoF0)

        pass

    def giveFilterResults(self):
        nameToSearch = "%"+self.eNombrePaciente.get()+"%"
        params = (str(nameToSearch),)
        return auxProcessList(queryNombresPaciente,params)
class LastNameSearch(AbstractSearchCriteria):
    def __init__(self, marco,modo):
        AbstractSearchCriteria.__init__(self, marco,modo)
        marcoF0 = Frame(marco,borderwidth=2, relief=RIDGE)
        lApellidosPaciente = Label(marcoF0, text="Apellido Paciente")
        self.eApellidoPaciente = Entry(marcoF0)

        lApellidosPaciente.pack()
        self.eApellidoPaciente.pack()
        self.ajusta(marcoF0)

        pass

    def giveFilterResults(self):
        nameToSearch = "%"+self.eApellidoPaciente.get()+"%"
        params = (str(nameToSearch),)
        return auxProcessList(queryApellidosPaciente,params)

class RutSearch(AbstractSearchCriteria):
    def __init__(self, marco,modo):
        AbstractSearchCriteria.__init__(self, marco,modo)
        marcoF0 = Frame(marco,borderwidth=2, relief=RIDGE)
        lRutPaciente= Label(marcoF0, text="Rut: ")
        self.eRutPaciente = Entry(marcoF0)

        lRutPaciente.pack()
        self.eRutPaciente.pack()
        self.ajusta(marcoF0)
        pass
    def giveFilterResults(self):
        rutToSearch = self.eRutPaciente.get()
        params = (str(rutToSearch),)
        return auxProcessList(queryRUN,params)

class SexoSearch(AbstractSearchCriteria):
    def __init__(self,marco,modo):
        AbstractSearchCriteria.__init__(self, marco,modo)
        marcoF0 = Frame(marco,borderwidth=2, relief=RIDGE)
        lSexo= Label(marcoF0, text="Sexo: ")
        lSexo.pack()

        self.boolSexo = IntVar()
        radio1 = Radiobutton(marcoF0, text="M", variable=self.boolSexo, value=1)
        radio1.pack(side=LEFT)
        radio2 = Radiobutton(marcoF0, text="H", variable=self.boolSexo, value=2)
        radio2.pack(side=RIGHT)

        self.ajusta(marcoF0)

        pass
    def giveFilterResults(self):
        valRadio = self.boolSexo.get()
        if valRadio == 1: #Es mujer buscar todas
            params = (str(""'M'""),)
        elif valRadio == 2:
            params = (str(""'H'""),)
        return auxProcessList(querySexoPaciente,params)


class Enfermedadearch(AbstractSearchCriteria): #Va enfermedad y confirmado
    def __init__(self, marco,modo):
        AbstractSearchCriteria.__init__(self,marco,modo)
        marcoF0 = Frame(marco,borderwidth=2, relief=RIDGE)
        lEnfermedad= Label(marcoF0, text="Enfermedad a buscar: ")
        self.enfermedadaValues = StringVar()
        self.comboEnfermedades = ttk.Combobox(marcoF0, textvariable=self.enfermedadaValues,
                                state='readonly')


        lEnfermedad.pack()
        self.comboEnfermedades.pack()
        self.ajusta(marcoF0)

        pass

    def update(self,objToQuery):
        self.comboEnfermedades['values'] = tuple(objToQuery.getEnfList())

    def giveFilterResults(self):
        params = (str(self.comboEnfermedades.get()),)
        return auxProcessList(queryEnfermedadNombre, params)


class ConfirmadoSearch(AbstractSearchCriteria):
    def __init__(self, marco,modo):
        AbstractSearchCriteria.__init__(self,marco,modo)
        marcoF0 = Frame(marco,borderwidth=2, relief=RIDGE)
        self.varSi = IntVar()
        r1 = Radiobutton(marcoF0, text="Confirmado", variable=self.varSi, value=1)
        r1.pack(side=LEFT)
        r2 = Radiobutton(marcoF0, text="Sospechoso", variable=self.varSi, value=2)
        r2.pack(side=RIGHT)

        self.ajusta(marcoF0)

        pass

    def giveFilterResults(self):
        params = ('TRUE' if (self.varSi.get()==1) else 'FALSE',)
        return auxProcessList(queryEnfermedadConfirmado, params)



class TipoRadioSearch(AbstractSearchCriteria):
    def __init__(self,marco,modo):
        AbstractSearchCriteria.__init__(self,marco,modo)
        marcoF0 = Frame(marco,borderwidth=2, relief=RIDGE)
        lTipoRadiografia= Label(marcoF0, text="Tipo de radiografia: ")
        self.tipoRadiografiaValues = StringVar()
        comboTipoRadiografia = ttk.Combobox(marcoF0, textvariable=self.tipoRadiografiaValues,
                                state='readonly')
        comboTipoRadiografia['values'] = ('Radiografia', 'Escaner', 'Resonancia')

        lTipoRadiografia.pack()
        comboTipoRadiografia.pack()

        self.ajusta(marcoF0)

        pass
    def giveFilterResults(self):

        params = (str(self.tipoRadiografiaValues.get()),)
        return auxProcessList(queryTipoRadio,params)

class FechaSearch(AbstractSearchCriteria): # Va rango de fechas
    def __init__(self,marco,modo):
        AbstractSearchCriteria.__init__(self,marco,modo)
        marcoF0 = Frame(marco,borderwidth=2, relief=RIDGE)
        #Fecha inicio
        
        lFechaRadiografia= Label(marcoF0, text="Busqueda en rango:")
        lFechaRadiografia.pack()
        self.varF0 = StringVar()
        self.varF0.set('Today')
        self.lF1 = Label(marcoF0, text = "DESDE:")
        self.lF1.pack()
        self.lF0 = Label(marcoF0, textvariable = self.varF0)
        self.lF0.pack()
        self.buttonF0 = Button(marcoF0,text="Cambiar", command= lambda: self.createWindowsAndBind(self.updateF0))
        self.buttonF0.pack()


        self.ajusta(marcoF0)


        #Fecha final
        lFechaRadiografiaFin= Label(marcoF0, text="HASTA : ")
        lFechaRadiografiaFin.pack()
        self.varFf = StringVar()
        self.varFf.set('Tomorrow')
        self.lFf = Label(marcoF0, textvariable = self.varFf)
        self.lFf.pack()
        self.buttonFf = Button(marcoF0,text="Cambiar", command= lambda: self.createWindowsAndBind(self.updateFf))
        self.buttonFf.pack()


        pass
    def updateF0(self,x):
        self.varF0.set(x.strftime('%Y-%m-%d'))
        return
    def updateFf(self,x):
        self.varFf.set(x.strftime('%Y-%m-%d'))
        return
    def createWindowsAndBind(self,fun):
        sf = SecondFrame(Tkinter.Toplevel())
        sf.setCallback(fun)

    def giveFilterResults(self):
        params = (self.varF0.get(),self.varFf.get(),)
        return auxProcessList(queryFechas,params)

class FumaSearch(AbstractSearchCriteria):
    def __init__(self,marco,modo):
        AbstractSearchCriteria.__init__(self,marco,modo)
        marcoF0 = Frame(marco,borderwidth=2, relief=RIDGE)
        lConfirmado = Label(marcoF0,text="Fuma")
        lConfirmado.pack()
        self.ajusta(marcoF0)
        pass
    def giveFilterResults(self):
        params = ('Tabaco',)
        return auxProcessList(queryFuma,params)

class MedicamentoSearch(AbstractSearchCriteria):
    def __init__(self,marco,modo):
        AbstractSearchCriteria.__init__(self,marco,modo)
        marcoF0 = Frame(marco,borderwidth=2, relief=RIDGE)
        lMedicamento= Label(marcoF0, text="Medicamento a buscar: ")
        self.medicamentoValues = StringVar()
        self.comboMedicamento = ttk.Combobox(marcoF0, textvariable=self.medicamentoValues,
                                state='readonly')
        # self.comboMedicamento['values'] = tuple(lista)
        lMedicamento.pack()
        self.comboMedicamento.pack()


        self.ajusta(marcoF0)

        pass

    def update(self,objToQuery):
        self.comboMedicamento['values'] = tuple(objToQuery.getMedList())


    def giveFilterResults(self): #Posible mejora de velocidad tener las id ya anotadas en lista
            medicamentoToSearch = self.comboMedicamento.get()
            params = (str(medicamentoToSearch),)
            return auxProcessList(queryMedicamento,params)
