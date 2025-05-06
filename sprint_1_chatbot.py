
import csv
def leer_preguntas_csv(nombre_archivo):
    preguntas = {}

    with open(nombre_archivo, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            pregunta = fila['pregunta'].lower()
            respuesta = fila['respuesta']
            preguntas[pregunta] = respuesta



def buscar_pregunta(preguntas, consulta_usuario):
    consulta_usuario = consulta_usuario.lower()
    if consulta_usuario in preguntas:
        return preguntas[consulta_usuario]
    else:
        return "No tengo la informacion para responder esta consulta"
    




def main():
    nombre_archivo = 'preguntas.csv'
    preguntas = leer_preguntas_csv(nombre_archivo)
    input_usuario= ""
    while input_usuario.lower != "chau":
        input_usuario=input("Bienvenido al ChatBot! Respondere tus consultas")
        

