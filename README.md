#Explicación código

from random import choice # Se importa la función choice de la librería import

#Palabras
# Esta función desempeña un papel crucial en nuestro juego
    Su propósito es seleccionar aleatoriamente una palabra de una lista predefinida 'palabras'.
    Utiliza la función choice del módulo random para seleccionar aleatoriamente una palabra de  
    la lista palabras que va a ser utilizada en el código principal para obtener la palabra que el   
    jugador debe adivinar.

def obtener_palabra_secreta(): 
    palabras = ["deltoides", "tricep", "trapecio", "cartuchera", "pectoral"] 
    return choice(palabras) # La palabra seleccionada se devuelve como resultado de la función.


#Mensaje Inicial
# La principal tarea de la función mostrar_introduccion() es dar la bienvenida a los jugadores de 
    manera amigable e introducirlos al Juego del Ahorcado en consola.
    Establece un tono positivo para la partida y sirve como un guía inicial, explicando las reglas 
    básicas del juego preparando al jugador para comenzar el juego.  

def mostrar_introduccion():
    print(""" 
    Bienvenido al juego del ahorcado!!!
          
    Deberás ingresar letras para lograr adivinar la palabra.
    Tienes 6 intentos.
           
    ¿Estás preparado?
          
    Comencemos el juego!!
    """)


# Linea decorativa
# La función imprime una decoración visual en la consola antes de ciertos eventos, como al   
    finalizar el juego.

def decoracion():
print("\n") # imprime una nueva línea en la consola, lo que añade un espacio en blanco antes
de la decoración de asteriscos.
deco = print("*"*50) # Se crea una variable que guarda la impresión de una línea de 50  
asteriscos. Esto se logra multiplicando el carácter "*" por 50.
    return deco # Se retorna el valor de la variable deco.







#Mostrar letras adivinadas y no adivinadas
# Esta función genera la representación visual de la palabra oculta con letras adivinadas y 
    guiones bajos para letras no adivinadas.

def mostrar_palabra(palabra, letras_adivinadas): # establece la creación de una función llamada mostrar_palabra que toma dos parámetros: palabra y letras_adivinadas.
resultado = "" # inicializa una cadena vacía llamada resultado que se utilizará para construir la 
representación visual de la palabra oculta.
    for letra in palabra: # itera a través de cada letra en la palabra que se está adivinando.
        if letra in letras_adivinadas: # verifica si la letra actual está en la lista letras_adivinadas.
            resultado += f"{letra} "  # se guarda en la variable resultado y se agrega un espacio. 
        else: # Si no está adivinada, se agrega un guion bajo entre dos espacios.
            resultado += " _ "
    return resultado # retornando la cadena construida que representa la palabra con 
    	las letras adivinadas y los guiones bajos para las letras no adivinadas.
	

# Proceso Letras
# Esta función es la encargada de manejar el flujo del juego cuando el jugador ingresa una letra. 
   Refleja cómo cada elección del jugador afecta directamente su progreso y puntaje.
   Toma varios parámetros relacionados con el estado del juego ya que Su función principal es   
   verificar si la letra ingresada es válida y luego actualizar los estados del juego en consecuencia,
   como el puntaje y el control de los intentos.

def procesar_letra(letra, letras_ingresadas, intentos, intentos_incorrectos, palabra_secreta, letras_adivinadas, puntos, puntaje_base, descuento_intento_incorrecto, nombre_jugador):
    if len(letra) != 1 or not letra.isalpha(): # Se verifica si la longitud de la cadena letra no es
    igual a 1, lo cual significa que el jugador ingresó más de una letra o si la variable letra     
     no es alfabética. Esta porción de código asegura de que la entrada sea realmente una 
     letra y no otro tipo de carácter.
