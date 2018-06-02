tamanio= ' '
masa= ' '
distancia=' '
constela= ' '
contenido = []
lineas = []


import sys
import os
from operator import itemgetter
import operator

program_name = sys.argv[0]
arguments = sys.argv[1:]
arguments2 = sys.argv[2:]

######################################################
def almacenar():
    nombre   = input('Nombre:')
    tamanio  = input('Tamaño: ')
    masa     = input('Masa: ')
    distancia= input('Distancia: ')
    constela = input('Constelacion: ')

    archivo = open ("estrellas.txt", "a+")
    archivo.write(nombre+" "+tamanio+" "+masa+" "+distancia+" "+constela+"\n")
    print("Estrella agregada \n")
    archivo.close()
#######################################################
def borrarDB():
    archivo = open ("estrellas.txt", "w+")
    for linea in archivo:
        archivo.write("")
    print(">>>> Registros eliminados")
    archivo.close()
#######################################################
def buscarRegistro():
    entrada=input("Introduzca el nombre de la estrella a consultar: ")
    archivo = open("estrellas.txt", "r")
    encontrada = False
    for linea in archivo:
        data=linea.split(" ")
        if data[0] == entrada:
            encontrada = True
            print("Nombre | tamanio | masa \n")
            print(linea)
    if encontrada == False:
        print("Estrella no encontrada\n\n")
#######################################################        
def mostrarRegistros():    
    archivo = open("estrellas.txt", "r+")
    if os.stat("estrellas.txt").st_size == 0:
        print("No hay registros")
    else:
        print("Nombre | tamanio | masa | distancia | constelacion")
        for linea in archivo:
            print(linea)
        archivo.close()
#######################################################
def ordenarDB():
    archivo = open ("estrellas.txt", "r")
    archivoOrden = open("estrellasOrden.txt", "w+")
    data = []
    datos =[]
    array = []

    print("Tipo de Orden:  1 Nombre   4 Distancia")
    print("                2 Tamaño   5 Constelacion")
    print("                3 Masa     ")
    print("Escriba una opcion: ", end="")
    entrada = input()

    for linea in archivo:
        linea = linea.rstrip('\n')
        linea = linea.split(" ")
        newL =[linea[0],int(linea[1]),int(linea[2]),int(linea[3]),linea[4]]
        data.append(newL)
    
    archivo.close()
    
    if entrada=='1':
        data=sorted(data, key=itemgetter(0)) #EN BASE A nombre
    elif entrada=='2':
        data=sorted(data, key=itemgetter(1)) #EN BASE A tamaño
    elif entrada=='3':
        data=sorted(data, key=operator.itemgetter(2)) #EN BASE A MASA        
    elif entrada == '4':
        data=sorted(data, key=itemgetter(3)) #EN BASE A distancia
    elif entrada == '5':
        data = sorted(data, key = itemgetter(4)) #En Base a constelacion
    #elif entrada == '6':
    #    data = sorted(data, key = itemgetter(5)) #En Base a temperatura
    else:
        print("Opcion NO valida")
    
    print("Nombre, Tamaño, Masa, Distancia, Constelacion, Temperatura")
    
    for renglon in data:
        print(renglon[0]+" "+str(renglon[1])+" "+str(renglon[2])+" "+str(renglon[3])+" "+renglon[4])
    
    for renglon in data:
        archivoOrden.write(renglon[0]+" "+str(renglon[1])+" "+str(renglon[2])+" "+str(renglon[3])+" "+renglon[4]+"\n")
    print("Registro ordenado y guardado en archivo estrellasOrden")
    archivoOrden.close()

##########################################################################
def clasificarCons():
    print("Clasificacion estelar por medio de la constelacion")
    constelacion = input("Introduzca la constelacion: ")
    archivo = open("estrellas.txt", "r+")
    data = []

    for linea in archivo:
        linea = linea.rstrip('\n')
        linea = linea.split(" ")
        if linea[4]== constelacion:
            newL=[linea[0],int(linea[1]),int(linea[2]),int(linea[3]),linea[4]]
            data.append(newL)
    print(data)

    archivo.close()

    for renglon in data:
        print(renglon[0]+" "+str(renglon[1])+" "+str(renglon[2])+" "+str(renglon[3])+" "+renglon[4]+"\n")
        
    archivoClasifi = open("estrellasClasifi.txt", "w+")
    for renglon in data:
        archivoClasifi.write(renglon[0]+" "+str(renglon[1])+" "+str(renglon[2])+" "+str(renglon[3])+" "+renglon[4]+"\n")


    archivoClasifi.close()                           

                               

######################Menu del programa####################
flag = '1'

while flag=='1':
    print("Base de datos estelar")
    print("Introduzca una opción:")
    print("(1) Almacenar nueva estrella")
    print("(2) Borrar base de datos")
    print("(3) Ordenar base de datos")
    print("(4) Leer archivo y mostrar")
    print("(5) Buscar registro")
    print("(6) Mostrar registros")
    print("(7) Clasificar por constelaciones")
    print("(8) Salir del programa")

    opcion=input()

    if opcion == '1':
        almacenar()

    elif opcion=='2':
        borrarDB()

    elif opcion == '3':
        ordenarDB()

    elif opcion == '4':
         with open("estrellas.txt") as f:
             data2 = f.readlines()
             print(data2)
             for linea in data2:
                 print (linea)
    elif opcion == '5':
        buscarRegistro()

    elif opcion == '6':
        mostrarRegistros()
        
    elif opcion == '7':
        clasificarCons()

    elif opcion == '8':
        print("Saliendo del programa...Gracias")
        sys.exit(1)

                           
                               
                               

    
 
