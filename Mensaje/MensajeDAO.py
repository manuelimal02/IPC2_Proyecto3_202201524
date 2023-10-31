from Mensaje.Fecha_Mensaje import Fecha_Mensaje
from Mensaje.Contenido_Mensaje import Contenido_Mensaje
import os

def contador_variable(lista):
    # Crea un diccionario vacío para realizar el seguimiento de las cuentas de hashtag
    contador = {}
    # Recorre la lista de hashtags
    for variable in lista:
        # Si el hashtag ya está en el diccionario, incrementa su cuenta en 1
        if variable in contador:
            contador[variable] += 1
        else:
            # Si el hashtag no está en el diccionario, agrégalo con una cuenta de 1
            contador[variable] = 1
    return contador

class MensajeDAO:
    def __init__(self):
        self.lista_mensaje_fecha=[]
    
    def nuevo_mensaje(self, fecha, usuario, hasthag, texto_mensaje):
        for fecha_mensaje in self.lista_mensaje_fecha:
            if fecha_mensaje.fecha==fecha:
                fecha_mensaje.lista_mensaje.append(Contenido_Mensaje(usuario, hasthag, texto_mensaje))
                return True
        lista_mensaje=[]
        lista_mensaje.append(Contenido_Mensaje(usuario, hasthag, texto_mensaje))
        nuevo_mensaje=Fecha_Mensaje(fecha, lista_mensaje)
        self.lista_mensaje_fecha.append(nuevo_mensaje)
        return True
    
    def imprimir_mensaje(self):
        print("------------------------")
        for fecha in self.lista_mensaje_fecha:
            print("---",fecha.fecha,"---")
            for mensaje in fecha.lista_mensaje:
                print(mensaje.usuario)
                print(mensaje.hashtag)
                print(mensaje.texto_mensaje)
        print("------------------------")
    
    def resetear_datos_mensaje(self):
        self.lista_mensaje_fecha.clear()
    
    def consultar_hashtag(self):
        if len(self.lista_mensaje_fecha)==0:
            return "No Existen Archivos De Mensaje Procesados."
        lista_hashtag=[]
        respuesta=""
        for fecha in self.lista_mensaje_fecha:
            respuesta+="Fecha: "+fecha.fecha+"\n"
            for mensaje in fecha.lista_mensaje:
                for hashtag in mensaje.hashtag:
                    lista_hashtag.append(hashtag)
            consultar_hashtag=contador_variable(lista_hashtag)
            for hashtag, contador in consultar_hashtag.items():
                respuesta+=f"#{hashtag}#: {contador} mensajes."+"\n"
            lista_hashtag.clear()
            respuesta+="\n"
        return respuesta
    
    def grafica_consular_hashtag(self):
        if len(self.lista_mensaje_fecha)==0:
            return "No Existen Archivos De Mensaje Procesados."
        lista_hashtag=[]
        nombre_archivo = "Grafica_Hasthtag"
        f = open(nombre_archivo+'.dot','w')
        texto_g = """
            graph "" {bgcolor="#f2f2f2" gradientangle=90 label="Grafica Hashtag"
                fontname="Helvetica,Arial,sans-serif"
                node [fontname="Helvetica,Arial,sans-serif"]
                edge [fontname="Helvetica,Arial,sans-serif"]"""
        contador_nodo=1
        contador_subgrafo=1
        for fecha in self.lista_mensaje_fecha:
            fecha_mensaje="Fecha: "+fecha.fecha
            texto_g+= """subgraph cluster0"""+str(contador_subgrafo)+"""{label="""+f'"'+fecha_mensaje+f'"'+""" style="filled" gradientangle="270"\n"""
            contador_actual=contador_nodo
            contador_nodo+=1
            texto_g += """n00"""+str(contador_actual)+"""[fillcolor="#d43440", style=filled, shape=doublecircle, label="""+f'"'+fecha.fecha+f'"'+"""];\n"""
            for mensaje in fecha.lista_mensaje:
                for hashtag in mensaje.hashtag:
                    lista_hashtag.append(hashtag)
            consultar_hashtag=contador_variable(lista_hashtag)
            for hashtag, cuenta in consultar_hashtag.items():
                texto_g += """n00"""+str(contador_nodo)+""" [fillcolor="#65babf", style=filled, shape=circle, label="""+f'"'+f"#{hashtag}#: {cuenta} mensajes."+f'"'+"""];\n"""
                texto_g += """n00"""+str(contador_actual)+ """--"""+ """n00"""+str(contador_nodo)+""" ;\n"""
                contador_nodo+=1
            lista_hashtag.clear()
            texto_g += """\n}\n"""
            contador_subgrafo+=1
            contador_nodo+=1
        texto_g += """\n}"""
        f.write(texto_g)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system(f'dot -Tpdf {nombre_archivo}.dot -o {nombre_archivo}.pdf')
        return "Grafica Hashtag Generada Correctamente"

    def consultar_menciones(self):
        if len(self.lista_mensaje_fecha)==0:
            return "No Existen Archivos De Mensaje Procesados."
        lista_usuario=[]
        respuesta=""
        for fecha in self.lista_mensaje_fecha:
            respuesta+="Fecha: "+fecha.fecha+"\n"
            for mensaje in fecha.lista_mensaje:
                for usuario in mensaje.usuario:
                    lista_usuario.append(usuario)
            consultar_menciones=contador_variable(lista_usuario)
            for usuario, cuenta in consultar_menciones.items():
                respuesta+=f"@{usuario}: {cuenta} mensajes."+"\n"
            lista_usuario.clear()
            respuesta+="\n"
        return respuesta

    def grafica_consular_menciones(self):
        if len(self.lista_mensaje_fecha)==0:
            return "No Existen Archivos De Mensaje Procesados."
        lista_usuario=[]
        nombre_archivo = "Grafica_Menciones"
        f = open(nombre_archivo+'.dot','w')
        texto_g = """
            graph "" {bgcolor="#f2f2f2" gradientangle=90 label="Grafica Menciones"
                fontname="Helvetica,Arial,sans-serif"
                node [fontname="Helvetica,Arial,sans-serif"]
                edge [fontname="Helvetica,Arial,sans-serif"]"""
        contador_nodo=1
        contador_subgrafo=1
        for fecha in self.lista_mensaje_fecha:
            fecha_mensaje="Fecha: "+fecha.fecha
            texto_g+= """subgraph cluster0"""+str(contador_subgrafo)+"""{label="""+f'"'+fecha_mensaje+f'"'+""" style="filled" gradientangle="270"\n"""
            contador_actual=contador_nodo
            contador_nodo+=1
            texto_g += """n00"""+str(contador_actual)+"""[fillcolor="#d43440", style=filled, shape=doublecircle, label="""+f'"'+fecha.fecha+f'"'+"""];\n"""
            for mensaje in fecha.lista_mensaje:
                for usuario in mensaje.usuario:
                    lista_usuario.append(usuario)
            consultar_menciones=contador_variable(lista_usuario)
            for usuario, cuenta in consultar_menciones.items():
                texto_g += """n00"""+str(contador_nodo)+""" [fillcolor="#65babf", style=filled, shape=circle, label="""+f'"'+f"@{usuario}: {cuenta} mensajes."+f'"'+"""];\n"""
                texto_g += """n00"""+str(contador_actual)+ """--"""+ """n00"""+str(contador_nodo)+""" ;\n"""
                contador_nodo+=1
            lista_usuario.clear()
            texto_g += """\n}\n"""
            contador_subgrafo+=1
            contador_nodo+=1
        texto_g += """\n}"""
        f.write(texto_g)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system(f'dot -Tpdf {nombre_archivo}.dot -o {nombre_archivo}.pdf')
        return "Grafica Menciones Generada Correctamente"