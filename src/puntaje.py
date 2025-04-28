# Variables globales para el puntaje, aciertos y fallos
puntaje = 15
aciertos = 0
fallos = 0

def actualizarPuntaje(es_correcto):
    """
    Actualiza el puntaje según si la respuesta es correcta o incorrecta.
    :param es_correcto: Booleano que indica si la respuesta fue correcta.
    :return: True si el juego continúa, False si el juego debe terminar.
    """
    global puntaje, aciertos, fallos

    if es_correcto:
        puntaje += 10
        aciertos += 1
    else:
        puntaje -= 5
        fallos += 1

    # Verificar condiciones de fin del juego
    if puntaje <= 0:
        print("¡Perdiste!")
        return False  # Indica que el juego debe terminar
    elif puntaje >= 70:
        print("¡Felicidades, Ganaste!")
        return False  # Indica que el juego debe terminar

    return True  # El juego continúa

def mostrarPuntaje():
    """
    Muestra el puntaje actual, aciertos y fallos.
    """
    global puntaje, aciertos, fallos
    print(f"Puntaje actual: {puntaje}")
    print(f"Aciertos: {aciertos}, Fallos: {fallos}")