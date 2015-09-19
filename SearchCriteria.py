__author__ = 'aferral'
from Tkinter import *
import psycopg2
import ttk
from Calendar import *

queryIdRadio = 'Select "IdRadio" FROM "Radiografia" WHERE "IdRadio" = %s '
queryNombresPaciente = 'Select "IdRadio" FROM "Radiografia" WHERE "NombresPaciente" LIKE %s '
queryApellidosPaciente = 'Select "IdRadio" FROM "Radiografia" WHERE "ApellidosPaciente" LIKE %s '
queryRUN = 'Select "IdRadio" FROM "Radiografia" WHERE "RUNPaciente" = %s '
querySexoPaciente = 'SELECT "IdRadio" FROM "Radiografia" WHERE "Radiografia"."RUNPaciente" ' \
        'IN (SELECT "RUN" FROM "Paciente" WHERE "Sexo" = %s)'
queryEnfermedad = 'Select "IdRadio" FROM "Representa" WHERE ("NombreE" = %s AND "Confirmado" = %s)'
queryTipoRadio = 'Select "IdRadio" FROM "Radiografia" WHERE "Tipo" = %s'
queryFechas = 'Select "IdRadio" FROM "Radiografia" WHERE ("Fecha" > %s AND "Fecha" < %s)'
queryFuma = 'SELECT "IdRadio" FROM "En Contexto de" WHERE "IdAntecedentes" IN ' \
        '(SELECT "IdAntecedentes" FROM "Adiccion" JOIN "Sustancia" ON ("Adiccion"."IdSustancia" =' \
        ' "Sustancia"."IdSustancia")  WHERE ("NombreSustancia" = %s))'
queryMedicamento  = 'SELECT "IdRadio" FROM "En Contexto de" JOIN "Prescripcion Medica" ' \
                    'ON ("En Contexto de"."IdAntecedentes" = "Prescripcion Medica"."IdAntecedentes")' \
                    ' WHERE "IdMedicamento" IN (SELECT "Medicamento"."IdMedicamento" FROM "Prescripcion Medica"' \
                    ' JOIN "Medicamento" ON ("Medicamento"."IdMedicamento" = "Prescripcion Medica"."IdMedicamento")' \
                    ' WHERE "Medicamento"."NombreMedicamento" = %s) '

def askDb(stringQuery,params):
    result = []
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
        radio1 = Radiobutton(marco, text="M", variable=self.boolSexo, value=1)
        radio2 = Radiobutton(marco, text="H", variable=self.boolSexo, value=2)

        self.ajusta(lSexo)
        self.ajusta(radio1)
        self.ajusta(radio2)

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
        marcoSelEnf = Frame(marco)
        lEnfermedad= Label(marcoSelEnf, text="Enfermedad a buscar: ")
        self.enfermedadaValues = StringVar()
        self.comboEnfermedades = ttk.Combobox(marcoSelEnf, textvariable=self.enfermedadaValues,
                                state='readonly')
        # self.comboEnfermedades['values'] = tuple(lista)

        marcoConf = Frame(marco)
        self.varSi = IntVar()
        r1 = Radiobutton(marco, text="Confirmado", variable=self.varSi, value=1)
        r2 = Radiobutton(marco, text="Sospechoso", variable=self.varSi, value=2)


        self.ajusta(lEnfermedad)
        self.ajusta(self.comboEnfermedades)
        self.ajusta(marcoSelEnf)
        self.ajusta(r1)
        self.ajusta(r2)
        self.ajusta(marcoConf)

        pass

    def update(self,objToQuery):
        self.comboEnfermedades['values'] = tuple(objToQuery.getEnfList())

    def giveFilterResults(self):
        params = (str(self.comboEnfermedades.get()),'TRUE' if (self.varSi.get()==1) else 'FALSE',)
        return auxProcessList(queryEnfermedad, params)

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
        marcoF0 = Frame(marco)
        lFechaRadiografia= Label(marcoF0, text="Busqueda en rango desde DESDE : ")
        lFechaRadiografia.pack(side=LEFT)
        self.varF0 = StringVar()
        self.varF0.set('Today')
        self.lF0 = Label(marcoF0, textvariable = self.varF0)
        self.lF0.pack(side=LEFT)
        self.buttonF0 = Button(marcoF0,text="Cambiar", command= lambda: self.createWindowsAndBind(self.updateF0))
        self.buttonF0.pack(side=LEFT)

        self.ajusta(marcoF0)


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
        lConfirmado = Label(marco,text="Fuma ? ")
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