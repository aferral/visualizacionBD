__author__ = 'aferral'
from Tkinter import *
import psycopg2
import ttk
from Calendar import *

def askDb(stringQuery,params):

    conn = psycopg2.connect(database='radiografiasUchile',
                            host='localhost',
                            port=5432 ,
                            password = '58132154',
                            user='postgres')

    cursor = conn.cursor()
    print "String Query : ",stringQuery
    print "Params ",params
    cursor.execute(stringQuery,params)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    print "Result: ",result
    return result

def auxProcessList(StringQuery,param):
    try:
        params = (str(param),)
        listRes =  askDb(StringQuery,params)

        for i in range(len(listRes)):
            listRes[i] = listRes[i][0]
        return listRes
    except :
        return []

class AbstractSearchCriteria(object):
    def __init__(self,marco):
        self.active = IntVar()
        c = Checkbutton(marco, variable=self.active)
        c.pack(side=LEFT)

        pass
    def isActive(self):
        return self.active.get()
    def giveFilterResults(self):
        return []

class IdSearch(AbstractSearchCriteria):
    def __init__(self,marco):
        AbstractSearchCriteria.__init__(self, marco)
        lIdRadio = Label(marco, text="IdRadio")
        lIdRadio.pack(side=LEFT)
        self.eIdRadio = Entry(marco)
        self.eIdRadio.pack(side=LEFT)
        pass
    def giveFilterResults(self):
        query = 'Select "IdRadio" FROM "Radiografia" WHERE "IdRadio" = %s '
        idToSearch = self.eIdRadio.get()
        return auxProcessList(query,idToSearch)



class NameSearch(AbstractSearchCriteria):
    def __init__(self,marco):
        AbstractSearchCriteria.__init__(self, marco)
        lNombrePaciente = Label(marco, text="Nombre Paciente")
        lNombrePaciente.pack(side=LEFT)
        self.eNombrePaciente = Entry(marco)
        self.eNombrePaciente.pack(side=LEFT)
        pass

    def giveFilterResults(self):
        query = 'Select "IdRadio" FROM "Pertenece a" WHERE "Nombre" % %s '
        nameToSearch = self.eNombrePaciente.get()
        return auxProcessList(query,nameToSearch)

class RutSearch(AbstractSearchCriteria):
    def __init__(self, marco):
        AbstractSearchCriteria.__init__(self, marco)
        lRutPaciente= Label(marco, text="Rut: ")
        lRutPaciente.pack(side=LEFT)
        self.eRutPaciente = Entry(marco)
        self.eRutPaciente.pack(side=LEFT)
        pass
    def giveFilterResults(self):
        query = 'Select "IdRadio" FROM "Pertenece a" WHERE "RUN" = %s '
        rutToSearch = self.eRutPaciente.get()
        return auxProcessList(query,rutToSearch)

class SexoSearch(AbstractSearchCriteria):
    def __init__(self,marco):
        AbstractSearchCriteria.__init__(self, marco)
        lSexo= Label(marco, text="Sexo: ")
        lSexo.pack(side=LEFT)
        self.boolSexo = IntVar()
        Radiobutton(marco, text="M", variable=self.boolSexo, value=1).pack(anchor=W)
        Radiobutton(marco, text="H", variable=self.boolSexo, value=2).pack(anchor=W)
        pass
    def giveFilterResults(self):
        query = 'SELECT "IdRadio" FROM "Pertenece a" WHERE "Pertenece a"."RUN" IN (SELECT "RUN" FROM "public"."Paciente" WHERE "Sexo" = %s)'
        valRadio = self.boolSexo.get()
        if valRadio == 1: #Es mujer buscar todas
            param = ""'M'""
            return auxProcessList(query,param)
        elif valRadio == 2:
            param = ""'H'""
            return auxProcessList(query,param)
        else:
            return []