print(f"\n {nombre_jugador} por favor, introduce una letra válida.")  # Si la letra ingresada
es + de 1 letra o no es una letra se imprime un mensaje de advertencia en la consola indicando al jugador que la entrada no es válida.
        return intentos, intentos_incorrectos, puntos # devuelve los estados actuales del juego 
        	sin realizar cambios, ya que la entrada del jugador no fue válida.


    # Letra repetida
    # verifica si la letra ingresada (letra) ya ha sido ingresada anteriormente y por lo tanto 
    se encuentra en la lista de letras ingresadas (letras_ingresadas), la cual almacena todas 
    las letras que el jugador ha intentado adivinar hasta el momento.

    if letra in letras_ingresadas:                   
        print(f"\n {nombre_jugador} ya probaste esa letra antes. Ingresa otra! ")  # imprime 
       	 un mensaje informando al jugador que ya ha intentado adivinar esa letra previamente y
              	le pide que ingrese otra.
        return intentos, intentos_incorrectos, puntos # devuelve los estados actuales del juego 
        	sin realizar cambios, ya que la letra ya fue ingresada anteriormente y no debe afectar 
        	los intentos, intentos incorrectos o los puntos del jugador.

    letras_ingresadas.append(letra) # se utiliza el método .append de las listas para agregar 
    	la letra ingresada por el jugador a la lista letras_ingresadas. 
                                    
    # Letra incorrecta en palabra secreta
    # Si la letra es incorrecta Esta estructura de control disminuye el número de intentos, 
        aumenta la cantidad de intentos incorrectos, reduce el puntaje del jugador y proporciona    
        mensajes informativos al jugador.  

    if letra not in palabra_secreta: #  verifica si la letra ingresada por el jugador (letra) no está
    	presente en la palabra secreta (palabra_secreta)
        intentos -= 1 # disminuye en 1 el número de intentos restantes.
        print(f"\n Incorrecto. Te quedan {intentos} intentos.") # imprime un mensaje informando
al jugador que la letra ingresada es incorrecta y muestra la cantidad de intentos restantes.
        intentos_incorrectos += 1 #  incrementa en 1 la cantidad de intentos incorrectos.
        puntos -= descuento_intento_incorrecto # reduce el puntaje del jugador en una cantidad
        	predefinida (descuento_intento_incorrecto) por cada intento incorrecto.
        print(f"Puntos: {puntos}") #  imprime el puntaje actual del jugador.
        decoracion() # llama a la función decoracion(), que imprime una línea decorativa en la 
        	consola.

        # Si la letra está en la palabra secreta, el flujo de control va al bloque else, se suma a la lista  
           de letras adivinadas, muestra un mensaje de celebración e incrementa el puntaje.
    else:  # En caso que la Letra sea adivinada
        letras_adivinadas.append(letra) # agrega la letra a la lista letras_adivinadas, que era la lista 
       	que almacena las letras que el jugador ha adivinado correctamente.
        print(f"\n Bien {nombre_jugador}!! La letra '{letra}' está en la palabra.") # informa al jugador
que adivinó correctamente y muestra la letra adivinada.
        puntos += puntaje_base # incrementa el puntaje del jugador con el puntaje predefinido
(puntaje_base) por adivinar correctamente una letra.
        print(f"\n Puntos: {puntos}") # imprime el puntaje actualizado del jugador.
        decoracion() # llama a la función decoracion() para imprimir una línea decorativa.

    return intentos, intentos_incorrectos, puntos # devuelve tres valores: la cantidad de intentos
restantes, la cantidad de intentos incorrectos acumulados y el puntaje actual del jugador. Estos valores se utilizan para actualizar las variables en el bucle principal del juego y continuar el flujo del programa.



# Proceso palabra
# Esta función maneja el proceso cuando el jugador decide arriesgarse a adivinar la palabra   
   completa.
   Su función principal es verificar si la palabra ingresada coincide con la palabra secreta 
   seleccionada aleatoriamente.
   Además, calcula el puntaje, que es distinto al de la letra, y lleva el control de los intentos, 
   y actualizando los estados del juego en consecuencia... por lo que toma varios parámetros   
   relacionados con el estado del juego.

def procesar_palabra(palabra_ingresada, palabra_secreta, intentos, intentos_incorrectos, puntos, puntaje_base, letras_adivinadas, nombre_jugador):
    ganador = False # Bandera. inicializa una variable llamada ganador y la establece en False. 
                                 # Esta variable se usará para determinar si el jugador ganó el juego.
    if palabra_ingresada == palabra_secreta: # Se verifica si la palabra_ingresada es igual a la 
