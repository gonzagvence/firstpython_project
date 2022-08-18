from abundante import es_divisor, suma_divisores_positivos, es_abundante, \
                      suma_abundantes, abundante_mas_cercano

def elegir_funcion() -> str:
    '''
    Despliega el menú de funciones disponibles en la pantalla y devuelve
    la opción elegida por el usuario
    Requiere: Nada.
    Devuelve: La opción elegida por el usuario, en mayúscula y sin espacios adelante y atrás según la siguiente codificación:
        A -> Divisivilidad de dos números;
        B -> Suma de los divisores positivos de un número;
        C -> Test de abundancia de un número;
        D -> Suma de números abundantes entre dos números;
        E -> Abundante más cercano a un número;
        F -> Finalizar;
    '''
    print()
    print('Funciones disponibles')
    print('---------------------')
    print('A. Divisibilidad de dos números [n,m]')
    print('B. Suma de divisores positivos [n]')
    print('C. Es abundante [n]')
    print('D. Suma de abundantes entre [n,m]')
    print('E. Abundante más cercano [n]')
    print('F. Finalizar')
    opción_elegida:str = input('Seleccione una opción: ').upper().strip()
    return opción_elegida
  

# Cuerpo principal del programa
finalizar:bool = False
while not finalizar:
    opcion_seleccionada:str = elegir_funcion()
    # Se analiza la opción elegida
    if opcion_seleccionada == 'A':
        n:str = input('Ingrese n: ')
        m:str = input('Ingrese m: ')
        if es_divisor(int(n),int(m)):
            print('El {} es divisor de {}.'.format(n, m))
        else:
            print('El {} no es divisor de {}.'.format(n, m))
    elif opcion_seleccionada == 'B':
        n:str = input('Ingrese n: ')
        resultado:int = suma_divisores_positivos(int(n))
        print('La suma de los divisores de {} es {}.'.format(n,resultado))
    elif opcion_seleccionada == 'C':
        n:str = input('Ingrese n: ')
        if es_abundante(int(n)):
            print('El {} es abundante.'.format(n))
        else:
            print('El {} no es abundante.'.format(n))
    elif opcion_seleccionada == 'D':
        n:str = input('Ingrese n: ')
        m:str = input('Ingrese m: ')
        resultado:int = suma_abundantes(int(n),int(m))
        print('La suma de los abundantes entre {} y {} es {}.'.format(n,m,resultado))
    elif opcion_seleccionada == 'E':
        n:str = input('Ingrese n: ')
        resultado:int = abundante_mas_cercano(int(n))
        print('El abundante más cercano a {} es {}.'.format(n,resultado))
    elif opcion_seleccionada == 'F':
        finalizar = True
    else:
        print('Opción inválida.')

    if opcion_seleccionada != 'F':
        input('Presione ENTER para continuar.')
