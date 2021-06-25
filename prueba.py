def palindromo(palabra:str)->bool:
    if palabra == palabra[-1::-1]:
        return False
    else:
        return True
       
def main ()->None:
    print('Ingrese una palabra que sea un palindromo')
    init = True
    while init == True:
        palabra = input('Ingrese una palabra: ')
        while not palabra.isalpha():
            palabra = input('ERR!!! Ingrese de nuevo la palabra: ')
        init = palindromo(palabra)
    print(f'La palabra -{palabra}- es un palindromo')

main()
