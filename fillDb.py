# Este script tiene como objetivo llenar una base de datos sql

import paramiko
import psycopg2
from dateutil.relativedelta import relativedelta

import json
import random
import datetime

# Requiero una lista de nombres

nombreslist = ["andres", "roberto", "pedro", "raul", "gonzalo", "raquel", "marta", "maria",
               "fulano", "mengano", "fulana", "juan", "jaime", "sebastian", "esperanza", "mirta", "maitte",
               "laura", "Armando"]
apellidolist = ["Ferrada", "Alvarez", "Mesa", "Casa", "Rodriguez", "Arroyo",
                "Arsenault", "Ortega", "Ferrari", "Romero", "Carrillo", "Escalona", "Bravo"
]
# Requiero una lista de enfermedades
nombreEnfermedadList = ["Actinomicosis", "Adenocarcinoma pulmonar", "Adenopatias", "Adenovirus", "Amiloidosis",
                        "Amiodarona", "Anemia", "Aneurisma", "Aneurisma aortico", "Aplasia medular", "AR",
                        "Arbol en brote", "Arteritis de Takayasu", "Artritis septica", "Artrosis", "Asbestosis", "Asma",
                        "Aspergiloma", "Aspergilosis", "Atelectasia", "Atelectasia redonda", "BALT", "Barotrauma",
                        "Beriliosis", "Bocio ", "Broncocele", "Bronquiectasias", "Bronquio accesorio",
                        "Bronquiolitis constrictiva", "Bronquiolitis infecciosa", "Bronquiolitis respiratoria", "Bula",
                        "Calcificacion metastasica", "Candida","Chlamidia pn"]

evolucionEnfermedadList = ["temprana", "latente", "recaida", "incubacion",
                           "terminal", "avanzada"
]
agudezaEnfermedadLista = ["leve", "grave", "aguda", "media"
]


#Requiero una lista de antecedentes
# Estos incluyen alergico, adiccion

# sustancias droga
sustanciasDrogaList = [
    "Tabaco", "Alcohol", "Cocaina", "Crack", "PastaBase",
]
# sustancias alergias
sustanciasList = [
    "Mani", "Nueces", "Leche", "Huevos", "Chocolate",
]

# intervenciones varias
intervencionLista = [
    "Apendicitis", "Amigdalitis", "Inflamacion de colon",
    "Cirujia plastica", "Rinoplastia"]

# medicamentos varios
mediLista = ["Irbesartan", "Irinotecan", "Isoniazida",
             "Isosorbide", "Itraconazol", "Ivermectina", "Jalea lubricante",
             "Ketamina", "Ketoconazol", "Lactulosa", "Lamivudina", "Lamotrigina",
             "Lansoprazol", "Latanoprost", "Laxante para enema", "L-Carnitina",
             "Leflunomida", "Letrozol", "Leucovorina", "Leuprolida",
             "Leuprorelina",
             "Levobupivacaina",
             "Levodopa con carbidopa",
             "Levofloxacino",
             "Levomepromazina",
             "Levonorgestrel",
             "Levotiroxina",
             "Lidocaina",
             "Liotironina",
             "Litio carbonato",
             "Lomefloxacino",
             "Loperamida",
             "Lopinavir con ritonavir",
             "Loratadina",
             "Lorazepam",
             "Lovastatina",
             "Lugol",
             "Magnesio hidroxido",
             "Magnesio sulfato",
             "Manitol",
             "Mebrofenina",
             "Medroxiprogesterona",
             "Meglumina antimoniato"
             "Melfalano",
             "Menotropins",
             "Mepivacaina",
             "Mercaptopurina",
             "Meropenem",
             "Mesalamina"
             "Mesalazina",
             "Mesna"
]


# prescripcion medicamentos

# radiografia
zonaLista = ["Torax", "Femur", "Craneo", "Pelvis", "Brazo"]
procedenciaLista = ["Ambulatorio", "Urgencias"]
tipoLista = ["Radiografia", "Escaner", "Resonancia"]

