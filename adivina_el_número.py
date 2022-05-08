import random


def run():
    numero_aleatorio = random.randint(1, 100)
    
    numero_elegido = int(input('Elige un número del 1 al 100: '))
            
    if numero_elegido != numero_aleatorio:
        while numero_aleatorio != numero_elegido:
            if numero_aleatorio > numero_elegido:
                numero_elegido = int(input('Elige un numero mas grande: '))
            
            else:
                numero_elegido = int(input('Elige un numero mas pequeño: '))
                
        print('HAS GANADO!!!')


if __name__ == '__main__':
    run()