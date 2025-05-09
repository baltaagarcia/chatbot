import csv
#recolectar preguntas y respuestas de un archivo CSV mediante su posicion(IMPAR=PREGUNTAS PAR=RESPUESTAS) en las filas
def recolectar_preguntas_y_respuestas(nombre_archivo):
    preguntas = []
    respuestas = []
    
    with open(nombre_archivo,) as archivo:
        lector = csv.reader(archivo)
        for i, fila in enumerate(lector):
            if i % 2 == 0:  
                preguntas.append(fila[0].strip().lower())
            else:  
                respuestas.append(fila[0].strip())
    return preguntas, respuestas


def buscar_pregunta(preguntas, respuestas, consulta_usuario):
    consulta_usuario = consulta_usuario.lower()
    if consulta_usuario in preguntas:
        posicion = preguntas.index(consulta_usuario)  
        return respuestas[posicion] 
    else:
        return "No tengo la información para responder esta consulta."

    




def main():
    
    archivo_csv= 'preguntas_y_respuestas.csv'
    preguntas, respuestas=recolectar_preguntas_y_respuestas(archivo_csv)
    print(preguntas)
    
    input_usuario=input("Bienvenido al chatbot. Escribe 'salir' para terminar o escribe tu pregunta: ").strip()
    while input_usuario != "salir":
        buscar_pregunta(preguntas, respuestas,input_usuario)
        if input_usuario in preguntas:
            respuesta= buscar_pregunta(preguntas, respuestas, input_usuario)
            print(respuesta)
        else:
            print("No tengo la informacion para responder esta consulta")

        input_usuario=input("Bienvenido al chatbot. Escribe 'salir' para terminar o escribe tu pregunta: ").strip()

           
main()