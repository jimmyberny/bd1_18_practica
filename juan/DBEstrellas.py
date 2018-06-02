import sys
import os
from operator import itemgetter
import operator

def constelacion():
    
    const = input("Nombre de la constelacion : ")
    print()

    archivo1 = open ("constelaciones.txt", "a+")
    archivo1.write(const + "\n")
    archivo1.close()


def nombreRep(nom):
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


def almacenarReg():
    nom=input("Nombre de la Estrella  : ")
    tam=input("Tamaño (Radio) Ro ó Km : ")
    mas=input("Masa Mo ó Kg           : ")
    dis=input("Distancia a la Tierra Km ó AL : ")
    con=input("Constelacion : ")
    tem=input("Temperatura Superficial °K    : ")
    print()
    try:
        #str(tam)
        #str(mas)
        #str(dis)
        #str(tem)
        if nombreRep(nom) == True:
            print("Ya existe el nombre de esa estrella, no se agregará al registro")
        else:
            nombre = "registros.txt"
            archivo = open (nombre, "a+")
            archivo.write(nom+":"+tam+":"+mas+":"+dis+":"+con+":"+tem+"\n")
            print("Registro agregado")
            archivo.close()
    except:
        print("NO REGISTRADO, DATOS INVALIDOS")
        print()
    

def buscarReg():
    entrada=input("¿QUÉ ESTRELLA QUIERE CONSULTAR?: ")
    archivo = open ("registros.txt", "r")
    encontrado=False
    for linea in archivo:
        newL=linea.split(":")
        if newL[0] == entrada:
            encontrado=True
            print(linea)
    if encontrado==False:
        print("No se encuentra esa estrella")
    archivo.close()

    
def mostrarReg():
    archivo = open ("registros.txt", "r+")
    if os.stat("registros.txt").st_size == 0:
        print("No hay registros")
    else:
        print("Nombre, tamaño/Radio, Masa, distancia, constelacion, temperatura Superficial")
        for linea in archivo:
            print(linea)
    archivo.close()


def borrarReg():
    entrada=input("Que estrella quieres eliminar?")
    archivo = open ("registros.txt", "r")
    for linea in archivo:
        newL=linea.split(":")
        if newL[0]== entrada:
            lineaBorrar=linea
    archivo.close()

    archivo = open ("registros.txt", "r")
    original = archivo.readlines()
    archivo.close()

    archivo = open("registros.txt", "w")
    for linea in original:
        if linea != lineaBorrar:
            archivo.write(linea)        
            print("Registro borrado")
    archivo.close()


def borrarDB():
    archivo = open ("registros.txt", "w+")
    for linea in archivo:
        archivo.write("")
    print("Registros eliminados")
    archivo.close()


def ordenarReg():
    archivo = open ("registros.txt", "r")
    data = []

    print("Tipo de Orden:  1 Nombre   4 Distancia")
    print("                2 Tamaño   5 Constelacion")
    print("                3 Masa     6 Temperatura")
    print("Escriba una opcion: ", end="")
    entrada = input()

    for linea in archivo:
        linea = linea.rstrip('\n')
        linea = linea.split(":")
        newL = [linea[0], (linea[1]), (linea[2]), (linea[3]), linea[4], (linea[5])]
        data.append(newL)
    archivo.close()
    
    if entrada=='1':
        data=sorted(data, key=itemgetter(0)) #EN BASE A nombre
    elif entrada=='2':
        data=sorted(data, key=itemgetter(1)) #EN BASE A tamaño
    elif entrada=='3':
        data=sorted(data, key=itemgetter(2)) #EN BASE A MASA        
    elif entrada == '4':
        data=sorted(data, key=itemgetter(3)) #EN BASE A distancia
    elif entrada == '5':
        data = sorted(data, key = itemgetter(4)) #En Base a constelacion
    elif entrada == '6':
        data = sorted(data, key = itemgetter(5)) #En Base a temperatura
    else:
        print("Opcion NO valida")
    
    print("Nombre | Tamaño,Radio | Masa | Distancia | Constelacion| Temperatura Superficial")
    print(data)
    print()


def menu():
    entrada = 8
    while entrada != 0:
        print("1 Almacenar un Registro           4 Remover un Registro")
        print("2 Recuperar un Registro           5 Remover todos los Registros")
        print("3 Recuperar lIsta de Registros    6 Ordenar Registros")
        print("7 Agregar constelacion")
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
            constelacion()
        elif entrada == 'exit':
            sys.exit()
        else:
            print("opcion no encontrada")      
menu()
