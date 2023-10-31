from Sentimiento.Sentimiento_Positivo import Sentimiento_Positivo
from Sentimiento.Sentimiento_Negativo import Sentimiento_Negativo
import os
def contar_sentimientos(cadena, sentimientos_positivos, sentimientos_negativos):
    # Inicializamos contadores para sentimientos positivos y negativos
    contador_positivos = 0
    contador_negativos = 0
    # Convertimos la cadena a minúsculas para hacer la búsqueda insensible a mayúsculas
    cadena = cadena.lower()
    # Iteramos a través de los sentimientos positivos y contamos cuántas veces aparecen en la cadena
    for sentimiento in sentimientos_positivos:
        contador_positivos += cadena.count(sentimiento.sentimiento_positivo)
    # Iteramos a través de los sentimientos negativos y contamos cuántas veces aparecen en la cadena
    for sentimiento in sentimientos_negativos:
        contador_negativos += cadena.count(sentimiento.sentimiento_negativo)
    # Devolvemos el número de sentimientos positivos y negativos encontrados
    return contador_positivos, contador_negativos

class SentimientoDAO:
    def __init__(self):
        self.lista_sentimiento_positivo=[]
        self.lista_sentimiento_positivo_rechazado=[]
        self.lista_sentimiento_negativo=[]
        self.lista_sentimiento_negativo_rechazado=[]
    
    def nuevo_sentimiento_positivo(self, sentimiento):
        for sent in self.lista_sentimiento_positivo:
            if sent.sentimiento_positivo==sentimiento:
                return False
        for sent in self.lista_sentimiento_negativo:
            if sent.sentimiento_negativo==sentimiento:
                self.lista_sentimiento_positivo_rechazado.append(sentimiento)
                return True
        nuevo_sentimiento = Sentimiento_Positivo(sentimiento)
        self.lista_sentimiento_positivo.append(nuevo_sentimiento)
        return True

    def nuevo_sentimiento_negativo(self, sentimiento):
        for sent in self.lista_sentimiento_negativo:
            if sent.sentimiento_negativo==sentimiento:
                return False
        for sent in self.lista_sentimiento_positivo:
            if sent.sentimiento_positivo==sentimiento:
                self.lista_sentimiento_negativo_rechazado.append(sentimiento)
                return True
        nuevo_sentimiento = Sentimiento_Negativo(sentimiento)
        self.lista_sentimiento_negativo.append(nuevo_sentimiento)
        return True

    def imprimir_sentimiento(self):
        print("------------------------")
        print("Sentimientos Positivos: ")
        for sentimiento in self.lista_sentimiento_positivo:
            print(sentimiento.sentimiento_positivo)
        print("------------------------")
        print("Sentimientos Negativo: ")
        for sentimiento in self.lista_sentimiento_negativo:
            print(sentimiento.sentimiento_negativo)
        print("------------------------")

    def resetear_datos_sentimiento(self):
        self.lista_sentimiento_positivo.clear()
        self.lista_sentimiento_positivo_rechazado.clear()
        self.lista_sentimiento_negativo.clear()
        self.lista_sentimiento_negativo_rechazado.clear()

    def consultar_sentimiento_mensaje(self, lista_mensaje_fecha):
        if len(lista_mensaje_fecha)==0:
            return "No Existen Archivos De Mensajes Procesados."
        if len(self.lista_sentimiento_negativo)==0 or len(self.lista_sentimiento_positivo)==0:
            return "No Existen Archivos De Sentimientos Procesados."
        contador_mensaje_positivo=0
        contador_mensaje_negativo=0
        contador_mensaje_neutro=0
        respuesta=""
        for fecha in lista_mensaje_fecha:
            respuesta+="Fecha: "+fecha.fecha+"\n"
            for mensaje in fecha.lista_mensaje:
                positivo, negativo = contar_sentimientos(mensaje.texto_mensaje, self.lista_sentimiento_positivo, self.lista_sentimiento_negativo)
                if positivo>negativo:
                    contador_mensaje_positivo+=1
                elif negativo>positivo:
                    contador_mensaje_negativo+=1
                else:
                    contador_mensaje_neutro+=1
            respuesta+="Mensajes Con Sentimientos Positivos: "+str(contador_mensaje_positivo)+"\n"
            respuesta+="Mensajes Con Sentimientos Negativos: "+str(contador_mensaje_negativo)+"\n"
            respuesta+="Mensajes Con Sentimientos Neutros: "+str(contador_mensaje_neutro)+"\n"
            respuesta+="\n"
            contador_mensaje_positivo=0
            contador_mensaje_negativo=0
            contador_mensaje_neutro=0
        return respuesta

    def grafica_sentimiento_mensaje(self, lista_mensaje_fecha):
        if len(lista_mensaje_fecha)==0:
            return "No Existen Archivos De Mensajes Procesados."
        if len(self.lista_sentimiento_negativo)==0 or len(self.lista_sentimiento_positivo)==0:
            return "No Existen Archivos De Sentimientos Procesados."
        contador_mensaje_positivo=0
        contador_mensaje_negativo=0
        contador_mensaje_neutro=0
        nombre_archivo = "Grafica_Sentimiento_Mensaje"
        f = open(nombre_archivo+'.dot','w')
        texto_g = """
            graph "" {bgcolor="#f2f2f2" gradientangle=90 label="Grafica Sentimiento Mensaje"
                fontname="Helvetica,Arial,sans-serif"
                node [fontname="Helvetica,Arial,sans-serif"]
                edge [fontname="Helvetica,Arial,sans-serif"]"""
        contador_nodo=1
        contador_subgrafo=1
        for fecha in lista_mensaje_fecha:
            fecha_mensaje="Fecha: "+fecha.fecha
            texto_g+= """subgraph cluster0"""+str(contador_subgrafo)+"""{label="""+f'"'+fecha_mensaje+f'"'+""" style="filled" gradientangle="270"\n"""
            contador_actual=contador_nodo
            contador_nodo+=1
            texto_g += """n00"""+str(contador_actual)+"""[fillcolor="#d43440", style=filled, shape=doublecircle, label="""+f'"'+fecha.fecha+f'"'+"""];\n"""
            for mensaje in fecha.lista_mensaje:
                positivo, negativo = contar_sentimientos(mensaje.texto_mensaje, self.lista_sentimiento_positivo, self.lista_sentimiento_negativo)
                if positivo>negativo:
                    contador_mensaje_positivo+=1
                elif negativo>positivo:
                    contador_mensaje_negativo+=1
                else:
                    contador_mensaje_neutro+=1
            texto_g += """n00"""+str(contador_nodo)+""" [fillcolor="#65babf", style=filled, shape=circle, label="""+f'"'+f"Mensajes Con Sentimientos Positivos: "+str(contador_mensaje_positivo)+f'"'+"""];\n"""
            texto_g += """n00"""+str(contador_actual)+ """--"""+ """n00"""+str(contador_nodo)+""" ;\n"""
            contador_nodo+=1
            texto_g += """n00"""+str(contador_nodo)+""" [fillcolor="#65babf", style=filled, shape=circle, label="""+f'"'+f"Mensajes Con Sentimientos Negativos: "+str(contador_mensaje_negativo)+f'"'+"""];\n"""
            texto_g += """n00"""+str(contador_actual)+ """--"""+ """n00"""+str(contador_nodo)+""" ;\n"""
            contador_nodo+=1
            texto_g += """n00"""+str(contador_nodo)+""" [fillcolor="#65babf", style=filled, shape=circle, label="""+f'"'+f"Mensajes Con Sentimientos Neutros: "+str(contador_mensaje_neutro)+f'"'+"""];\n"""
            texto_g += """n00"""+str(contador_actual)+ """--"""+ """n00"""+str(contador_nodo)+""" ;\n"""
            texto_g += """\n}\n"""
            contador_subgrafo+=1
            contador_nodo+=1
        texto_g += """\n}"""
        f.write(texto_g)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system(f'dot -Tpdf {nombre_archivo}.dot -o {nombre_archivo}.pdf')
        return "Grafica Sentimiento Mensaje Generada Correctamente"
