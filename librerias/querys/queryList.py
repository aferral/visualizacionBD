__author__ = 'aferral'
queryInsertRadio = 'INSERT INTO "Radiografia"("IdRadio", "Fecha", "Zona", "Procedencia", ' \
                '"Tipo", "Comentario", "RUNPaciente", "NombresPaciente","ApellidosPaciente") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);'

queryPacienteInfo = 'SELECT "Nombres","Apellidos","RUN","FechaNac","Sexo" FROM ' \
                    '"Paciente" WHERE "RUN" = %s AND "Apellidos" = %s AND "Nombres" = %s '
queryUpdatePaciente = 'UPDATE "Paciente" SET "FechaNac" = %s,"Sexo"= %s WHERE ' \
                      '"RUN" = %s AND "Nombres" = %s AND "Apellidos" = %s ;'

queryFiltrarPaciente = 'SELECT "Nombres","Apellidos","RUN" FROM "Paciente" '
queryAddPaciente = 'INSERT INTO "Paciente" ("Sexo", "RUN", "Nombres", "Apellidos", "FechaNac" ) ' \
                'VALUES (%s, %s, %s, %s, %s)'
queryDeletePaciente = 'DELETE FROM "Paciente" WHERE "Nombres" = %s AND "Apellidos" = %s AND "RUN" = %s ;'

queryAddEnfToRad = 'INSERT INTO "Representa"( "NombreE", "Confirmado","IdRadio") VALUES (%s, %s, %s);'

queryAddFrame = 'INSERT INTO "Frames"( "NumOfFrame", "IdRadio") VALUES (%s, %s);'

queryAddMedicamento = 'INSERT INTO "Medicamento"( "NombreMedicamento") VALUES (%s);'
queryDeleteMedicamento = 'DELETE FROM "Medicamento" WHERE "NombreMedicamento" = %s ;'
queryUpdateMedicamento = 'UPDATE "Medicamento" SET "NombreMedicamento"= %s WHERE "NombreMedicamento" = %s;'
queryListaMedicamento = 'SELECT "IdMedicamento","NombreMedicamento" FROM "Medicamento"'

queryAddDroga = 'INSERT INTO "SustanciaAdiccion"( "NombreSustanciaAdiccion") VALUES (%s);'
queryDeleteDroga = 'DELETE FROM "SustanciaAdiccion" WHERE "NombreSustanciaAdiccion" = %s ;'
queryUpdateDroga = 'UPDATE "SustanciaAdiccion" SET "NombreSustanciaAdiccion"= %s WHERE "NombreSustanciaAdiccion" = %s;'
queryListaDroga = 'SELECT "NombreSustanciaAdiccion", "IdSustanciaAdiccion" FROM "SustanciaAdiccion";'

queryAddAlergia = 'INSERT INTO "SustanciaAlergia"( "NombreSustanciaAlergia") VALUES (%s);'
queryDeleteAlergia = 'DELETE FROM "SustanciaAlergia" WHERE "NombreSustanciaAlergia" = %s ;'
queryUpdateAlergia = 'UPDATE "SustanciaAlergia" SET "NombreSustanciaAlergia"= %s WHERE "NombreSustanciaAlergia" = %s;'
queryListaAlergia = 'SELECT "IdSustanciaAlergia", "NombreSustanciaAlergia" FROM "SustanciaAlergia";'

queryAddAntece = 'INSERT INTO "Antecedentes" ("IdAntecedentes") ' \
 'VALUES (DEFAULT) RETURNING "IdAntecedentes";'