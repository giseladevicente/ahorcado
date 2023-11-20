# ahorcado
import os # Librería para limpiar pantalla
from rsc.modules.ahorcado import mostrar_palabra, mostrar_figura, decoracion

from random import choice

def main():

    os.system("cls")

    print(""" 
    Bienvenido al juego del ahorcado!!!
          
    Deberas ingresar letras para lograr adivinar la palabra.
    Tienes 6 intentos.
           
    Estas preparado?
          
    Comencemos el juego!!
    """)
    
    nombre_jugador = input("Ingresa tu nombre: ")

    decoracion()

    palabras = ["deltoides" , "tricep" , "trapecio" , "esternocleidomastoideo" , "pectoral"] 

    while True:
        palabra_secreta = choice(palabras)
        print(palabra_secreta)

        print(f"{nombre_jugador} la palabra que deberas adivinar tiene: {len(palabra_secreta)} letras")

        intentos = 6
        intentos_incorrectos = 0
        letras_adivinadas = []
        letras_ingresadas = []
        puntos = 0
        puntaje_base= 10
        descuento_intento_incorrecto = 5

        
        while intentos > 0:
            # os.system("cls")

            print(f"\n Letras ingresadas: {letras_ingresadas}")

            print(mostrar_figura(intentos_incorrectos))

            # Ingreso de letra
            print("\n Palabra: ", mostrar_palabra(palabra_secreta, letras_adivinadas))
            letra = input("\n Adivina una letra: ").lower()

            # Letra ingresada no es una letra o se ingreso + de 1.
            if len(letra) != 1 or not letra.isalpha():
                print(f"\n {nombre_jugador} por favor, introduce una letra válida.")
                os.system("pause")
                continue

            # Letra repetida
            if letra in letras_ingresadas:
                print(f"\n {nombre_jugador} ya probaste esa letra antes. Ingresa otra! ")
                os.system("pause")
                continue
            else: 
                letras_ingresadas.append(letra)
                # Letra incorrecta en palabra secreta
                if letra not in palabra_secreta:
                    intentos -= 1
                    print(f"\n Incorrecto. Te quedan {intentos} intentos.")
                    intentos_incorrectos += 1
                    puntos -= descuento_intento_incorrecto
                    print(f"Puntos: {puntos}")
                    decoracion()
                    # os.system("pause")
                else: #Letra adivinada
                    letras_adivinadas.append(letra)
                    print(f"\n Bien {nombre_jugador}!! La letra '{letra}' esta en la palabra.")
                    puntos += puntaje_base
                    print(f"\n Puntos: {puntos}")
                    decoracion()
            
            # GANO! -Cantidad de letras adivinadas == a cantidad de letras en palabra secreta  y consulta de reinicio de juego
            if all(letra in letras_adivinadas for letra in palabra_secreta): #todas las letras de palabra_secreta están en letras_adivinadas.
                print(f"Felicitaciones {nombre_jugador}!!! Ganaste")
                decoracion()
                break

            # PERDIÓ! - Intentos == 0 y consulta de reinicio de juego
            if intentos == 0:
                print(f"{nombre_jugador} Perdiste! La palabra era '{palabra_secreta}'.")
                decoracion()
                break

        # Puntaje final
        print(f"Tu puntaje final es: {puntos}")

        respuesta = input("\n ¿Quieres jugar nuevamente? (s/n): ").lower()
        decoracion()
        if respuesta != 's':
            print("Hasta luego")
            os.system("pause")
            break

os.system("cls")
