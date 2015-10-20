__author__ = 'aferral'
import tkMessageBox

from SearchCriteria import askDb
from librerias.querys.queryList import queryFiltrarPaciente
from librerias.querys.queryList import queryAddPaciente
from librerias.querys.queryList import queryPacienteInfo
from librerias.querys.queryList import queryUpdatePaciente
from librerias.querys.queryList import queryDeletePaciente


def filtrarPaciente(runentry,pacienteCombo,statusValue):
    varRun = runentry.get().strip()
    whereString = ""
    params = (varRun,)
    if (varRun != ''):
        regex = "'^"+varRun+"'"
        whereString = whereString + ('WHERE CAST("RUN" AS TEXT) ~ '+regex)
    listRes = []
    try:
       listRes = askDb(queryFiltrarPaciente + whereString,params)
    except Exception, e:
        if statusValue :
            statusValue.set("Status: "+str(e))
    if len(listRes) == 0:
       listRes = ["No hay resultados"]
    else:
       for i in range(len(listRes)):
           listRes[i] = listRes[i][0]+","+str(listRes[i][1])+","+str(listRes[i][2])
    pacienteCombo['values'] = tuple(listRes)
    pacienteCombo.current(0)
    pass


def crearPaciente(boolsexo,runTvar,nombTvar,apeTvar,fechaTvar):
    varSexo = 'M'
    if boolsexo.get():
        if boolsexo.get() == 1:
            varSexo = 'H'
    varRun = runTvar.get().strip()
    varNombre = nombTvar.get().strip()
    varApellido = apeTvar.get().strip()
    varFecha = fechaTvar.get().strip()
    print "Comienzo CREACION paciente"
    print "Rut ",varRun
    print "nombre ",varNombre
    print "apellido ",varApellido
    print "Sexo ",str(varSexo)
    print "FechaNac ",varFecha
    params = (varSexo,varRun,varNombre,varApellido,varFecha,)
    try:
        askDb(queryAddPaciente,params)
        tkMessageBox.showinfo("Resultado","Status: "+"Paciente agregado")
    except Exception, e:
        print str(e)
        tkMessageBox.showinfo("Resultado","ERROR Status: "+str(e))
def updatePaciente(boolsexo,runTvar,nombTvar,apeTvar,fechaTvar):
    varSexo = 'M'
    if boolsexo.get():
        if boolsexo.get() == 1:
            varSexo = 'H'
    varRun = runTvar.get().strip()
    varNombre = nombTvar.get().strip()
    varApellido = apeTvar.get().strip()
    varFecha = fechaTvar.get().strip()
    print "Comienzo UPDATE paciente"
    print "Rut ",varRun
    print "nombre ",varNombre
    print "apellido ",varApellido
    print "Sexo ",str(varSexo)
    print "FechaNac ",varFecha
    params = (varFecha,varSexo,varRun,varNombre,varApellido,)
    try:
        askDb(queryUpdatePaciente,params)
        tkMessageBox.showinfo("Resultado","Status: "+"Informacion actualizada")
    except Exception, e:
        print str(e)
        tkMessageBox.showinfo("Resultado","ERROR Status: "+str(e))
    pass
def updateEntrys(varRun,varNom,varApe,varSex,varFec,varCurr):
    if len(varCurr.get().split(",")) > 2:
        listRes = varCurr.get().split(",")
        rut = listRes[2]
        nombre = listRes[0]
        apellidos = listRes[1]
        params = (rut,apellidos,nombre,)
        result = askDb(queryPacienteInfo,params)
        if len(result ) > 0:
            varRun.set(rut)
            varNom.set(nombre)
            varApe.set(apellidos)
            varSex.set(result[0][4] == 'H' )
            varFec.set(result[0][3].strftime('%Y-%m-%d'))

    pass
def deletePaciente(varCurr):
    if len(varCurr.get().split(",")) > 2:
        listRes = varCurr.get().split(",")
        rut = listRes[2]
        nombre = listRes[0]
        apellidos = listRes[1]
        params = (nombre,apellidos,rut,)
        try:
            askDb(queryDeletePaciente,params)
            tkMessageBox.showinfo("Resultado","Status: "+"Borrado exitoso")
        except Exception, e:
            print str(e)
            tkMessageBox.showinfo("Resultado","ERROR Status: "+str(e))
    pass