import random

# Función para obtener una palabra al azar de una lista de palabras
def obtener_palabra():
    palabras = ["python", "programacion", "chatgpt", "tecnologia", "odoo", "javascript", "desarrollo", "web", "aplicaciones", "moviles", "inteligencia", "artificial", "machine", "learning", "deep", "learning", "redes", "neuronales", "big", "data", "analitica", "datos", "ciencia", "datos", "estadistica", "probabilidad", "matematicas", "algoritmos", "computacion", "informatica"]
    return random.choice(palabras)

# Función para mostrar el estado actual de la palabra con las letras adivinadas
def mostrar_palabra(palabra, letras_adivinadas):
    resultado = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado

# Función principal del juego
def jugar_ahorcado():
    print("Bienvenido al juego del ahorcado!")
    print("Tienes 6 intentos para adivinar la palabra.")

    palabra = obtener_palabra()
    intentos_restantes = 6
    letras_adivinadas = []
    juego_terminado = False

    while not juego_terminado:
        # Mostrar la palabra con las letras adivinadas
        print(mostrar_palabra(palabra, letras_adivinadas))

        if intentos_restantes == 0:
            print("¡Perdiste! La palabra era:", palabra)
            break

        # Solicitar al jugador que ingrese una letra
        letra = input("Ingresa una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra. Intenta con otra.")
            continue

        if letra in palabra:
            letras_adivinadas.append(letra)
            if set(letras_adivinadas) == set(palabra):
                print("¡Felicidades! ¡Has adivinado la palabra:", palabra, "!")
                break
        else:
            intentos_restantes -= 1
            print("Letra incorrecta. Te quedan", intentos_restantes, "intentos.")

    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").lower()
    if jugar_de_nuevo == "s":
        jugar_ahorcado()
    else:
        print("Gracias por jugar. ¡Hasta luego!")

# Iniciar el juego
jugar_ahorcado()
