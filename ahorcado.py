""" Deberán crear una aplicación de consola que simulara el juego del “Ahorcado”, que permita:
1-Palabras ocultas: Definir una lista de palabras predefinidas de las cuales se seleccionará una
aleatoriamente como la palabra oculta en cada partida.
  
2-Visualización del ahorcado: Crear una función que muestre la figura del ahorcado progresivamente a
medida que el jugador adivina letras incorrectas.

3-Registro de intentos: Permitir que los jugadores ingresen letras para adivinar la palabra oculta y llevar
un registro de los intentos.

4-Verificación de adivinanzas: Validar si la letra ingresada por el jugador está presente en la
palabra oculta y mostrar su posición en caso de acierto.
5-Control de fin de juego: Establecer una condición de finalización del juego, como adivinar la palabra
correctamente o completar la figura del ahorcado. """

from rsc.modules.funciones import mostrar_introduccion, decoracion, obtener_palabra_secreta, mostrar_palabra, mostrar_figura, procesar_letra, procesar_palabra

def main(): # Función principal que contiene todo el flujo principal del juego.
  
    mostrar_introduccion() # Mensaje de bienvenida y reglas básicas del juego.
 
    nombre_jugador = input("Ingresa tu nombre: ") # Solicita nombre al jugar.

    decoracion()
    
    #Bucle principal del juego
    # Finaliza cuando el jugador decide no jugar más, en caso contrario se restablece su contenido permitiendo realizar un nuevo juego. 
    while True: 
        # Configuración inicial
        palabra_secreta = obtener_palabra_secreta()
        print(palabra_secreta)

        #Cantidad de letras en palabra secreta
        print(f"{nombre_jugador} la palabra que deberas adivinar tiene: {len(palabra_secreta)} letras")

        intentos = 6 # Intentos totales
        intentos_incorrectos = 0 
        letras_adivinadas = []
        letras_ingresadas = [] # Contiene las letras adivinadas y no adivinadas
        puntos = 0
        puntaje_base = 10 # Puntaje por letra correcta 
        descuento_intento_incorrecto = 5 # Descuento de puntaje por letras incorrectas 

        # Bucle para cada intento del jugador
        while intentos > 0:
            # información del juego
            print(f"\n Letras ingresadas: {letras_ingresadas}")

            print(mostrar_figura(intentos_incorrectos))

            print("\n Palabra: ", mostrar_palabra(palabra_secreta, letras_adivinadas))

            # Ingreso letra or palabra?    
            letra_o_palabra = input("\n ¿Quieres Adivinar una letra o arriesgar palabra? (L para letra, P para palabra): ").lower()

            #Ingreso de letra
            if letra_o_palabra == 'l':
                letra = input("Ingrese una letra: ").lower() 
                intentos, intentos_incorrectos, puntos = procesar_letra(
                    letra, letras_ingresadas, intentos, intentos_incorrectos, palabra_secreta,
                    letras_adivinadas, puntos, puntaje_base, descuento_intento_incorrecto, nombre_jugador
                )     
                # # GANO! -Cantidad de letras adivinadas == a cantidad de letras en palabra secreta
                if all(letra in letras_adivinadas for letra in palabra_secreta):
                    print(f"Felicitaciones {nombre_jugador}!!! Ganaste")
                    break

            #Ingreso de palabra
            elif letra_o_palabra == 'p':
                palabra_ingresada = input("Ingrese una palabra: ").lower() 
                ganador, intentos, intentos_incorrectos, puntos = procesar_palabra(palabra_ingresada, palabra_secreta, 
                intentos, intentos_incorrectos, puntos,
                puntaje_base, letras_adivinadas, nombre_jugador
                )
                if ganador:
                    break
            else: #Ingreso otro caracteres que no es 'p' ni 'l'
                print(f"\n {nombre_jugador} por favor, introduce una opción válida (L o P).")
                continue

            #Perdió - Sin intentos
        else:
            print(mostrar_figura(intentos_incorrectos))
            print(f"{nombre_jugador} Perdiste! La palabra era '{palabra_secreta}'.")
            

        # Puntaje final
        print(f"Tu puntaje final es: {puntos}")
        decoracion()

        # Consulta de reinicio de juego
        respuesta = input("\n ¿Quieres jugar nuevamente? (s/n): ").lower()

        while respuesta != "n":
            if respuesta == "s":
                decoracion()
                break
            else:
                if not respuesta.isalpha() or respuesta !="s" and respuesta !="n":
                    print(f"\n {nombre_jugador} por favor, introduce una letra válida.")
                    respuesta = input("\n ¿Quieres jugar nuevamente? (s/n): ").lower()    
        else:
            decoracion()
            print("""¡Espero que hayas disfrutado poniendo a prueba tus habilidades de adivinanza!
                  
                    ¡Hasta luego y gracias por jugar!""")
            break
        

if __name__ == "__main__":
    main()
