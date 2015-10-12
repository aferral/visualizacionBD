import Tkinter
from Tkinter import *

from librerias.SearchCriteria import askDb

queryFrames = 'SELECT "NumOfFrame" FROM "Frames" WHERE "IdRadio" = %s'

queryAlergia = 'SELECT "NombreSustanciaAlergia" FROM "Alergico" JOIN "SustanciaAlergia" ON' \
                ' ("Alergico"."IdSustancia" = "SustanciaAlergia"."IdSustanciaAlergia") WHERE ' \
                '"IdAntecedentes" IN (SELECT "IdAntecedentes" FROM "En Contexto de"' \
                ' WHERE "IdRadio" = %s)'
queryAdiccion = 'SELECT "NombreSustanciaAdiccion" FROM "Adiccion" JOIN "SustanciaAdiccion" ON ' \
                '("Adiccion"."IdSustancia" = "SustanciaAdiccion"."IdSustanciaAdiccion") WHERE "IdAntecedentes"' \
                ' IN (SELECT "IdAntecedentes" FROM "En Contexto de" WHERE "IdRadio" = %s)'

queryOperacion = 'SELECT "FechaOperacion","NombreOperacion","DrOperacion" FROM "Intervencion" ' \
                ' WHERE "IdAntecedentes" IN (SELECT "IdAntecedentes" FROM "En Contexto de" WHERE "IdRadio" = %s)'

queryMed = 'SELECT "NombreMedicamento" FROM "Prescripcion Medica" JOIN "Medicamento" ON ' \
                '("Prescripcion Medica"."IdMedicamento" = "Medicamento"."IdMedicamento") WHERE ' \
                '"IdAntecedentes" IN (SELECT "IdAntecedentes" FROM "En Contexto de" WHERE "IdRadio" = %s)'

queryTrabajo = 'SELECT "NombreTrabajo" FROM "Trabajo" WHERE "IdAntecedentes" IN ' \
                '(SELECT "IdAntecedentes" FROM "En Contexto de" WHERE "IdRadio" = %s)'

queryComentario = 'SELECT "Comentario" FROM "Otros" WHERE "IdAntecedentes" IN ' \
                '(SELECT "IdAntecedentes" FROM "En Contexto de" WHERE "IdRadio" = %s)'

queryPaciente = 'SELECT "Paciente"."Nombres","Paciente"."Apellidos","Paciente"."RUN","Paciente"."FechaNac","Sexo" FROM' \
                ' "Radiografia" JOIN "Paciente" ON ("Paciente"."RUN" = "Radiografia"."RUNPaciente"' \
                ' AND "Paciente"."Nombres" = "Radiografia"."NombresPaciente" ' \
                ' AND "Paciente"."Apellidos" = "Radiografia"."ApellidosPaciente" ' \
                ') WHERE "IdRadio" = %s'

class Bloque(Tkinter.Frame):

    def __init__(self,nombre,query,master, **kwargs):


        Frame.__init__(self, master, **kwargs)

        self.vString = StringVar()
        localLabel = Label(self,text=nombre+": ")
        localLabel.pack()
        self.localLabelShow = Label(self,textvariable=self.vString)
        self.localLabelShow.pack()
        self.query = query

        self.pack()
        pass
    def update(self,idRadio):
        params = (idRadio,)
        listaRes = askDb(self.query,params)
        stringout = ""
        for elem in listaRes:
            for contenido in elem:
                stringout+=str(contenido).strip()+"\n"
        self.vString.set(stringout)
        pass


class VentanaDetalles(Tkinter.Frame):
    def __init__(self, *args, **kwargs):
        Tkinter.Frame.__init__(self, *args, **kwargs)
        self.lista = []

                #Frames
        self.lista.append(Bloque("Frames", queryFrames, self))
        #Alergico
        self.lista.append(Bloque("Alergias", queryAlergia, self))

        #Adiccion
        self.lista.append(Bloque("Adicciones", queryAdiccion, self))

        #Intervencion
        self.lista.append(Bloque("Intervencion", queryOperacion, self))

        #Medicamento
        self.lista.append(Bloque("Medicamento", queryMed, self))

        #Trabajo
        self.lista.append(Bloque("Trabajo", queryTrabajo, self))

        #Otros
        self.lista.append(Bloque("Otros", queryComentario, self))

        #Paciente
        self.lista.append(Bloque("Paciente", queryPaciente, self))

        self.pack()
        pass


    def setWindow(self,window):
        self.window = window
    def setValues(self,event):

        idRadio = self.window.getCurrentIdRadio()

        for bloque in self.lista:
            bloque.update(idRadio)
        pass


