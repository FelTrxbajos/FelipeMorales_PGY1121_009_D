import os
import numpy
import time
import msvcrt

concierto = numpy.zeros((10,10),int)


lista_rut = []
lista_entradas = []
lista_filas = [10,9,8,7,6,5,4,3,2,1]
lista_columnas = []
ent_vip = 120000
ent_gold = 80000
ent_silver = 50000
def mostrar_menu():
    os.system("cls")
    print('''Menu de entradas para concierto de "MICHAEL JAM"
    1.Comprar entradas
    2.Mostrar ubicaciones disponibles
    3.Ver listado de asistentes
    4.Mostrar ganancias totales
    5.Salir''')

def validar_opcion():
    while True:
        try:
            opc = int(input("Ingrese una opcion: "))   
            if opc in(1,2,3,4,5):
                return opc
            else:
                print("ERROR! debes seleccionar uno de los numeros válidos")
        except:
            print("ERROR! debes ingresar una valor numérico")
  
def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese su rut (sin puntos ni dígito verificador): "))
            if rut >= 10000000 and rut <= 99999999:
                return rut
            else:
                print("ERROR! debe ingresar un rut válido")
                time.sleep(2)
                os.system("cls")
        except:
            print ("ERROR! debes ingresar un valor numérico")
            time.sleep(2)
            os.system("cls")
        lista_rut.append(rut)

def mostrar_ubicacion():
    print ("\t ESCENARIO\n ")
    contador = 1 
    for x in range (10):
        print ((x+ 1), end="  ")
        for y in range (10):
            print ((y + contador),end=" ")
        print ()    
    time.sleep(3)
    
def validar_asiento():
    while True:
        try:
            asiento = int(input("Indique cuál o cuáles asientos desea:"))
            if asiento <= 100 and asiento >=0:
                return asiento
            else:
                print("ERROR! elija un asiento disponible")
        except:
            print("ERROR! debe ingresar un valor numérico") 

def validar_entradas():
    
    while True:
        try:
            cant_entradas = int(input("Cuantas entradas desea comprar (mín 1, max 3)"))     
            if cant_entradas >=1 and cant_entradas <= 3:
                return cant_entradas
            else:
                print("ERROR! debes comprar 1 a 3 entradas")
                time.sleep(2)
                os.system("cls")
        except:
            print("ERROR! debes ingresar un valor numérico")
            time.sleep(2)
            os.system("cls")
def comprar_entradas ():
    os.system("cls")
    validar_entradas()
    while True:
        mostrar_ubicacion()
        try:
            entrada = int(input("Ingrese donde quiere sentarse: "))
            if entrada == 0:
                return entrada
            else:
                print("ERROR! debe ingresar un numero válido")
        except:
            print("ERROR! ingrese un valor numérico")   
        validar_rut()
        print ("Compra realizada con éxito")
        
def ganancias_totales():
    print (f"""            Tipo entradas         Cant entradas      Ganancia total
            Platinum:{ent_vip}                                            
            Gold:    {ent_gold}                                         
            Silver:  {ent_silver}                                   
            TOTAL:                                                 """)
    time.sleep(4)
    
def lista_asistentes():
    if lista_rut == []:
        print("No hay ruts disponibles")
        time.sleep(3)
        return lista_rut
    else:
        print(lista_rut)

def salir():
    print("Felipe morales  06/07/2023")        