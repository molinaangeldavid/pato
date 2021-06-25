def bisiesto(anio:int)->bool:
    '''
    PRE: Ingresa un valor numerico entero, la cual es un año
    POST: Retorna un valor booleano, indicando si un año es bisiesto o no
    '''
    if anio%4==0:
        return True
    else:
        return False    

def dias_del_mes(mes:int, anio:int)->int:
    '''
    PRE: Ingresan dos valores numericos enteros, la cual son el mes y el año
    POST: Retorna un valor numerico, la cual son los dias que corresponden a mes
    '''
    if mes == 2:
        if anio % 4 == 0:
            return 29
        else: 
            return 28
    else:
        return 30                 

def fecha_valida(dia:int, mes:int, anio:int):
    '''
    PRE: Ingresan tres valores numericos, la cual son dia  mes y año
    POST: Retorna un valor booleano, la cual indica si una fecha es valida o no
    '''
    if mes == 2 and anio % 4 == 0 and dia <=29:
        return True
    elif mes == 2 and anio % 4 != 0 and dia <=28:
        return True
    if mes<12 and mes != 2 and dia <=30:
        return True    

def dias_h_fin_mes(dia:int, mes:int, anio:int):
    '''
    PRE: Ingresan tres valores numericos enteros, la cual son dia mes y año
    POST: Retorna un valor numerico entero, la cual son los dias que faltan para finalizar el mes
    '''
    if mes == 2:
        if anio % 4 == 0:
            dias =  29
        else: 
            dias =  28
    else:
        dias = 30  
    fecha = dias - dia
    return fecha

def dias_h_fin_anio(dia:int, mes:int, anio:int)->int:
    '''
    PRE: Ingresan tres valores numericos, la cual son los dias, mes y anios
    POST: Retorna un valor numerico, la cual indica el tiempo faltante para finalizar el anio
    '''
    if mes == 2:
        if anio % 4 == 0:
            dias =  29
        else: 
            dias =  28
    else:
        dias = 30  
    fecha = dias - dia
    if mes>1:
        resultado = (mes - 1) * 30 + dia

        

def dias_transcurridos(dia:int, mes:int, anio:int):
    '''
    DOC: Completar
    '''
    pass


def tiempo_transcurrido(dia1:int, mes1:int, anio1:int, dia2:int, mes2:int, anio2:int):
    '''
    DOC: Completar
    '''
    pass

def main():
    print(dias_h_fin_mes(4,6,2012))

main()