palabra_secreta. Si es cierto, significa que el jugador ha adivinado correctamente la 
palabra completa.
        print(f"Felicitaciones {nombre_jugador}!!! Ganaste") # se imprime un mensaje de
felicitación
puntos = (puntaje_base * len(letras_adivinadas)) + (len(palabra_secreta) - len(letras_adivinadas)) * 30 # se calcula el puntaje 
        decoracion() # Se muestra una decoración para presentar visualmente el resultado.
        ganador = True # establece la variable ganador en True.
    else:
        intentos -= 1 # se disminuye en 1 el número de intentos restantes.
        print(f"\n Incorrecto. Te quedan {intentos} intentos.")  # se imprime un mensaje indicando
 que la adivinanza es incorrecta se muestran la cantidad de intentos restantes.
        intentos_incorrectos += 1 # Se suma 1 al acumulador de intentos_incorrectos
        puntos -= 10 # Se decrementa el puntaje en 10 puntos en lugar de 5.
        print(f"Puntos: {puntos}") # Se imprime el puntaje actual.
        decoracion() # Se muestra una decoración para presentar visualmente el resultado.

    return ganador, intentos, intentos_incorrectos, puntos # La función retorna los valores
 actualizados de intentos, intentos_incorrectos y puntos y el valor que tiene la variable 
ganador. Estos valores se utilizan en el bucle principal del juego para gestionar el flujo del programa.
   


# Representación gráfica figura ahorcado
# Esta función proporciona una representación gráfica del ahorcado en función de la cantidad de  
   intentos incorrectos realizados por el jugador. Este gráfico se utiliza para mostrar visualmente  
   el progreso del juego y la situación actual del jugador.
   La función toma como parámetro el número de intentos incorrectos y, en base a este valor, 
   elige la representación gráfica correspondiente, y cada llamada a esta función actualiza la 
   figura en la consola, dándole al jugador una visión visual de cuántos intentos incorrectos ha  
   acumulado.

def mostrar_figura(intentos):
    # Se define una lista llamada figuras que contiene representaciones visuales del ahorcado en 
         diferentes etapas.
    # Cada elemento de la lista es una cadena de texto que representa una parte específica de la
         figura. 
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
    return figuras[intentos] #La función retorna el elemento de la lista figuras que corresponde a
 la cantidad de intentos incorrectos realizados por el jugador. 
# Esto permite mostrar la figura del ahorcado de acuerdo con la cantidad de errores cometidos.



"""
Juego del Ahorcado en consola
El objetivo es adivinar una palabra oculta, seleccionada aleatoriamente de una lista predefinida, antes de agotar
todos los intentos disponibles.
"""

# Importación de funciones del archivo "funciones" contenido en las carpetas: rsc y modules 
from rsc.modules.funciones import mostrar_introduccion, decoracion, obtener_palabra_secreta, mostrar_palabra, mostrar_figura, procesar_letra, procesar_palabra

#Funcion main


def main(): #La función main marca el punto de partida del juego. Es la función principal que
 contiene todo el flujo principal del juego

    mostrar_introduccion() # se llama a mostrar_introduccion() para presentar al jugador el
mensaje de bienvenida e introducción al juego. 

    nombre_jugador = input("Ingresa tu nombre: ") # Solicita al jugador su nombre y lo guarda en
la variable nombre_jugador

    decoracion() # se imprime una decoración

    # while True
