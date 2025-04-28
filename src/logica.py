def adivinar(opciones, respuesta_correcta):
    """Función para adivinar la respuesta correcta de una pregunta.
    Args:
        opciones (list): Lista de opciones de respuesta.
        respuesta_correcta (list): Respuesta correcta.
    Returns:
        bool: True si la respuesta es correcta, False en caso contrario.
    """
    # Se obtiene la respuesta del usuario
    respuesta_usuario = input("Ingrese la letra de su respuesta: ").upper()
    if respuesta_usuario == respuesta_correcta[0]:
        return True
    else:
        return False