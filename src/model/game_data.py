class GameData:
    def __init__(self):
        #Es un diccionario que contiene las preguntas y respuestas del juego, por favor sigan el mismo formato.
        self.preguntas_y_respuestas = [
            {
                "pregunta": "Transformar el siguiente numero binario a decimal: 1010",
                "opciones": ["A) 8", "B) 10", "C) 12", "D) 14"],
                "respuesta_correcta": ["B", "10"]
            },
            {
                "pregunta": "Transformar el siguiente numero binario a decimal: 1101",
                "opciones": ["A) 11", "B) 12", "C) 13", "D) 14"],
                "respuesta_correcta": ["C", "13"]
            },
            {
                "pregunta": "Transformar el siguiente numero binario a decimal: 1110",
                "opciones": ["A) 14", "B) 15", "C) 13", "D) 12"],
                "respuesta_correcta": ["A", "14"]
            },
            {
                "pregunta": "Transformar el siguiente numero binario a decimal: 1001",
                "opciones": ["A) 7", "B) 8", "C) 9", "D) 10"],
                "respuesta_correcta": ["C", "9"]
            },
            {
                "pregunta": "Transformar el siguiente numero binario a decimal: 1111",
                "opciones": ["A) 15", "B) 16", "C) 14", "D) 13"],
                "respuesta_correcta": ["A", "15"]
            },
            {
                "pregunta": "Transformar el siguiente numero binario a decimal: 1011",
                "opciones": ["A) 10", "B) 11", "C) 12", "D) 13"],
                "respuesta_correcta": ["B", "11"]
            },
            {
                "pregunta": "Transformar el siguiente numero binario a decimal: 0101",
                "opciones": ["A) 4", "B) 5", "C) 6", "D) 7"],
                "respuesta_correcta": ["B", "5"]
            },
            {
                "pregunta": "Transformar el siguiente numero binario a decimal: 0011",
                "opciones": ["A) 2", "B) 3", "C) 4", "D) 5"],
                "respuesta_correcta": ["B", "3"]
            },
            {
                "pregunta": "Transformar el siguiente numero binario a decimal: 0110",
                "opciones": ["A) 5", "B) 6", "C) 7", "D) 8"],
                "respuesta_correcta": ["B", "6"]
            },
            {
                "pregunta": "Transformar el siguiente numero binario a decimal: 0001",
                "opciones": ["A) 0", "B) 1", "C) 2", "D) 3"],
                "respuesta_correcta": ["B", "1"]
            },
            {
                "pregunta": "Transformar el siguiente numero binario a decimal: 10100",
                "opciones": ["A) 18", "B) 19", "C) 20", "D) 21"],
                "respuesta_correcta": ["C", "20"]
            },
            {
                "pregunta": "Transformar el siguiente numero binario a decimal: 11010",
                "opciones": ["A) 26", "B) 27", "C) 28", "D) 29"],
                "respuesta_correcta": ["A", "26"]
            },
            {
                "pregunta": "Transformar el siguiente numero binario a decimal: 11100",
                "opciones": ["A) 28", "B) 29", "C) 30", "D) 31"],
                "respuesta_correcta": ["C", "30"]
            },
        ]
        
    # Funcion para obtener las preguntas y respuestas del juego, es llamada desde el main.py
    # y es la que se encarga de devolver la lista de preguntas y respuestas.
    # Lo que permite property es que se pueda llamar a la funcion como un atributo, sin necesidad de usar parentesis
    @property
    def obtener_preguntas_y_respuestas(self):
        """Devuelve la lista de preguntas del juego"""
        return self.preguntas_y_respuestas