class Enfermedadearch(AbstractSearchCriteria): #Va enfermedad y confirmado
    def __init__(self,marco,lista):
        AbstractSearchCriteria.__init__(self,marco)
        marcoSelEnf = Frame(marco)
        lEnfermedad= Label(marcoSelEnf, text="Enfermedad a buscar: ")
        lEnfermedad.pack(side=LEFT)
        self.enfermedadaValues = StringVar()
        self.comboEnfermedades = ttk.Combobox(marcoSelEnf, textvariable=self.enfermedadaValues,
                                state='readonly')
        self.comboEnfermedades['values'] = tuple(lista)
        self.comboEnfermedades.current(0)
        self.comboEnfermedades.pack()
        marcoSelEnf.pack()

        marcoConf = Frame(marco)
        self.varSi = IntVar()
        self.varSospechoso = IntVar()
        Radiobutton(marco, text="Confirmado", variable=self.varSi, value=1).pack(anchor=W)
        Radiobutton(marco, text="Sospechoso", variable=self.varSi, value=2).pack(anchor=W)

        marcoConf.pack()

        pass

    def update(self,objToQuery):
        self.comboEnfermedades['values'] = tuple(objToQuery.getEnfList())
        self.comboEnfermedades.current(0)

class TipoRadioSearch(AbstractSearchCriteria):
    def __init__(self,marco):
        AbstractSearchCriteria.__init__(self,marco)
        lTipoRadiografia= Label(marco, text="Tipo de radiografia: ")
        lTipoRadiografia.pack(side=LEFT)
        tipoRadiografiaValues = StringVar()
        comboTipoRadiografia = ttk.Combobox(marco, textvariable=tipoRadiografiaValues,
                                state='readonly')
        comboTipoRadiografia['values'] = ('Radiografia', 'Escaner', 'Resonancia')
        comboTipoRadiografia.current(0)
        comboTipoRadiografia.pack()

        pass

class FechaSearch(AbstractSearchCriteria): # Va rango de fechas
    def __init__(self,marco):
        AbstractSearchCriteria.__init__(self,marco)

        #Fecha inicio
        marcoF0 = Frame(marco)

        lFechaRadiografia= Label(marcoF0, text="Busqueda en rango desde DESDE : ")
        lFechaRadiografia.pack(side=LEFT)
        self.varF0 = StringVar()
        self.varF0.set('Today')
        self.lF0 = Label(marcoF0, textvariable = self.varF0)
        self.lF0.pack(side=LEFT)
        self.buttonF0 = Button(marcoF0,text="Cambiar", command= lambda: self.createWindowsAndBind(self.updateF0))
        self.buttonF0.pack(side=LEFT)

        marcoF0.pack()


        marcoFf = Frame(marco)

        #Fecha final
        lFechaRadiografiaFin= Label(marcoFf, text="Busqueda en rango HASTA : ")
        lFechaRadiografiaFin.pack(side=LEFT)
        self.varFf = StringVar()
        self.varFf.set('Tomorrow')
        self.lFf = Label(marcoFf, textvariable = self.varFf)
        self.lFf.pack(side=LEFT)
        self.buttonFf = Button(marcoFf,text="Cambiar", command= lambda: self.createWindowsAndBind(self.updateFf))
        self.buttonFf.pack(side=LEFT)

        marcoFf.pack()
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


class FumaSearch(AbstractSearchCriteria):
    def __init__(self,marco):
        AbstractSearchCriteria.__init__(self,marco)
        lConfirmado = Label(marco,text="Fuma ? ")
        lConfirmado.pack(side=LEFT)

        self.boolFuma = IntVar()
        Radiobutton(marco, text="Si", variable=self.boolFuma, value=1).pack(anchor=W)
        Radiobutton(marco, text="No", variable=self.boolFuma, value=2).pack(anchor=W)

        pass

class MedicamentoSearch(AbstractSearchCriteria):
    def __init__(self,marco,lista):
        AbstractSearchCriteria.__init__(self,marco)

        lMedicamento= Label(marco, text="Medicamento a buscar: ")
        lMedicamento.pack(side=LEFT)
        self.medicamentoValues = StringVar()
        self.comboMedicamento = ttk.Combobox(marco, textvariable=self.medicamentoValues,
                                state='readonly')
        self.comboMedicamento['values'] = tuple(lista)
        self.comboMedicamento.current(0)
        self.comboMedicamento.pack()

        pass

    def update(self,objToQuery):
        self.comboMedicamento['values'] = tuple(objToQuery.getMedList())
        self.comboMedicamento.current(0)