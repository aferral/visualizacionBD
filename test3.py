
import calendar
import Tkinter
import tkFont
from Tkinter import *

from SearchCriteria import askDb
import ttk
class VentanaDetalles(Tkinter.Frame):
    def __init__(self, *args, **kwargs):
        Tkinter.Frame.__init__(self, *args, **kwargs)

        #Frames
        self.vFrames = StringVar()
        self.lFramesStatic= Label(self,text="Frames: ")
        self.lFramesStatic.pack()
        self.lFrames = Label(self,textvariable=self.vFrames)
        self.lFrames.pack()

        #Alergico
        self.vAlergico = StringVar()
        self.lAlergicoStatic= Label(self,text="Alergias : ")
        self.lAlergicoStatic.pack()
        self.lAlergico = Label(self,textvariable=self.vAlergico)
        self.lAlergico.pack()

        #Adiccion
        self.vAdiccion = StringVar()
        self.lAdiccionStatic= Label(self,text="Adicciones : ")
        self.lAdiccionStatic.pack()
        self.lAdiccion = Label(self,textvariable=self.vAdiccion)
        self.lAdiccion.pack()

        #Intervencion
        self.vIntervencion = StringVar()
        self.lIntervencionStatic= Label(self,text="Intervencion : ")
        self.lIntervencionStatic.pack()
        self.lIntervencion = Label(self,textvariable=self.vIntervencion)
        self.lIntervencion.pack()

        #Medicamento
        self.vMedicamento = StringVar()
        self.lMedicamentoStatic= Label(self,text="Medicamento : ")
        self.lMedicamentoStatic.pack()
        self.lMedicamento = Label(self,textvariable=self.vMedicamento)
        self.lMedicamento.pack()

        #Trabajo
        self.vTrabajo = StringVar()
        self.lTrabajoStatic= Label(self,text="Trabajo : ")
        self.lTrabajoStatic.pack()
        self.lTrabajo = Label(self,textvariable=self.vTrabajo)
        self.lTrabajo.pack()

        #Otros
        self.vOtros = StringVar()
        self.lOtrosStatic= Label(self,text="Otros : ")
        self.lOtrosStatic.pack()
        self.lOtros = Label(self,textvariable=self.vOtros)
        self.lOtros.pack()

        #Paciente
        self.vPaciente = StringVar()
        self.lPacienteStatic= Label(self,text="Paciente : ")
        self.lPacienteStatic.pack()
        self.lPaciente = Label(self,textvariable=self.vPaciente)
        self.lPaciente.pack()

        self.pack()
        pass
    def setWindow(self,window):
        self.window = window
    def setValues(self,event):


        idRadio = self.window.getCurrentIdRadio()
        print "Doing "+str(idRadio)

        query = 'SELECT "NumOfFrame" FROM "Frames" WHERE "IdRadio" = %s'
        params = (idRadio,)
        stringRes = askDb(query,params)
        self.vFrames.set(stringRes)

        query = 'SELECT "NombreSustanciaAlergia" FROM "Alergico" JOIN "SustanciaAlergia" ON' \
                ' ("Alergico"."IdSustancia" = "SustanciaAlergia"."IdSustanciaAlergia") WHERE ' \
                '"IdAntecedentes" IN (SELECT "IdAntecedentes" FROM "En Contexto de"' \
                ' WHERE "IdRadio" = %s)'
        params = (idRadio,)
        stringRes = askDb(query,params)
        self.vAlergico.set(stringRes)

        query = 'SELECT "NombreSustanciaAdiccion" FROM "Adiccion" JOIN "SustanciaAdiccion" ON ' \
                '("Adiccion"."IdSustancia" = "SustanciaAdiccion"."IdSustanciaAdiccion") WHERE "IdAntecedentes"' \
                ' IN (SELECT "IdAntecedentes" FROM "En Contexto de" WHERE "IdRadio" = %s)'
        params = (idRadio,)
        stringRes = askDb(query,params)
        self.vAdiccion.set(stringRes)

        query = 'SELECT "FechaOperacion","NombreOperacion","DrOperacion" FROM "Intervencion" ' \
                ' WHERE "IdAntecedentes" IN (SELECT "IdAntecedentes" FROM "En Contexto de" WHERE "IdRadio" = %s)'
        params = (idRadio,)
        stringRes = askDb(query,params)
        self.vIntervencion.set(stringRes)

        query = 'SELECT "NombreMedicamento" FROM "Prescripcion Medica" JOIN "Medicamento" ON ' \
                '("Prescripcion Medica"."IdMedicamento" = "Medicamento"."IdMedicamento") WHERE ' \
                '"IdAntecedentes" IN (SELECT "IdAntecedentes" FROM "En Contexto de" WHERE "IdRadio" = %s)'
        params = (idRadio,)
        stringRes = askDb(query,params)
        self.vMedicamento.set(stringRes)

        query = 'SELECT "NombreTrabajo" FROM "Trabajo" WHERE "IdAntecedentes" IN ' \
                '(SELECT "IdAntecedentes" FROM "En Contexto de" WHERE "IdRadio" = %s)'
        params = (idRadio,)
        stringRes = askDb(query,params)
        self.vTrabajo.set(stringRes)

        query = 'SELECT "Comentario" FROM "Otros" WHERE "IdAntecedentes" IN ' \
                '(SELECT "IdAntecedentes" FROM "En Contexto de" WHERE "IdRadio" = %s)'
        params = (idRadio,)
        stringRes = askDb(query,params)
        self.vOtros.set(stringRes)

        query = 'SELECT "Paciente"."Nombres","Paciente"."Apellidos","Paciente"."RUN","Paciente"."FechaNac","Sexo" FROM' \
                ' "Radiografia" JOIN "Paciente" ON ("Paciente"."RUN" = "Radiografia"."RUNPaciente"' \
                ' AND "Paciente"."Nombres" = "Radiografia"."NombresPaciente" ' \
                ' AND "Paciente"."Apellidos" = "Radiografia"."ApellidosPaciente" ' \
                ') WHERE "IdRadio" = %s'
        params = (idRadio,)
        stringRes = askDb(query,params)
        self.vPaciente.set(stringRes)
        pass


