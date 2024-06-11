# Importación de la función choice del módulo random
from random import choice 


# Mensaje inicial. 
def mostrar_introduccion(): 
    # Procedimiento que presenta un mensaje de bienvenida y establece las reglas básicas del juego antes de comenzar.
    print(""" 
    Bienvenido al juego del ahorcado!!!
          
    Deberás ingresar letras o palabras para lograr adivinar la palabra secreta.
          
    Tienes 6 intentos.
          
    Antes de comenzar quiero comentarte que según tu elección, de ingresar letra o palabra, el puntaje será distinto
    tanto para los intentos correctos como para los intentos incorrectos.
           
    ¿Estás preparado?
          
    Comencemos el juego!!
    """)

# Linea decorativa. 
def decoracion(): 
    # Función que imprime un salto de linea y 50 asteriscos en la consola. 
    print("\n") 
    deco = print("*"*50) 
    return deco 

# Palabra aleatoria
def obtener_palabra_secreta(): 
    # Función que devuelve una palabra aleatoria de la lista predefinida 'palabras'.
    palabras = ["casa", "perro", "pato", "fresa", "pera"] 
    return choice(palabras) 


# Representación gráfica figura ahorcado
def mostrar_figura(intentos):
    # Función que devuelve una representación gráfica del ahorcado según la cantidad de intentos incorrectos.
    figuras = [
        """
           +---+
           |   |
               |
               |
               |
               |
        =========""",
        """
           +---+
           |   |
           O   |
               |
               |
               |
        =========""",
        """
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========""",
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========""",
        """
           +---+
           |   |
           O   |
          /|\  |
               |
               |
        =========""",
        """
           +---+
           |   |
           O   |
          /|\  |
          /    |
               |
        =========""",
        """
           +---+
           |   |
           O   |
          /|\  |
          / \  |
               |
        ========="""
    ]
    return figuras[intentos]



# Mostrar letras adivinadas y no adivinadas
def mostrar_palabra(palabra, letras_adivinadas):
    # Función que muestra la representación visual de la palabra oculta con letras adivinadas y guiones bajos para letras no adivinadas.
    resultado = "" 
    for letra in palabra: 
        if letra in letras_adivinadas:
            resultado += f" {letra} "
        else:
            resultado += " _ "
    return resultado

# Proceso Letras
def procesar_letra(letra, letras_ingresadas, intentos, intentos_incorrectos, palabra_secreta, letras_adivinadas, puntos, puntaje_base, descuento_intento_incorrecto, nombre_jugador):
    # Función que procesa la letra ingresada por el jugador y actualiza los estados del juego.
    if len(letra) != 1 or not letra.isalpha(): # Letra ingresada no es una letra o se ingreso + de 1.
        print(f"\n {nombre_jugador} por favor, introduce una letra válida.") 
        return intentos, intentos_incorrectos, puntos


    # Letra repetida
    if letra in letras_ingresadas: 
        print(f"\n {nombre_jugador} ya probaste esa letra antes. Ingresa otra! ")
        return intentos, intentos_incorrectos, puntos 

    letras_ingresadas.append(letra)
    
    decoracion()

     # Letra incorrecta en palabra secreta
    if letra not in palabra_secreta:
        intentos -= 1
        print(f"\n Incorrecto. Te quedan {intentos} intentos.")
        intentos_incorrectos += 1
        puntos -= descuento_intento_incorrecto
        print(f"Puntos: {puntos}")
        decoracion()
    else:  #Letra adivinada
        letras_adivinadas.append(letra)
        print(f"\n Bien {nombre_jugador}!! La letra '{letra}' está en la palabra.")
        puntos += puntaje_base
        print(f"\n Puntos: {puntos}")
        decoracion()

    return intentos, intentos_incorrectos, puntos

#Proceso palabra
def procesar_palabra(palabra_ingresada, palabra_secreta, intentos, intentos_incorrectos, puntos, puntaje_base, letras_adivinadas, nombre_jugador):
    # Función que procesa la palabra ingresada por el jugador y actualiza los estados del juego.
    ganador = False

    if  not palabra_ingresada.isalpha(): 
        print(f"\n {nombre_jugador} por favor, introduce una palabra válida.") 
    elif palabra_ingresada == palabra_secreta:
        decoracion()
        print(f"Felicitaciones {nombre_jugador}!!! Ganaste")
        puntos += (len(palabra_secreta) - len(letras_adivinadas)) * 30
        ganador = True
    else:
        intentos -= 1
        print(f"\n Incorrecto. Te quedan {intentos} intentos.")
        intentos_incorrectos += 1
        puntos -= 10
        print(f"Puntos: {puntos}")
        decoracion()

    return ganador, intentos, intentos_incorrectos, puntos
