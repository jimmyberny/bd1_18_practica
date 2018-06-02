import sys
import os
from operator import itemgetter
import operator

def nombreRep(nom): #checar si ya existe el nombre de la estrella
    try:
        archivo = open ("registros.txt", "r")
        repetido=False
        for linea in archivo:
            newL=linea.split(":")
            if newL[0] == nom:
                repetido=True
        archivo.close()
    except:
        repetido=False
    return repetido

def almacenarReg(): #almacenar un nuevo registro
    nom=input("Nombre: ")
    tam=input("Tamaño :")
    mas=input("MASA KG :")
    dis=input("Distancia a la Tierra X :")
    con=input("Constelacion :")
    tem=input("Temperatura K :")
    try:
        int(tam)
        int(mas)
        int(dis)
        int(tem)
        if nombreRep(nom) == True:
            print(">>>> Ya existe el nombre de esa estrella, NO se agregará al registro \n")
        else:
            nombre = "registros.txt"
            archivo = open (nombre, "a+")
            archivo.write(nom+":"+tam+":"+mas+":"+dis+":"+con+":"+tem+"\n")
            print(">>>> Registro agregado\n")
            archivo.close()
    except:
        print(">>>> NO REGISTRADO, DATOS INVALIDOS\n")
    

def buscarReg(): #Buscar una estrella del registro por su nombre
    entrada=input("¿QUÉ ESTRELLA QUIERE CONSULTAR?: ")
    archivo = open ("registros.txt", "a+")#leer y/o crear archivo
    encontrado=False
    for linea in archivo:
        newL=linea.split(":")
        if newL[0] == entrada:
            encontrado=True
            print(linea)
    if encontrado==False: #si no se encuentra la estrella imprime que no está
        print(">>>> NO se encuentra esa estrella \n")
    archivo.close()

    
def mostrarReg():#imprimir todo el registro
    archivo = open ("registros.txt", "a+") #crear y/o leer archivo
    if os.stat("registros.txt").st_size == 0:
        print(">>>> NO hay registros\n") #si está vacío decir q no hay registros
    else:
        print("nombre, tamaño, masa, distancia, constelacion, temperatura\n")
        for linea in archivo: 
            print(linea)
    archivo.close()


def borrarReg():
    entrada=input("Que estrella quieres eliminar?")
    archivo = open ("registros.txt", "a+") #crear y/o leer archivo
    for linea in archivo:
        newL=linea.split(":")
        if newL[0]== entrada:
            lineaBorrar=linea #linea a borrar
    archivo.close()

    archivo = open ("registros.txt", "r") #guardar datos del archivo
    original = archivo.readlines()
    archivo.close()

    archivo = open("registros.txt", "w") #escribir aquellas lineas menos la q se desea eliminar
    for linea in original:
        if linea != lineaBorrar:
            archivo.write(linea)        
    print(">>>> Registro borrado\n")
    archivo.close()


def borrarDB():
    archivo = open ("registros.txt", "w+") #escribir y/o crear
    for linea in archivo:
        archivo.write("")
    print(">>>> Registros eliminados\n")
    archivo.close()


def ordenarReg():
    archivo = open ("registros.txt", "a+")
    data = []

    print("Tipo de Orden:  1 Nombre   4 Distancia")
    print("                2 Tamaño   5 Constelacion")
    print("                3 Masa     6 Temperatura")
    print("Escriba una opcion: ", end="")
    entrada = input()

    for linea in archivo:
        linea = linea.rstrip('\n')
        linea = linea.split(":")
        newL = [linea[0],int(linea[1]), int(linea[2]), int(linea[3]), linea[4], int(linea[5])]
        data.append(newL)
    archivo.close()
    
    if entrada=='1':
        data=sorted(data, key=itemgetter(0)) #EN BASE A nombre
        print("Nombre, Tamaño, Masa, Distancia, Constelacion, Temperatura")
        print(data)
        print()

    elif entrada=='2':
        data=sorted(data, key=itemgetter(1)) #EN BASE A tamaño
        print("Nombre, Tamaño, Masa, Distancia, Constelacion, Temperatura")
        print(data)
        print()

    elif entrada=='3':
        data=sorted(data,key=operator.itemgetter(2)) #EN BASE A MASA        
        print("Nombre, Tamaño, Masa, Distancia, Constelacion, Temperatura")
        print(data)
        print()

    elif entrada == '4':
        data=sorted(data, key=itemgetter(3)) #EN BASE A distancia
        print("Nombre, Tamaño, Masa, Distancia, Constelacion, Temperatura")
        print(data)
        print()

    elif entrada == '5':
        data = sorted(data, key = itemgetter(4)) #En Base a constelacion
        print("Nombre, Tamaño, Masa, Distancia, Constelacion, Temperatura")
        print(data)
        print()

    elif entrada == '6':
        data = sorted(data, key = itemgetter(5)) #En Base a temperatura
        print("Nombre, Tamaño, Masa, Distancia, Constelacion, Temperatura")
        print(data)
        print()

    else:
        print(">>>> Opcion NO valida\n")
    

