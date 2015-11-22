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
        lIdRadio = Label(marco, text="IdRadio")
        self.eIdRadio = Entry(marco)

        self.ajusta(lIdRadio)
        self.ajusta(self.eIdRadio)

    def giveFilterResults(self):
        idToSearch = self.eIdRadio.get()
        params = (str(idToSearch),)
        return auxProcessList(queryIdRadio,params)


class NameSearch(AbstractSearchCriteria):
    def __init__(self, marco,modo):
        AbstractSearchCriteria.__init__(self, marco,modo)
        lNombrePaciente = Label(marco, text="Nombre Paciente")
        self.eNombrePaciente = Entry(marco)

        self.ajusta(lNombrePaciente)
        self.ajusta(self.eNombrePaciente)

        pass

    def giveFilterResults(self):
        nameToSearch = "%"+self.eNombrePaciente.get()+"%"
        params = (str(nameToSearch),)
        return auxProcessList(queryNombresPaciente,params)
class LastNameSearch(AbstractSearchCriteria):
    def __init__(self, marco,modo):
        AbstractSearchCriteria.__init__(self, marco,modo)
        lApellidosPaciente = Label(marco, text="Apellido Paciente")
        self.eApellidoPaciente = Entry(marco)

        self.ajusta(lApellidosPaciente)
        self.ajusta(self.eApellidoPaciente)

        pass

    def giveFilterResults(self):
        nameToSearch = "%"+self.eApellidoPaciente.get()+"%"
        params = (str(nameToSearch),)
        return auxProcessList(queryApellidosPaciente,params)

class RutSearch(AbstractSearchCriteria):
    def __init__(self, marco,modo):
        AbstractSearchCriteria.__init__(self, marco,modo)
        lRutPaciente= Label(marco, text="Rut: ")
        self.eRutPaciente = Entry(marco)

        self.ajusta(lRutPaciente)
        self.ajusta(self.eRutPaciente)
        pass
    def giveFilterResults(self):
        rutToSearch = self.eRutPaciente.get()
        params = (str(rutToSearch),)
        return auxProcessList(queryRUN,params)

class SexoSearch(AbstractSearchCriteria):
    def __init__(self,marco,modo):
        AbstractSearchCriteria.__init__(self, marco,modo)
        lSexo= Label(marco, text="Sexo: ")

        self.boolSexo = IntVar()
        marcoF0 = Frame(marco)
        radio1 = Radiobutton(marcoF0, text="M", variable=self.boolSexo, value=1)
        radio1.pack(side=LEFT)
        radio2 = Radiobutton(marcoF0, text="H", variable=self.boolSexo, value=2)
        radio2.pack(side=RIGHT)

        self.ajusta(lSexo)
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
        lEnfermedad= Label(marco, text="Enfermedad a buscar: ")
        self.enfermedadaValues = StringVar()
        self.comboEnfermedades = ttk.Combobox(marco, textvariable=self.enfermedadaValues,
                                state='readonly')


        self.ajusta(lEnfermedad)
        self.ajusta(self.comboEnfermedades)

        pass

    def update(self,objToQuery):
        self.comboEnfermedades['values'] = tuple(objToQuery.getEnfList())

    def giveFilterResults(self):
        params = (str(self.comboEnfermedades.get()),)
        return auxProcessList(queryEnfermedadNombre, params)


class ConfirmadoSearch(AbstractSearchCriteria):
    def __init__(self, marco,modo):
        AbstractSearchCriteria.__init__(self,marco,modo)
        self.varSi = IntVar()
        marcoF0 = Frame(marco)
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
        lTipoRadiografia= Label(marco, text="Tipo de radiografia: ")
        self.tipoRadiografiaValues = StringVar()
        comboTipoRadiografia = ttk.Combobox(marco, textvariable=self.tipoRadiografiaValues,
                                state='readonly')
        comboTipoRadiografia['values'] = ('Radiografia', 'Escaner', 'Resonancia')


        self.ajusta(lTipoRadiografia)
        self.ajusta(comboTipoRadiografia)

        pass
    def giveFilterResults(self):

        params = (str(self.tipoRadiografiaValues.get()),)
        return auxProcessList(queryTipoRadio,params)

class FechaSearch(AbstractSearchCriteria): # Va rango de fechas
    def __init__(self,marco,modo):
        AbstractSearchCriteria.__init__(self,marco,modo)

        #Fecha inicio
        
        lFechaRadiografia= Label(marco, text="Busqueda en rango:")
        marcoF0 = Frame(marco)
        self.varF0 = StringVar()
        self.varF0.set('Today')
        self.lF1 = Label(marcoF0, text = "DESDE:")
        self.lF1.pack(side=LEFT)
        self.lF0 = Label(marcoF0, textvariable = self.varF0)
        self.lF0.pack(side=LEFT)
        self.buttonF0 = Button(marcoF0,text="Cambiar", command= lambda: self.createWindowsAndBind(self.updateF0))
        self.buttonF0.pack(side=LEFT)
        self.ajusta(lFechaRadiografia)
        self.ajusta(marcoF0)


        marcoFf = Frame(marco)

        #Fecha final
        lFechaRadiografiaFin= Label(marcoFf, text="HASTA : ")
        lFechaRadiografiaFin.pack(side=LEFT)
        self.varFf = StringVar()
        self.varFf.set('Tomorrow')
        self.lFf = Label(marcoFf, textvariable = self.varFf)
        self.lFf.pack(side=LEFT)
        self.buttonFf = Button(marcoFf,text="Cambiar", command= lambda: self.createWindowsAndBind(self.updateFf))
        self.buttonFf.pack(side=LEFT)

        self.ajusta(marcoFf)
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
        lConfirmado = Label(marco,text="Fuma")
        self.ajusta(lConfirmado)
        pass
    def giveFilterResults(self):
        params = ('Tabaco',)
        return auxProcessList(queryFuma,params)

class MedicamentoSearch(AbstractSearchCriteria):
    def __init__(self,marco,modo):
        AbstractSearchCriteria.__init__(self,marco,modo)

        lMedicamento= Label(marco, text="Medicamento a buscar: ")
        self.medicamentoValues = StringVar()
        self.comboMedicamento = ttk.Combobox(marco, textvariable=self.medicamentoValues,
                                state='readonly')
        # self.comboMedicamento['values'] = tuple(lista)

        self.ajusta(lMedicamento)
        self.ajusta(self.comboMedicamento)

        pass

    def update(self,objToQuery):
        self.comboMedicamento['values'] = tuple(objToQuery.getMedList())


    def giveFilterResults(self): #Posible mejora de velocidad tener las id ya anotadas en lista
            medicamentoToSearch = self.comboMedicamento.get()
            params = (str(medicamentoToSearch),)
            return auxProcessList(queryMedicamento,params)
