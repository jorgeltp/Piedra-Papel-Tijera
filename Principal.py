'''JUEGO DE PIEDRA PApEL O TIJERA:
    En este juego se enfrenta un jugador contra el ordenador, para ello se definen dos variables:
        
        jugador y maquina

    en jugador se guardará lo que saque el jugador (piedra, papel o tijera) y en maquina guardamos lo que saque
    el ordenador, lo cual se generará aleatoriamente mediante una función que se llama juega_maquina().
    
    EMPATE:
    Se definirá una función llamada empate, para evaluar el caso en que jugador y mmaquina saquen un mismo valor.
    
    GANA JUGADOR:
    jugador=piedra y maquina=tijera gana jugador
    jugador=papel y maquina=piedra gana jugador
    jugador=tijera y maquina=papel gana jugador'''

import random #Importamos el modulo ramdom para poder generar un numero aleatorio
import sys #Importamos el modulo sys para poder detener el programa en cualquier punto con sys.exit()

# A continuación definimos las diferentes funciones que utilizaremos en el juego

# Definimos la funcion lanzamiento() para que el jugador pueda lanzar

def lanzamiento(jugador):
    while jugador not in sg_seleccionar:
        jugador = input(f'{nombre}, escribe piedra, papel ó tijera: ').upper()
    return jugador

# La función juega_maquina(), ejecuta el lanzamiento aleatorio del ordenador

def juega_maquina(sg_seleccionar):
    aleatorio = random.choice(sg_seleccionar)
    return aleatorio

# La función compara_oponentes(), compara el lanzamiento de los dos jugadores y da un resultado DE LA PARTIDA
def compara_oponentes(jugador, maquina):
    if jugador == maquina:
        print(f'¨{nombre} LANZÓ {jugador} ORDENADOR LANZÓ {maquina}')
        print('¡¡¡HAY EMPATE!!!!')
    elif jugador == 'PIEDRA' and maquina == 'TIJERA':
        print(f'¨{nombre} LANZÓ {jugador} ORDENADOR LANZÓ {maquina}')
        print(f'¡¡¡GANA {nombre}!!!')
    elif jugador == 'PAPEL' and maquina == 'PIEDRA':
        print(f'¨{nombre} LANZÓ {jugador} ORDENADOR LANZÓ {maquina}')
        print(f'¡¡¡GANA {nombre}!!!')
    elif jugador == 'TIJERA' and maquina == 'PAPEL':
        print(f'¨{nombre} LANZÓ {jugador} ORDENADOR LANZÓ {maquina}')
        print(f'¡¡¡GANA {nombre}!!!')
    else:
        print(f'¨{nombre} LANZÓ {jugador} ORDENADOR LANZÓ {maquina}')
        print('¡¡¡GANA EL ORDENADOR!!!')


#JUEGO CONTINUO - EN ESTA FUNCIÓN VAMOS A HACER QUE EL JUGADOR CONTINÚE JUGANDO TODAS LAS VECES QUE QUIERA

def seguir_jugando(jugador):
    seguir = ('SI', 'NO')
    seguimos = input(f'{nombre}, ¿continuamos jugando? (SI ó NO): ').upper()
    while seguimos not in seguir:
        seguir_jugando(jugador)
    if seguimos == 'SI':
        jugador = ''
        maquina = ''
        rutina_ppal()
    else:
       print(f'ADIOS {nombre}, VUELVE CUANDO QUIERAS')
       sys.exit()

#RUTINA DE JUEGO
def rutina_ppal(jugador='', maquina = ''):
    jugador = lanzamiento(jugador)
    maquina = juega_maquina(sg_seleccionar)
    compara_oponentes(jugador, maquina)
    seguir_jugando(jugador='')

#//////////////////////////////////////////////////////////////
#RUTINA PRINCIPAL DEL JUEGO
#/////////////////////////////////////////////////////////////

#En las tres lineas siguientes preguntamos el nombre al jugador y le decimos que escoja piedra, papel o tijera
sg_seleccionar = ('PIEDRA', 'PAPEL', 'TIJERA')
jugador = ''
maquina = ''
nombre = input('''¡¡¡Vamos a jugar piedra, papel o tijera!!!
               ¿Cómo te llamas?: ''').upper()
rutina_ppal()