# trabajo
trabajoLista = ["Obrero", "Contador", "Doctor", "Bombero", "Profesor",
                "Ingeniero", "Deportista Olimpico", "Vendedor Informal", "Militar", "Carabinero"]


def giveRut():
    return random.randint(10000000, 19999999);


def sendDb(query, params):
    conn = psycopg2.connect(database="database10000", host="localhost", port=5432, password="58132154",
                            user="postgres")
    cursor = conn.cursor();
    cursor.execute(query, params);
    try:
        res = cursor.fetchall();
    except:
        res = ""
    conn.commit();
    cursor.close();
    conn.close();

    return res


def randomDate():
    dateIni = datetime.datetime(1950, 01, 01);
    dateIni = dateIni + relativedelta(months=random.randint(0, 11))
    dateIni = dateIni + relativedelta(years=random.randint(0, 55))
    dateIni = dateIni + datetime.timedelta(days=random.randint(0, 29))
    return dateIni


sexo = ["M", "H"];


def generarPacientes(cantidad):
    for i in range(cantidad):
        query = 'INSERT INTO "Paciente" ("Nombres",' \
                '"Apellidos",' \
                '"RUN", "FechaNac" ,' \
                '"Sexo",' \
                '"Peso",' \
                '"Altura" ) VALUES (%s,%s,%s,%s,%s,%s,%s)'
        #Baja probabilidad pero existente de choque rut,nombre debe ser unico
        nombres = random.choice(nombreslist)
        apellidos = random.choice(apellidolist) + " " + random.choice(apellidolist)
        date = randomDate().strftime('%Y-%m-%d')
        rutRand = giveRut();
        params = (nombres, apellidos, rutRand, date, random.choice(sexo),
                  random.randint(50, 150), random.randint(150, 230))
        sendDb(query, params)


def generarSustanciasAlergia():
    for sus in sustanciasList:
        query = 'INSERT INTO "SustanciaAlergia" ("IdSustanciaAlergia",' \
                '"NombreSustanciaAlergia" ' \
                ') VALUES (DEFAULT,%s)'
        params = (sus,)
        sendDb(query, params)


def generarSustanciasDroga():
    for sus in sustanciasDrogaList:
        query = 'INSERT INTO "SustanciaAdiccion" ("IdSustanciaAdiccion",' \
                '"NombreSustanciaAdiccion" ' \
                ') VALUES (DEFAULT,%s)'
        params = (sus,)

        sendDb(query, params)


#Aca ajustar a solo nombre
def generarEnfermedades():
    agregado = []
    for enf in nombreEnfermedadList:
        query = 'INSERT INTO "Enfermedad" ("NombreE" ' \
                ') VALUES (%s)'
        params = (enf, )
        if (params in agregado):
            continue
        agregado.append(params)

        sendDb(query, params)


#Podria buscar ya agregado de una mejor forma
def generarRadiografias(cantidad):
    agregado = []
    for i in range(cantidad):
        query = 'INSERT INTO "Radiografia" ("IdRadio",' \
                '"Fecha", "Zona" ,' \
                '"Procedencia","Tipo", ' \
                '"RUNPaciente", "NombresPaciente" ,' \
                ' "ApellidosPaciente" ' \
                ') VALUES (DEFAULT,%s,%s,%s,%s,%s,%s,%s)'
        fecha = randomDate().strftime('%Y-%m-%d');
        zone = random.choice(zonaLista);
        proc = random.choice(procedenciaLista);
        tip = random.choice(tipoLista);

        query2 = 'SELECT "Nombres", "RUN","Apellidos" ' \
        ' FROM "Paciente" ORDER BY RANDOM() LIMIT 1'
        result = sendDb(query2,'')
        (nombres, rut,apellidos) = result[0]


        params = ( fecha, zone, proc, tip,rut,nombres,apellidos)
        if (params in agregado):
            continue
        agregado.append(params)

        sendDb(query, params)


def generarTrabajos():

    for trabajo in trabajoLista:
        query2 = 'INSERT INTO "Antecedentes" ("IdAntecedentes") ' \
                 'VALUES (DEFAULT) RETURNING "IdAntecedentes";'
        idJustAdded = sendDb(query2, '')[0][0]
        query1 = 'INSERT INTO "Trabajo" ("IdAntecedentes", ' \
                 '"NombreTrabajo") VALUES (%s, %s) '
        params = (idJustAdded,trabajo,)
        sendDb(query1,params)


