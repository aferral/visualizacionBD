__author__ = 'aferral'

#Todo Arreglar mucha redundancia y mejorar nombre de algunas querys

#--------------------------------Querys de Radiografias-------------------------------------
queryGetRadioInfo = 'SELECT "IdRadio","Fecha", "Zona", "Procedencia","Tipo", "Comentario", "RUNPaciente", ' \
                       '"NombresPaciente","ApellidosPaciente" FROM "Radiografia" WHERE "IdRadio" = %s'

queryInsertRadio = 'INSERT INTO "Radiografia"("IdRadio", "Fecha", "Zona", "Procedencia", ' \
                '"Tipo", "Comentario", "RUNPaciente", "NombresPaciente","ApellidosPaciente"' \
                   ') VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);'
queryUpdateRadio = 'UPDATE "Radiografia" SET "IdRadio" = %s, "Fecha" = %s, "Zona" = %s, "Procedencia" = ' \
                   '%s,"Tipo" = %s, "Comentario" = %s, "RUNPaciente" = %s, "NombresPaciente" = %s,"ApellidosPaciente" = ' \
                   '%s WHERE "IdRadio" = %s'

queryIdRadio = 'Select "IdRadio" FROM "Radiografia" WHERE "IdRadio" = %s '
queryFechas = 'Select "IdRadio" FROM "Radiografia" WHERE ("Fecha" > %s AND "Fecha" < %s)'
queryDeleteRadio = 'DELETE FROM "Radiografia" WHERE "IdRadio" = %s ;'
#--------------------------------Querys pacientes--------------------------------
queryPacienteInfo = 'SELECT "Nombres","Apellidos","RUN","FechaNac","Sexo" FROM ' \
                    '"Paciente" WHERE "RUN" = %s AND "Apellidos" = %s AND "Nombres" = %s '
queryUpdatePaciente = 'UPDATE "Paciente" SET "FechaNac" = %s,"Sexo"= %s WHERE ' \
                      '"RUN" = %s AND "Nombres" = %s AND "Apellidos" = %s ;'

queryFiltrarPaciente = 'SELECT "Nombres","Apellidos","RUN" FROM "Paciente" '
queryAddPaciente = 'INSERT INTO "Paciente" ("Sexo", "RUN", "Nombres", "Apellidos", "FechaNac" ) ' \
                'VALUES (%s, %s, %s, %s, %s)'
queryDeletePaciente = 'DELETE FROM "Paciente" WHERE "Nombres" = %s AND "Apellidos" = %s AND "RUN" = %s ;'

queryPaciente = 'SELECT "Paciente"."Nombres","Paciente"."Apellidos","Paciente"."RUN","Paciente".' \
                '"FechaNac","Sexo" FROM' \
                ' "Radiografia" JOIN "Paciente" ON ("Paciente"."RUN" = "Radiografia"."RUNPaciente"' \
                ' AND "Paciente"."Nombres" = "Radiografia"."NombresPaciente" ' \
                ' AND "Paciente"."Apellidos" = "Radiografia"."ApellidosPaciente" ' \
                ') WHERE "IdRadio" = %s'

queryNombresPaciente = 'Select "IdRadio" FROM "Radiografia" WHERE "NombresPaciente" LIKE %s '
queryApellidosPaciente = 'Select "IdRadio" FROM "Radiografia" WHERE "ApellidosPaciente" LIKE %s '
queryRUN = 'Select "IdRadio" FROM "Radiografia" WHERE "RUNPaciente" = %s '
querySexoPaciente = 'SELECT "IdRadio" FROM "Radiografia" WHERE "Radiografia"."RUNPaciente" ' \
        'IN (SELECT "RUN" FROM "Paciente" WHERE "Sexo" = %s)'

#--------------------------------Querys REPRESENTA--------------------------------
queryAddEnfToRad = 'INSERT INTO "Representa"( "NombreE", "Confirmado","IdRadio", "Comentario" ' \
                   ') VALUES (%s, %s, %s,%s);'
queryDeleteEnfRelation = 'DELETE FROM "Representa" WHERE "IdRadio" = %s ;'
#--------------------------------Querys Frames--------------------------------
queryAddFrame = 'INSERT INTO "Frames"( "NumOfFrame", "IdRadio") VALUES (%s, %s);'
queryFrames = 'SELECT "NumOfFrame" FROM "Frames" WHERE "IdRadio" = %s'
queryDeleteFrames = 'DELETE FROM "Frames" WHERE "IdRadio" = %s ;'

#--------------------------------Querys Medicamento--------------------------------
queryAddMedicamento = 'INSERT INTO "Medicamento"( "NombreMedicamento") VALUES (%s);'
queryDeleteMedicamento = 'DELETE FROM "Medicamento" WHERE "NombreMedicamento" = %s ;'
queryUpdateMedicamento = 'UPDATE "Medicamento" SET "NombreMedicamento"= %s WHERE "NombreMedicamento" = %s;'
queryListaMedicamento = 'SELECT "IdMedicamento","NombreMedicamento" FROM "Medicamento"'