# Después de la función main, entra en juego el bucle while True, este bucle se ejecuta continuamente, permitiendo que el jugador volver a participar del juego sin tener que volver a ejecutar todo el programa.
    
    while True:  # -> Genera un bucle infinito hasta que el jugador decide no jugar mas.

        palabra_secreta = obtener_palabra_secreta() 
        print(palabra_secreta)
        
        print(f"{nombre_jugador} la palabra que deberas adivinar tiene: {len(palabra_secreta)} 
        letras") #Imprime la cantidad de letras en palabra secreta.

#Dentro del bucle True se realiza la configuración inicial para cada juego. Se declaran e  
   inicializan variables claves que afectan el flujo del juego, para rastrear el progreso del 
   jugador y determinar el resultado final.
        intentos = 6 # Número inicial de intentos.
        intentos_incorrectos = 0 #  Contador de intentos incorrectos
        letras_adivinadas = [] # Lista de letras que el jugador ha adivinado correctamente.
        letras_ingresadas = [] # Es una lista que se va actualizando a medida que el jugador ingresa 
letras.
        puntos = 0 # puntaje actual del jugador.
        puntaje_base= 10 # El puntaje base que el jugador puede ganar.
        descuento_intento_incorrecto = 5 # Puntos descontados por letra no adivinada.



        # Bucle para cada intento del jugador
        # Este bloque de código representa un ciclo de juego donde se muestran las estadísticas 
actuales, se muestra la figura del ahorcado actualizada, la palabra oculta con las letras
adivinadas, y las letras ingresadas por el jugador.
Se recopila la entrada del jugador (si desea arriesgar letra o palabra completa) y se procesa para actualizar el estado del juego utilizando las funciones procesar_letra() y procesar_palabra().
        # Se verifica si el jugador ha ganado (adivinado la palabra completa) o perdido (se quedó sin 
intentos).
        # El bucle continúa hasta que el jugador gane o se quede sin intentos.
        # Al final del juego, se muestra un mensaje de felicitación si el jugador ha ganado, o se  
revela la palabra correcta si ha perdido. Al salir del bucle se muestra el puntaje obtenido y consulta si desea volver a jugar nuevamente.

        while intentos > 0: #Controla cada intento. Ejecuta mientras haya intentos disponibles.

            print(f"\n Letras ingresadas: {letras_ingresadas}") #Muestra en la consola las letras que el 
jugador ha ingresado hasta el momento.

            print(mostrar_figura(intentos_incorrectos)) #Utiliza la función mostrar_figura para 
imprimir en la consola la representación gráfica de la figura del ahorcado, basándose en la cantidad de intentos incorrectos.

            print("\n Palabra: ", mostrar_palabra(palabra_secreta, letras_adivinadas)) #Muestra en la 
consola la palabra que el jugador está tratando de adivinar, con las letras adivinadas hasta el momento reveladas y las letras no adivinadas ocultas como guiones bajos, por lo que la función mostrar_palabra toma los argumentos palabra_secreta y letras_adivinadas.

            # Ingreso letra o palabra?   	 
letra_o_palabra = input("\n ¿Quieres Adivinar una letra o arriesgar palabra? (L para letra, P para palabra): ").lower() # Solicita al jugador que elija si quiere adivinar una letra o 
arriesgar la palabra completa. La entrada se convierte a minúsculas para evitar problemas de coincidencia de mayúsculas y minúsculas.

            #Ingreso de letra
            if letra_o_palabra == 'l': # Si el jugador elige adivinar una letra ('l'),
                letra = input("Ingrese una letra: ").lower() # Se solicita al jugador que ingrese una letra y   
se utiliza la función lower para convertir lo ingresado a minúscula 

intentos, intentos_incorrectos, puntos = procesar_letra(letra, letras_ingresadas, intentos, intentos_incorrectos, palabra_secreta, letras_adivinadas, puntos, puntaje_base, descuento_intento_incorrecto, nombre_jugador) # Se guarda en cada  
variable según corresponda el resultado actualizado por cada intento que 
realiza utilizando la función procesar_letra.







            #Ingreso de palabra    
            elif letra_o_palabra == 'p': #Si el jugador elige arriesgar la palabra completa ('p')
                palabra_ingresada = input("Ingrese una palabra: ").lower() # Se solicita al jugador que 
ingrese la palabra y se procesa utilizando la función procesar_palabra.

                ganador, intentos, intentos_incorrectos, puntos = procesar_palabra(palabra_ingresada, 
  palabra_secreta, intentos, intentos_incorrectos, puntos, puntaje_base,  
  letras_adivinadas, nombre_jugador)

                if ganador: # Si la variable ganador es True sale del bucle e ingresa al bucle While True.
                    break
                   
            else: # Si la opción ingresada no es válida (Ingreso otro caracteres que no es 'p' ni 'l'),
                print(f"\n {nombre_jugador} por favor, introduce una opción válida (L o P).")   # se