def generarMedicamentos():

    for med in mediLista:
        query = 'INSERT INTO "Medicamento" ("IdMedicamento","NombreMedicamento" ' \
                ') VALUES (DEFAULT,%s)'

        params = ( med,)

        sendDb(query, params)

#Que mejor se haga una busqueda de relacicon radiografia, enfermedad y de ahi agregar frames
def generarFrames():


    #Generar frames
    # Consigue lista de radiografias con enfermedad
    query = 'SELECT "IdRadio" FROM "Representa" '
    res = sendDb(query,'')


    for elem in res:
        idRadio = elem[0]
        query = 'INSERT INTO "Frames" ("IdRadio","NumOfFrame") ' \
                ' VALUES (%s,%s)'
        params = (idRadio, random.randint(1, 100))
        sendDb(query, params)

#generarFrames()



#Requiero uno que tome todas las radiografias con enfermedades y les de
#Tome random los antecedentes a agregar
#Generar intervenciones que sea individual
def generaraUnIntervencion():


    query2 = 'INSERT INTO "Antecedentes" ("IdAntecedentes") ' \
             'VALUES (DEFAULT) RETURNING "IdAntecedentes";'
    idJustAdded = sendDb(query2, '')[0][0]

    query = 'INSERT INTO "Intervencion" ("IdAntecedentes", "FechaOperacion", ' \
            ' "NombreOperacion", "DrOperacion" ) VALUES (%s,%s,%s,%s)'
    fec = randomDate().strftime('%Y-%m-%d');
    nombreop = random.choice(intervencionLista);
    dr = nombre = random.choice(nombreslist) + " " + \
                  random.choice(apellidolist) + " " + random.choice(apellidolist)
    params = (idJustAdded, fec, nombreop, dr)
    sendDb(query, params)
    return idJustAdded

#Generar adiccion

def generaraUnAdiccion(lownSustancias,upSustancias):
    query2 = 'INSERT INTO "Antecedentes" ("IdAntecedentes") ' \
             'VALUES (DEFAULT) RETURNING "IdAntecedentes";'
    idJustAdded = sendDb(query2, '')[0][0]

    query = 'INSERT INTO "Adiccion" ("IdAntecedentes", "IdSustancia", ' \
            ' "Meses" ) VALUES (%s,%s,%s)'
    idsus = random.randint(lownSustancias, upSustancias)
    mess = random.randint(1, 100);
    params = (idJustAdded, idsus, mess)
    sendDb(query, params)

    return idJustAdded

#generaraUnAdiccion(1,5)

#Generar alergico
def generaraUnAlergico(lownSustancias,upSustancias):
    query2 = 'INSERT INTO "Antecedentes" ("IdAntecedentes") ' \
             'VALUES (DEFAULT) RETURNING "IdAntecedentes";'
    idJustAdded = sendDb(query2, '')[0][0]

    query = 'INSERT INTO "Alergico" ("IdAntecedentes", "IdSustancia" ' \
            ' ) VALUES (%s,%s)'
    idsus = random.randint(lownSustancias, upSustancias)
    params = (idJustAdded, idsus, )
    sendDb(query, params)

    return idJustAdded
#generaraUnAlergico(1,5)

#Asociar Trabajo con Idantecedentes
def generarTrabajo():
    query2 = 'INSERT INTO "Antecedentes" ("IdAntecedentes") ' \
             'VALUES (DEFAULT) RETURNING "IdAntecedentes";'
    idJustAdded = sendDb(query2, '')[0][0]

    query = 'INSERT INTO "Trabajo" ("IdAntecedentes", "NombreTrabajo" ' \
            ' ) VALUES (%s,%s)'

    tra = random.choice(trabajoLista);
    params = (idJustAdded, tra)
    sendDb(query, params)

    return idJustAdded
#generarTrabajo()