queryMed = 'SELECT "NombreMedicamento" FROM "Prescripcion Medica" JOIN "Medicamento" ON ' \
                '("Prescripcion Medica"."IdMedicamento" = "Medicamento"."IdMedicamento") WHERE ' \
                '"IdAntecedentes" IN (SELECT "IdAntecedentes" FROM "En Contexto de" WHERE "IdRadio" = %s)'

queryMedicamento = 'SELECT "IdRadio" FROM "En Contexto de" JOIN "Prescripcion Medica" ' \
                    'ON ("En Contexto de"."IdAntecedentes" = "Prescripcion Medica"."IdAntecedentes")' \
                    ' WHERE "IdMedicamento" IN (SELECT "Medicamento"."IdMedicamento" FROM "Prescripcion Medica"' \
                    ' JOIN "Medicamento" ON ("Medicamento"."IdMedicamento" = "Prescripcion Medica"."IdMedicamento")' \
                    ' WHERE "Medicamento"."NombreMedicamento" = %s) '

queryListaMed = 'SELECT "NombreMedicamento" FROM "Medicamento" '


#--------------------------------Querys Droga--------------------------------
queryAddDroga = 'INSERT INTO "SustanciaAdiccion"( "NombreSustanciaAdiccion") VALUES (%s);'
queryDeleteDroga = 'DELETE FROM "SustanciaAdiccion" WHERE "NombreSustanciaAdiccion" = %s ;'
queryUpdateDroga = 'UPDATE "SustanciaAdiccion" SET "NombreSustanciaAdiccion"= %s WHERE "NombreSustanciaAdiccion" = %s;'
queryListaDroga = 'SELECT "IdSustanciaAdiccion","NombreSustanciaAdiccion" FROM "SustanciaAdiccion";'

queryAdiccion = 'SELECT "NombreSustanciaAdiccion" FROM "Adiccion" JOIN "SustanciaAdiccion" ON ' \
                '("Adiccion"."IdSustancia" = "SustanciaAdiccion"."IdSustanciaAdiccion") WHERE "IdAntecedentes"' \
                ' IN (SELECT "IdAntecedentes" FROM "En Contexto de" WHERE "IdRadio" = %s)'

queryFuma = 'SELECT "IdRadio" FROM "En Contexto de" WHERE "IdAntecedentes" IN ' \
        '(SELECT "IdAntecedentes" FROM "Adiccion" JOIN "Sustancia" ON ("Adiccion"."IdSustancia" =' \
        ' "Sustancia"."IdSustancia")  WHERE ("NombreSustancia" = %s))'
#--------------------------------Querys Alergia--------------------------------
queryAddAlergia = 'INSERT INTO "SustanciaAlergia"( "NombreSustanciaAlergia") VALUES (%s);'
queryDeleteAlergia = 'DELETE FROM "SustanciaAlergia" WHERE "NombreSustanciaAlergia" = %s ;'
queryUpdateAlergia = 'UPDATE "SustanciaAlergia" SET "NombreSustanciaAlergia"= %s WHERE "NombreSustanciaAlergia" = %s;'
queryListaAlergia = 'SELECT "IdSustanciaAlergia", "NombreSustanciaAlergia" FROM "SustanciaAlergia";'

queryAlergia = 'SELECT "NombreSustanciaAlergia" FROM "Alergico" JOIN "SustanciaAlergia" ON' \
                ' ("Alergico"."IdSustancia" = "SustanciaAlergia"."IdSustanciaAlergia") WHERE ' \
                '"IdAntecedentes" IN (SELECT "IdAntecedentes" FROM "En Contexto de"' \
                ' WHERE "IdRadio" = %s)'

#--------------------------------Querys antecedente--------------------------------
queryAddAntece = 'INSERT INTO "Antecedentes" ("IdAntecedentes") ' \
 'VALUES (DEFAULT) RETURNING "IdAntecedentes";'
querySearchIdAnt = 'SELECT "IdAntecedentes" FROM "En Contexto de" WHERE "IdRadio" = %s '
queryOperacion = 'SELECT "FechaOperacion","NombreOperacion","DrOperacion" FROM "Intervencion" ' \
                ' WHERE "IdAntecedentes" IN (SELECT "IdAntecedentes" FROM "En Contexto de" WHERE "IdRadio" = %s)'

queryDeleteEnContexto = 'DELETE FROM "En Contexto de" WHERE "IdRadio" = %s ;'
queryDeleteAntTrabajo = 'DELETE FROM "Trabajo" WHERE "IdAntecedentes" IN %s ;'
queryDeleteAntMedicamento = 'DELETE FROM "Prescripcion Medica" WHERE "IdAntecedentes" IN %s ;'
queryDeleteAntAlergia = 'DELETE FROM "Alergico" WHERE "IdAntecedentes" IN %s ;'
queryDeleteAntAdiccion = 'DELETE FROM "Adiccion" WHERE "IdAntecedentes" IN %s ;'
queryDeleteAntOtros = 'DELETE FROM "Otros" WHERE "IdAntecedentes" IN %s ;'
queryDeleteAntIntervencion = 'DELETE FROM "Intervencion" WHERE "IdAntecedentes" IN %s ;'
queryDeleteAntecedentes = 'DELETE FROM "Antecedentes" WHERE "IdAntecedentes" IN %s ;'


