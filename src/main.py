#main
from model.game_data import GameData
from logica import adivinar
from puntaje import actualizarPuntaje, mostrarPuntaje

def AdivinanzasBinarias():
    print("Bienvenido a Adivinanzas Binarias")
    datos = GameData()
    
    for pregunta in datos.obtener_preguntas_y_respuestas:
        print("\n" + pregunta["pregunta"])
        
        opciones = "\n".join(pregunta["opciones"])
        print(opciones)
        
        es_correcto = adivinar(pregunta["respuesta_correcta"])
        if es_correcto:
            # Si la respuesta es correcta, se llama a la función contadorPuntaje() para actualizar el puntaje
            print("Correcto!")
        else:
            print("Incorrecto!")

        if not actualizarPuntaje(es_correcto):
            # Si el puntaje llega a 0 o supera 70, se termina el juego
            break
        mostrarPuntaje()
            
if __name__ == "__main__":
    AdivinanzasBinarias()