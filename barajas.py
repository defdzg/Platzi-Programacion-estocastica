import random
import collections

PALOS = ['espada', 'corazon', 'rombo', 'trebol'] #Con mayúsculas significa que es una constante
VALORES = ['a', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k']

def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))
            
    return barajas

def obtener_mano(barajas, tamano_mano):
    mano = random.sample(barajas, tamano_mano)
    
    return mano

# Probabilidad de encontrar una corrida en una probabilidad de 5 cartas  
    # El color (flush) o también llamado "corrida" es una combinación de 
    # cinco cartas del mismo palo (o más), no necesariamente consecutivas.   
    
def corrida(manos):
    valores = []
    for mano in manos:
        for carta in mano:
            valores.append(carta[1])
            
    counter = dict(collections.Counter(valores))
    
    cinco = 0

    for val in counter.values():
        if val == 5:
            cinco += 1
            break
    
    print (counter.values())
    return(cinco)
    
def main(tamano_mano, intentos):
    barajas = crear_baraja()
    
    manos = []
    
    for __ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)
    
    flush = corrida(manos)
    
    probabilidad = flush/intentos
    
    print(f'La probabilidad de obtener una corrida en una mano de tamano {tamano_mano} es {probabilidad}')
        
if __name__ ==  '__main__':
    tamano_de_mano = int(input('De cuantas barajas será la mano: '))
    intentos = int(input('Cuantos intentos de la simulacion: '))
    main(tamano_de_mano, intentos)
    
    #print(mano)
    #print(barajas)