queryTrabajo = 'SELECT "NombreTrabajo" FROM "Trabajo" WHERE "IdAntecedentes" IN ' \
                '(SELECT "IdAntecedentes" FROM "En Contexto de" WHERE "IdRadio" = %s)'

queryComentario = 'SELECT "Comentario" FROM "Otros" WHERE "IdAntecedentes" IN ' \
                '(SELECT "IdAntecedentes" FROM "En Contexto de" WHERE "IdRadio" = %s)'

#--------------------------------Query Zona--------------------------------
queryAddZona = 'INSERT INTO "Zonas"( "nombreZ") VALUES (%s);'
queryDeleteZona = 'DELETE FROM "Zonas" WHERE "nombreZ" = %s ;'
queryUpdateZona = 'UPDATE "Zonas" SET "nombreZ"= %s WHERE "nombreZ" = %s;'
#TODO ARREGLAR ESTRUCTURA REDUNDANCIA
queryListaZona = 'SELECT DISTINCT "nombreZ" FROM "Zonas" ORDER BY "nombreZ" '
queryRadiZone = 'SELECT DISTINCT "nombreZ" FROM "Zonas" ORDER BY "nombreZ" '

#--------------------------------Query Tipo--------------------------------
queryAddTipo = 'INSERT INTO "TipoR"( "nombreT") VALUES (%s);'
queryDeleteTipo = 'DELETE FROM "TipoR" WHERE "nombreT" = %s ;'
queryUpdateTipo = 'UPDATE "TipoR" SET "nombreT"= %s WHERE "nombreT" = %s;'
queryListaTipo = 'SELECT "nombreT" FROM "TipoR";'
queryTipos = 'SELECT "nombreT" FROM "TipoR" '

#TODO ARREGLAR ESTRUCTURA OBSOLETA Y REDUNDANCIA
queryTipoRadio = 'Select "IdRadio" FROM "Radiografia" WHERE "Tipo" = %s'

#--------------------------------Query Procedencia--------------------------------
queryAddProce = 'INSERT INTO "Procedencias"( "nombreP") VALUES (%s);'
queryDeleteProce = 'DELETE FROM "Procedencias" WHERE "nombreP" = %s ;'
queryUpdateProce = 'UPDATE "Procedencias" SET "nombreP"= %s WHERE "nombreP" = %s;'
#TODO BORRAR REDUNDANCIA
queryListaProce = 'SELECT "nombreP" FROM "Procedencias";'
queryProcedencia = 'SELECT DISTINCT "nombreP" FROM "Procedencias" ORDER BY "nombreP"'

#--------------------------------Querys enfermedades--------------------------------
queryAddEnfermedad = 'INSERT INTO "Enfermedad"( "NombreE") VALUES (%s);'
queryDeleteEnfermedad = 'DELETE FROM "Enfermedad" WHERE "NombreE" = %s ;'
queryUpdateEnfermedad = 'UPDATE "Enfermedad" SET "NombreE"= %s WHERE "NombreE" = %s;'
queryListaEnfermedad = 'SELECT "NombreE" FROM "Enfermedad"'

#TODO BORRAR REDUNDANCIA
queryListaEnf = 'SELECT DISTINCT "NombreE" FROM "Enfermedad" ORDER BY "NombreE" '
queryEnfName = 'SELECT DISTINCT "NombreE" FROM "Enfermedad" ORDER BY "NombreE" '
queryEnfermedadNombre = 'Select "IdRadio" FROM "Representa" WHERE ("NombreE" = %s)'
queryEnfermedadConfirmado = 'Select "IdRadio" FROM "Representa" WHERE ("Confirmado" = %s)'

queryRepresentaFromId = 'Select "NombreE", "Confirmado","Comentario","IdRadio" ' \
                        'FROM "Representa" WHERE "IdRadio" = %s'
#--------------------------------Query Ayudas Visualizacion--------------------------------

queryMostrar = 'select "IdRadio","Fecha","Zona","Procedencia","Tipo","RUNPaciente","NombresPaciente", ' \
                '"ApellidosPaciente","NombreE","Confirmado" from "Radiografia" ' \
                'JOIN "Representa" USING ( "IdRadio" ) WHERE "Radiografia"."IdRadio" in %s'

metaquery = 'CREATE TEMP TABLE tmp126 AS ( ' + queryMostrar + " ) ;" + "SELECT column_name " \
        "FROM  information_schema.columns WHERE  table_name = 'tmp126' ORDER  BY ordinal_position"


