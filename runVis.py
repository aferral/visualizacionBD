__author__ = 'aferral'


from Tkinter import *
import ttk
from tkintertable.Tables import TableCanvas
from tkintertable.TableModels import TableModel

r = Tk()
r.wm_title("Ventana de busqueda")
marco00=Frame(r)
lTextoEntrada = Label(marco00, text="Ventana de busqueda")
lTextoEntrada.pack()
lIdRadio = Label(marco00, text="IdRadio")
lIdRadio.pack(side=LEFT)
eIdRadio = Entry(marco00)
eIdRadio.pack(side=LEFT)

marco00.grid(row=0,column=0)


marco01=Frame(r)

lNombrePaciente = Label(marco01, text="Nombre Paciente")
lNombrePaciente.pack(side=LEFT)
eNombrePaciente = Entry(marco01)
eNombrePaciente.pack(side=LEFT)


marco01.grid(row=1,column=0)


#Rut
marco02=Frame(r)

lRutPaciente= Label(marco02, text="Rut: ")
lRutPaciente.pack(side=LEFT)
eRutPaciente = Entry(marco02)
eRutPaciente.pack(side=LEFT)


marco02.grid(row=2,column=0)
#Sexo

marco03=Frame(r)
lSexo= Label(marco03, text="Sexo: ")
lSexo.pack(side=LEFT)
boolSexo = False;
Radiobutton(marco03, text="M", variable=boolSexo, value=1).pack(anchor=W)
Radiobutton(marco03, text="H", variable=boolSexo, value=2).pack(anchor=W)


marco03.grid(row=3,column=0)

#Enfermedad comboBox

marco04=Frame(r)
lEnfermedad= Label(marco04, text="Enfermedad a agregar: ")
lEnfermedad.pack(side=LEFT)
enfermedadaValues = StringVar()
comboEnfermedades = ttk.Combobox(marco04, textvariable=enfermedadaValues,
                        state='readonly')
comboEnfermedades['values'] = ('A', 'B', 'C')
comboEnfermedades.current(0)
comboEnfermedades.pack()
marco04.grid(row=4,column=0)

#Tipo de radiografia
marco05=Frame(r)
lTipoRadiografia= Label(marco05, text="Tipo de radiografia: ")
lTipoRadiografia.pack(side=LEFT)
tipoRadiografiaValues = StringVar()
comboTipoRadiografia = ttk.Combobox(marco05, textvariable=tipoRadiografiaValues,
                        state='readonly')
comboTipoRadiografia['values'] = ('A', 'B', 'C')
comboTipoRadiografia.current(0)
comboTipoRadiografia.pack()
marco05.grid(row=5,column=0)

#Fecha inicio fecha final
marco06=Frame(r)
lFechaRadiografia= Label(marco06, text="Busqueda en rango desde DESDE : ")
lFechaRadiografia.pack(side=LEFT)


#Intervalo inicio
#Dia
fechaDiaValues = StringVar()
comboDiaInicio = ttk.Combobox(marco06, textvariable=fechaDiaValues,
                        state='readonly')
comboDiaInicio['values'] = ('A', 'B', 'C')
comboDiaInicio.current(0)
comboDiaInicio.pack(side=LEFT)

#mes
fechaMesValues = StringVar()
comboMesInicio = ttk.Combobox(marco06, textvariable=fechaMesValues,
                        state='readonly')
comboMesInicio['values'] = ('A', 'B', 'C')
comboMesInicio.current(0)
comboMesInicio.pack(side=LEFT)

#ano
fechaAnoValues = StringVar()
comboAnoInicio = ttk.Combobox(marco06, textvariable=fechaAnoValues,
                        state='readonly')
comboAnoInicio['values'] = ('A', 'B', 'C')
comboAnoInicio.current(0)
comboAnoInicio.pack(side=LEFT)

marco06.grid(row=6,column=0)


#Fecha final
marco07=Frame(r)
lFechaRadiografiaFin= Label(marco07, text="Busqueda en rango HASTA : ")
lFechaRadiografiaFin.pack(side=LEFT)


#Intervalo fin
#Dia

comboDiaFin = ttk.Combobox(marco07, textvariable=fechaDiaValues,
                        state='readonly')
comboDiaFin['values'] = ('A', 'B', 'C')
comboDiaFin.current(0)
comboDiaFin.pack(side=LEFT)

#mes
comboMesFin = ttk.Combobox(marco07, textvariable=fechaMesValues,
                        state='readonly')
comboMesFin['values'] = ('A', 'B', 'C')
comboMesFin.current(0)
comboMesFin.pack(side=LEFT)

#ano
comboAnoFin= ttk.Combobox(marco07, textvariable=fechaAnoValues,
                        state='readonly')
comboAnoFin['values'] = ('A', 'B', 'C')
comboAnoFin.current(0)
comboAnoFin.pack(side=LEFT)

marco07.grid(row=7,column=0)

#Confirmado
marco08 = Frame(r)
lConfirmado = Label(marco08,text="Confirmado ? ")
lConfirmado.pack(side=LEFT)
varSi = IntVar()
varSospechoso = IntVar()
c = Checkbutton(marco08, text="Si", variable=varSi)
c.pack(side=LEFT)
c = Checkbutton(marco08, text="Sospechoso", variable=varSospechoso)
c.pack(side=LEFT)
marco08.grid(row=8,column=0)

#Fuma
marco09 = Frame(r)
lConfirmado = Label(marco09,text="Fuma ? ")
lConfirmado.pack(side=LEFT)
varSi = IntVar()
varSospechoso = IntVar()
c = Checkbutton(marco09, text="Si", variable=varSi)
c.pack(side=LEFT)
c = Checkbutton(marco09, text="No", variable=varSospechoso)
c.pack(side=LEFT)
marco09.grid(row=9,column=0)


#Medicamento
marco10 = Frame(r)
marco10.grid(row=10,column=0)

#Mostrar resultados
marco11 = Frame(r)
lResultados = Label(marco11,text="Resultados de query: ")
lResultados.pack()
bExportExcel = Button(marco11, text="Exportar a excel")
bExportExcel.pack()
marco11.grid(row=11,column=0)

marco12 = Frame(r)
model = TableModel()
data = {'fila': {'col22':22,'col2':245,'col3':587,'col4':999},'fila2':{'col1':223,'col2':44,'col3':55,'col4':66}}
model.importDict(data)
table = TableCanvas(marco12, model,
                    cellwidth=60, cellbackgr='#e3f698',
                    thefont=('Arial',12),rowheight=18, rowheaderwidth=30,
                    rowselectedcolor='yellow', editable=True)
table.createTableFrame()
marco12.grid(row=12,column=0)



r.mainloop()