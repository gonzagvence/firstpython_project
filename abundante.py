def es_divisor(n:int, m:int)->bool:
    '''
    Determina si n es un divisor de m.
    Requiere: n y m mayores que cero
    Devuelve: True en el caso de que n sea divisor
            de m y False en el caso de no serlo
    '''
    vr:bool = False
    if (m%n == 0):
        vr = True
    return vr


def suma_divisores_positivos(n:int)->int:
    '''
    Obtiene la suma de los divisores positivos de n.
    Requiere: n entero mayor que cero
    Devuelve: la suma de todos los divisores 
            positivos de n
    '''
    vr:int = 0
    i:int = 1

    while (i <= n):
        if es_divisor(i,n):
            vr = vr + i
        i = i + 1
    
    return vr


def es_abundante(n:int)->bool:
    '''
    Determina si n es un número abundante, es decir, si 
    la suma de todos los divisores positivos de n (incluido 
    el propio n) es estrictamente mayor que 2 × n.
    Requiere: n entero mayor que cero
    Devuelve: True si n es un numero abundante y
            False en el caso de no serlo
    '''
    vr:bool = False
    suma_divisores = suma_divisores_positivos(n)
    if (suma_divisores > 2*n):
        vr = True
    return vr

def suma_abundantes(n:int, m:int)->int:
    '''
    Obtiene la suma de los números abundantes mayores o 
    iguales que n y menores o iguales que m.
    Requiere: n menor o igual que m, mayores que cero
    Devuelve: la suma de los numeros abuntantes mayores o
            iguales que n y menores o iguales que m

    '''
    vr:int = 0
    i:int = n
    while (n <= i and i <= m):
        if(es_abundante(i)):
            vr = vr + i
        i= i + 1
    return vr

def abundantemayor(k:int)->int:
    '''
    Obtiene el numero abundante mas cercano mayor que k
    Requiere: k mayor que cero
    Devuelve: el numero abundante mas cercano mayor que k

    '''
    j:int = k
    while es_abundante(j) == False:
        j = j + 1
    return j

def abundantemenor(k:int)->int:
    '''
    Obtiene el numero abundante mas cercano menor que k
    Requiere: k mayor que cero
    Devuelve: el numero abundante mas cercano menor que k

    '''
    numero_abundante:int = 0
    j:int = k
    
    while (j > 0) and (es_abundante(j) == False)  :
        j = j - 1
        if j > 0 and es_abundante(j):
            numero_abundante = j

    return numero_abundante

def abundante_mas_cercano(n:int)->int:
    '''
    Obtiene el número abundante más cercano a n, teniendo 
    en cuenta que:
    (I) si n es abundante, se espera obtener n;
    (II) en caso de haber más de uno (uno menor que n y 
    otro mayor que n), se espera obtener el mayor de ellos.
    Requiere: n entero mayor que cero
    Devuelve: el numero abundante mas cercano a n
    '''
    vr:int = 0

    if es_abundante(n):
        vr = n
    else:
        abundante_menor:int = abundantemenor(n)
        abundante_mayor:int = abundantemayor(n)
        if abundante_menor != 0:
            distancia_abundante_menor:int = abs(abundante_menor - n)
            distancia_abundante_mayor:int = abundante_mayor - n
            if(distancia_abundante_menor >= distancia_abundante_mayor):
                vr = abundante_mayor
            else:
                vr = abundante_menor
        else:
                vr = abundante_mayor

    return vr