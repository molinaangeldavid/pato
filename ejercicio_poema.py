# Se pide hacer un programa que abra un archivo de texto llamado entrada.txt el mismo contiene el siguiente poema de Ruben Dario
# y permita al usuario poder buscar palabras. Si las mismas se encuentran deberá:
# a- indicar cuántas veces aparece y en qué línea del poema está.
# b- copiar la línea a un archivo llamado salida.txt
# Además se deberá implementar try except para la apertura de archivos

import os

def validar_palabra()->str:
    '''
    PRE: ---
    POST: Retorna un string, la cual es la validacion de la palabra ingresada
    '''
    palabra = input('Ingrese la palabra que cree esta en el poema: ')
    while not palabra.isalpha():
        palabra = input('Err!!! Ingrese la palabra que cree esta en el poema: ')
    return palabra

def palabra_en_poema(linea_poemas:str,palabra:str,contador:int,contador_linea:list,palabra_linea:list)->None:
    '''
    PRE: Ingresan 2 strings y 3 listas. la cual corresponden a la estructura general
    POST: ---
    '''
    if palabra in linea_poemas:
        palabra_linea.append(linea_poemas)
        contador_linea.append(contador) 

def mostrar_lineas(palabra,palabra_linea:list)->None:
    '''
    PRE: Ingresa una lista, la cual es las lineas que aparecen la palabra buscada
    POST: Retorna las veces que aparece la palabra
    '''
    contador = 0
    nueva_linea = []
    for i in palabra_linea:
        linea = i.rstrip().split()
        nueva_linea.append(linea)
    for i in nueva_linea:
        if palabra in i:
            contador += 1
    print(f'En total se repite {contador} veces.')        

def copiar_lineas(palabra_linea:list)->None:
    '''
    PRE: Ingresa una lista, la cual contiene todas las lineas que contiene la palabra
    POST: Retorna un archivo .txt. Que contiene las lineas
    '''
    ruta = 'archivos/salida.txt'
    with open(ruta,'w') as salida:
        for linea in palabra_linea:
            salida.write(linea)

def main()->None:
    direccion = os.path.abspath(os.path.dirname(__file__)) 
    archivo = 'archivos/entrada.txt'
    try:
        ruta = os.path.join(direccion,archivo)
    except IOError:
        print('No se encontró el archivo o la ruta')
    else:    
        contador_linea = [] #linea en la que aparece la palabra
        palabra_linea = [] #la frase donde aparece la palabra
        contador = 0 #contador de lineas
        contador_palabras = 0 #las veces que aparece la palabra
        with open (ruta,'r') as archivo_poema:
            palabra = validar_palabra()
            for linea_poemas in archivo_poema:
                contador += 1
                palabra_en_poema(linea_poemas,palabra,contador,contador_linea,palabra_linea)   
            mostrar_lineas(palabra,palabra_linea)  
        print(f'La palabra esta/n en la/s linea/s: {contador_linea}')    
        copiar_lineas(palabra_linea)    
main()   