def menu():
    entrada = 7
    while entrada != 0:
        print("1 Almacenar un Registro           4 Remover un Registro")
        print("2 Recuperar un Registro           5 Remover todos los Registros")
        print("3 Recuperar lIsta de Registros    6 Ordenar Registros")
        print("7 Agregar Constelación            8 Relación Constelación\n  ")
        print("Salir: escriba exit")
        print()
        print("Escriba una opcion: ",end="")
        
        entrada=input()
        if entrada=='1':
            almacenarReg()
        elif entrada=='2':
            buscarReg()
        elif entrada =='3':
            mostrarReg()
        elif entrada == '4':
            borrarReg()
        elif entrada == '5':
            borrarDB()
        elif entrada == '6':
            ordenarReg()
        elif entrada == '7':
            const()
        elif entrada == '8':
            opCon()
            printRel()
        elif entrada == 'exit':
            sys.exit()
        else:
            print(">>>> Opcion NO encontrada")      

def const():
    entrada = input("Escribe el nombre de la constelacion: ")
    archivo = open ("constelaciones.txt", "a+")
    archivo.write(entrada+"\n")
    archivo.close()

def opCon(): ##### funcion ppal para crear relacion
    archivo=open("relacion.txt", "a+") #crear arch en caso q no exista
    archivo.close()
    if os.stat("relacion.txt").st_size != 0: # si no esta vacio, borrar su contenido
        archivo = open ("relacion.txt", "w+")
        for linea in archivo:
            archivo.write("")
        archivo.close()

    archivo2 = open ("constelaciones.txt", "a+") # crear arch en caso no exista
    archivo2.close()  
    if os.stat("constelaciones.txt").st_size == 0:# si esta vacio imprimir..
        print(">>>> No hay constelaciones agregadas\n")
    else:
        archivo2 = open ("constelaciones.txt", "r+") #leer
        for linea in archivo2:     
            linea2=linea.rstrip('\n') #eliminar el caracter salto de linea
            add=relacion(linea2)     #llamar funcion para comparar el nombre de constelacion, retorna arreglo
            asign("\nConstelacion "+linea) #escribir en el archivo el nombre de constelacion
            for item in add:
                asign(item)#funcion que escribira en el archivo los registros
        archivo2.close()

def relacion(lineaCons): #funcion para comparar
    archivo = open ("registros.txt", "r")
    arr=[]    
    i=0
    for linea in archivo:
        linea2 = linea.rstrip('\n')
        linea2 = linea2.split(":")
        comparar1=str(linea2[4])
        comparar2=str(lineaCons)
        if comparar1==comparar2: #comparar nombre constelacion, con la constelacin del registro
            i+=1
            arr.append(linea)
    archivo.close()
    return arr #revolver en un arreglo aquellos que pertenecen a la constelacion

def asign(add): #funcion q escribe en el archivo relacion los registros
    archivo2 = open ("relacion.txt", "a+")
    newCad=''
    for cad in add:
        newCad=newCad+cad
    archivo2.write(newCad) #escribir las palabras del arreglo
    archivo2.close()

def printRel(): #solo imprimir en consola el archivo de la relacion de registros
    archivo=open("relacion.txt","r")
    for linea in archivo:
        cad=''
        linea= linea.split(":")
        for item in linea:
            cad=cad + " "+ item
        print(cad)
    archivo.close()

menu()