#Generar prescipcion medica
def generarMedPres():
    query2 = 'INSERT INTO "Antecedentes" ("IdAntecedentes") ' \
             'VALUES (DEFAULT) RETURNING "IdAntecedentes";'
    idJustAdded = sendDb(query2, '')[0][0]

    query = 'SELECT "IdMedicamento" FROM "Medicamento" ORDER BY RANDOM() LIMIT 1'
    medRandom = sendDb(query, '')[0]

    query = 'INSERT INTO "Prescripcion Medica" ("IdAntecedentes", "IdMedicamento" ' \
            ' ) VALUES (%s,%s)'

    params = (idJustAdded, medRandom,)
    sendDb(query, params)

    return idJustAdded
#generarMedPres()

#Genera en contexto de antecedentes-radiografia
def generarRelacionAntecedesRadiografia():
    #Generar Antecedentesid
    # Todas las radiografias tienen un numero entre 0 y 5 antecedentes

    query = 'SELECT "IdRadio" FROM "Radiografia"'
    listaRad = sendDb(query, "")
    query = 'SELECT MIN("IdSustanciaAlergia") FROM "SustanciaAlergia" '
    lowBoundAlergia = sendDb(query, "")[0][0]
    query = 'SELECT MAX("IdSustanciaAlergia") FROM "SustanciaAlergia" '
    highBoundAlergia = sendDb(query, "")[0][0]
    query = 'SELECT MAX("IdSustanciaAdiccion") FROM "SustanciaAdiccion" '
    lowBoundAdicion = sendDb(query, "")[0][0]
    query = 'SELECT MAX("IdSustanciaAdiccion") FROM "SustanciaAdiccion" '
    highBoundAdicion = sendDb(query, "")[0][0]

    cont = 0
    for elem in listaRad:
        print "Antecedentes listos "+str(cont*100.0/(len(listaRad)))
        cont+=1
        idra = elem[0]

        #Cantidad de Antecedesnte de radiografia
        nAnt = random.randint(1, 5)
        #Selecion x tipos random que no se repitan
        colocados = []

        for i in range(nAnt):

            cual = random.randint(1, 5)  #5 tipos de antecedentes
            if (cual not in colocados):
                colocados.append(cual)

                if (cual == 1):
                    antcread = generaraUnIntervencion()
                elif (cual == 2):
                    antcread = generaraUnAlergico(lowBoundAlergia,highBoundAlergia)
                elif (cual == 3):
                    antcread = generaraUnAdiccion(lowBoundAdicion,highBoundAdicion)
                elif (cual == 4):
                    antcread = generarTrabajo()
                elif (cual == 5):
                    antcread = generarMedPres()

                #Ahora coloca relacion antecedentes radiografia
                query = 'INSERT INTO "En Contexto de" ("IdAntecedentes", "IdRadio" ' \
                        ' ) VALUES (%s,%s)'

                params = (antcread, idra)
                sendDb(query, params)
            else:
                continue

#generarRelacionAntecedesRadiografia()

#Generar representa radiografia-enfermedad
def generarRelacionRadiografiaEnfermedad(numero):

    query = 'SELECT "IdRadio" FROM "Radiografia" LIMIT %s'
    params = (numero,)

    res = sendDb(query, params)
    cont = 0
    for elem in res:
        print "RelacionRadioEnf listos "+str(cont*100.0/(len(res)))
        cont+=1
        idRadio = elem[0]

        #Conseguir enfermedad random
        query = 'SELECT "NombreE" FROM "Enfermedad" ORDER BY RANDOM() LIMIT 1'
        enfRandom = sendDb(query, params)[0]

        query = 'INSERT INTO "Representa" ("IdRadio","NombreE","Confirmado" ' \
                ' ) VALUES (%s,%s,%s)'

        params = (idRadio, enfRandom,True, )

        sendDb(query, params)
    generarFrames()


generarPacientes(5000)
generarSustanciasAlergia()
generarEnfermedades()
generarRadiografias(5000)
generarSustanciasDroga()
generarTrabajos()
generarMedicamentos()


generarRelacionAntecedesRadiografia()
generarRelacionRadiografiaEnfermedad(1000)

