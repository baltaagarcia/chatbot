import csv
#recolectar preguntas y respuestas de un archivo CSV mediante su posicion(IMPAR=PREGUNTAS PAR=RESPUESTAS) en las filas
def recolectar_preguntas_y_respuestas(nombre_archivo):
    preguntas = []
    respuestas = []
    
    with open(nombre_archivo, mode="r+", newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        for i, fila in enumerate(lector):
            if i % 2 == 0:  
                preguntas.append(fila[0].strip().lower())
            else:  
                respuestas.append(fila[0].strip().lower())
    return preguntas, respuestas


def buscar_pregunta(preguntas, respuestas, consulta_usuario):
    consulta_usuario = consulta_usuario.lower()
    if consulta_usuario in preguntas:
        posicion = preguntas.index(consulta_usuario)  
        return respuestas[posicion] 
    else:
        return "No tengo la informacion para responder esta consulta."
    
def contar_filas(archivo):
    archivo.seek(0)
    return sum(1 for _ in archivo)
    
def agregar_pregunta(nueva_pregunta, consulta_usuario):
    with open(consulta_usuario, mode='r+', newline='', encoding='utf-8') as archivo:
        archivo.seek(0)
        if contar_filas(archivo) % 2 == 0:
            escritor = csv.writer(archivo)
            escritor.writerow([nueva_pregunta])

def agregar_respuesta(nueva_respuesta, consulta_usuario):
    with open(consulta_usuario, mode='r+', newline='', encoding='utf-8') as archivo:
        archivo.seek(0)
        if contar_filas(archivo) % 2 == 1:
            escritor = csv.writer(archivo)
            escritor.writerow([nueva_respuesta])


def es_valida (nueva_pregunta):
    if nueva_pregunta.strip().endswith("?"):
        print ("Buena pregunta! Voy a agregarla al sistema")
        return True
    else:
        print ("No puedo agregar esta pregunta, prueba colocando un: ?")
        return False 

    




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
            continuar = int(input("Quiere agregar esta pregunta? Ingrese 1 para agregar, 2 para descartar: "))
            while continuar > 2 or continuar < 1:
                continuar = int(input("Valor invalido. Ingrese 1 para agregar, 2 para descartar: "))
            if continuar == 1:
                while es_valida(input_usuario) != True:
                    input_usuario=input("Ingrese su pregunta correctamente: ").strip()
                agregar_pregunta(input_usuario, archivo_csv)
                nueva_respuestas = input("Ingrese la respuesta a su pregunta: ")
                agregar_respuesta(nueva_respuestas, archivo_csv)
                print("Pregunta y respuesta almacenada correctamente!")
            else:
                print("Pregunta descartada con exito!")

        input_usuario=input("Bienvenido al chatbot. Escribe 'salir' para terminar o escribe tu pregunta: ").strip()

           
main()