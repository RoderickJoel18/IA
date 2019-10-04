import sqlite3

db= sqlite3.connect('C:/Users/roder/OneDrive/Documentos/Programación/Python/Basicos/IA/app/bd_numeros.db')
cursor = db.cursor()
#cursor.execute('''CREATE TABLE numeros(id INTEGER PRIMARY KEY, edad INTEGER NOT NULL)''')

db.commit()

print("Menú: \n1. Insertar numeros \n2. Sumar números \n3. Promedio de los números")
opcion = int(input("Introduzca la opción deseada: "))

if opcion == 1:
    edad = input("Introduzca una edad: ")
    cursor.execute('''INSERT INTO numeros(edad) VALUES(?)''', (edad,))
    db.commit()
    print("Registro añadido correctamente")

elif opcion == 2:
    cursor.execute('''SELECT sum(edad) FROM numeros''')
    sumaEdad = cursor.fetchall()

    for i in sumaEdad:
        listaEdad = list(i)
        print("La sumatoria de las edades es: "+ str(listaEdad[0]))

    cursor.execute('''SELECT sum(id) FROM numeros''')
    sumaId = cursor.fetchall()
    for j in sumaId:
        listaId = list(j)
        print("La sumatoria de los registros es: "+ str(listaId[0]))

elif opcion == 3:
    respuestaEdad = []
    cursor.execute('''SELECT sum(edad) FROM numeros''')
    sumaEdad = cursor.fetchall()
    for iEdad in sumaEdad:
        numeradorEdad = list(iEdad)

    cursor.execute('''SELECT count(edad) FROM numeros''')
    divisorEdad = cursor.fetchall()
    for jEdad in divisorEdad:
        denominadorEdad = list(jEdad)
        respuestaEdad.append(numeradorEdad[0]/denominadorEdad[0])

    respuestaId = []
    cursor.execute('''SELECT sum(id) FROM numeros''')
    sumaId = cursor.fetchall()
    for iId in sumaId:
        numeradorId = list(iId)

    cursor.execute('''SELECT count(id) FROM numeros''')
    divisorId = cursor.fetchall()
    for jId in divisorId:
        denominadorId = list(jId)
        respuestaId.append(numeradorId[0]/denominadorId[0])
    
    print("El promedio de las edades es: "+ str(respuestaEdad[0]))
    print("El promedio de los registros es: "+ str(respuestaId[0]))

else: 
    print("Opción Incorrecta...")


db.close()