imprime un mensaje solicitando al jugador que ingrese nuevamente una opción. 
                Continue # vuelve al comienzo del bucle while

            # GANO! 
               # Después de cada intento, se verifica si el jugador ha adivinado todas las letras de la   
palabra. 
            if all(letra in letras_adivinadas for letra in palabra_secreta):
                # La función all se utiliza para verificar si todos los elementos de un iterable (como una  
     lista, tupla o cadena) son evaluados como True. 
     Si todas las letras en letras adivinadas coinciden en cada letra en la palabra secreta =     
     True, es decir... -Cantidad de letras adivinadas == a cantidad de letras en palabra  
     secreta.
                print(f"Felicitaciones {nombre_jugador}!!! Ganaste") # se imprime un mensaje de
felicitación 
                decoracion() # se muestra la decoración
                break # y se rompe el bucle del juego.
            
            #Perdió - Sin intentos #Verifica si el jugador ha agotado todos sus intentos (intentos igual  
a 0).
            
        else: # Si esta condición del bucle while es falsa, es menor a 0, significa que el jugador ha 
     perdido el juego, 
            print(mostrar_figura(intentos_incorrectos)) # Se muestra la figura del ahorcado completa
            print(f"{nombre_jugador} Perdiste! La palabra era '{palabra_secreta}'.") # se muestra un 
mensaje indicando la palabra secreta
            decoracion() # se muestra la decoración y finaliza el bucle


        # Puntaje final
        print(f"Tu puntaje final es: {puntos}") # Después de salir del bucle del juego, se imprime el 
puntaje final del jugador.







        # Consulta de reinicio de juego
        # En la sección de consulta de reinicio se utiliza un bucle while True para gestionar la 
consulta de reinicio del juego

respuesta = input("\n ¿Quieres jugar nuevamente? (s/n): ").lower()  # Se le consulta al 
jugador si desea jugar nuevamente ingresando "s" si quiere jugar nuevamente o "n" si 
desea finalizar el juego.  La entrada del jugador se convierte a minúsculas para garantizar coherencia.

        decoracion() # Después de la consulta, se muestra la decoración.

        while respuesta != "n": # Se ingresa a una bucle while mientras la respuesta sea distinta a 
     "n" para asegurarse de manejar entradas incorrectas o inesperadas.
            if respuesta == "s": # Si la respuesta es igual a "s"
                break # Finaliza el bucle y entra en el bucle while True  
                        # obteniendo una nueva palabra secreta, restableciendo los intentos, puntajes y 
listas.
            else: #Si respuesta no es un caracter alfabético o es distinta a "s" y a "n"
                if not respuesta.isalpha() or respuesta !="s" and respuesta !="n":
                    print(f"\n {nombre_jugador} por favor, introduce una letra válida.") # Se imprime un 
mensaje con el nombre del jugador pidiéndole que introduzca una letra válida.

                    respuesta = input("\n ¿Quieres jugar nuevamente? (s/n): ").lower() # Vuelva a
consultar si quiere volver a jugar ingresando nuevamente en el bucle de reinicio. 
        else: # Si la respuesta es "n", quiere decir que el jugador decide no jugar más
            print("Hasta luego") # Imprime mensaje "Hasta luego"
            break # Sale del bucle
        

if __name__ == "__main__":
    main()

"""
# construcción que se utiliza en Python para determinar si el script actual se está ejecutando como el programa principal
 o si está siendo importado como un módulo en otro script.

__name__ es una variable especial en Python que se establece según el contexto en el que se está ejecutando el script.

Cuando el script se ejecuta directamente, __name__ se establece en "__main__", 
lo que significa que es el programa principal que se está ejecutando.

main() es la función principal del script que contiene todo el flujo principal del juego del ahorcado.


la línea if __name__ == "__main__": verifica si el script se está ejecutando directamente (no importado como módulo) 
y, en ese caso, llama a la función main(), iniciando así la ejecución del juego del ahorcado. 
"""
