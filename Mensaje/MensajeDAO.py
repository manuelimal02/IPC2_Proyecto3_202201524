from Mensaje.Fecha_Mensaje import Fecha_Mensaje
from Mensaje.Contenido_Mensaje import Contenido_Mensaje
import xml.etree.ElementTree as ET
import os

def contador_variable(lista):
    contador = {}
    for variable in lista:
        if variable in contador:
            contador[variable] += 1
        else:
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
            return "Consulta Hashtag: No existen archivos de mensaje procesados."
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
            return "Gráfica Hashtag: No existen archivos de mensaje procesados."
        lista_hashtag=[]
        nombre_archivo = "Graficas/Grafica_Hasthtag"
        f = open(nombre_archivo+'.dot','w')
        texto_g = """
            graph "" {bgcolor="#f2f2f2" gradientangle=90 label="Grafica Hashtag - 202201524 - Carlos Manuel Lima y Lima"
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
            texto_g += """n00"""+str(contador_actual)+"""[fillcolor="#d43440", style=filled, shape=component, label="""+f'"'+fecha.fecha+f'"'+"""];\n"""
            for mensaje in fecha.lista_mensaje:
                for hashtag in mensaje.hashtag:
                    lista_hashtag.append(hashtag)
            consultar_hashtag=contador_variable(lista_hashtag)
            for hashtag, cuenta in consultar_hashtag.items():
                texto_g += """n00"""+str(contador_nodo)+""" [fillcolor="#65babf", style=filled, shape=rectangle, label="""+f'"'+f"#{hashtag}#: {cuenta} mensajes."+f'"'+"""];\n"""
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
        return "Gráfica Hashtag Generada Correctamente."

    def consultar_menciones(self):
        if len(self.lista_mensaje_fecha)==0:
            return "Consulta Menciones: No existen archivos de mensaje procesados."
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
            return "Gráfica Menciones: No existen archivos de mensaje procesados."
        lista_usuario=[]
        nombre_archivo = "Graficas/Grafica_Menciones"
        f = open(nombre_archivo+'.dot','w')
        texto_g = """
            graph "" {bgcolor="#f2f2f2" gradientangle=90 label="Grafica Menciones - 202201524 - Carlos Manuel Lima y Lima"
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
            texto_g += """n00"""+str(contador_actual)+"""[fillcolor="#d43440", style=filled, shape=component, label="""+f'"'+fecha.fecha+f'"'+"""];\n"""
            for mensaje in fecha.lista_mensaje:
                for usuario in mensaje.usuario:
                    lista_usuario.append(usuario)
            consultar_menciones=contador_variable(lista_usuario)
            for usuario, cuenta in consultar_menciones.items():
                texto_g += """n00"""+str(contador_nodo)+""" [fillcolor="#65babf", style=filled, shape=rectangle, label="""+f'"'+f"@{usuario}: {cuenta} mensajes."+f'"'+"""];\n"""
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
        return "Gráfica Menciones Generada Correctamente."
    
    def base_datos_mensaje(self):
        mensajes_generales = ET.Element("Base-Datos-Mensaje")
        for fecha in self.lista_mensaje_fecha:
            mensaje = ET.SubElement(mensajes_generales, "Mensaje")
            fecha_ms = ET.SubElement(mensaje, "Fecha")
            fecha_ms.text = fecha.fecha
            for mensaje_fecha in fecha.lista_mensaje:
                texto_ms = ET.SubElement(mensaje, "Texto")
                texto_ms.text = mensaje_fecha.texto_mensaje
        datos=ET.tostring(mensajes_generales)
        datos=str(datos)
        self.xml_identado(mensajes_generales)
        arbol_xml=ET.ElementTree(mensajes_generales)
        arbol_xml.write("BBDD/Base-Datos-Mensaje.xml",encoding="UTF-8",xml_declaration=True)

    def resumen_mensaje(self):
        if len(self.lista_mensaje_fecha)==0:
            return "Resumen Mensaje: No existen archivos de mensaje procesados."
        mensajes_generales = ET.Element("Mensaje")
        lista_hashtag=[]
        lista_usuario=[]
        for fecha in self.lista_mensaje_fecha:
            tiempo = ET.SubElement(mensajes_generales, "Tiempo")
            fecha_ms = ET.SubElement(tiempo, "Fecha")
            fecha_ms.text = fecha.fecha
            for mensaje in fecha.lista_mensaje:
                for hashtag in mensaje.hashtag:
                    lista_hashtag.append(hashtag)
            consultar_hashtag=contador_variable(lista_hashtag)
            for mensaje in fecha.lista_mensaje:
                for usuario in mensaje.usuario:
                    lista_usuario.append(usuario)
            consultar_menciones=contador_variable(lista_usuario)
            ms_recibido = ET.SubElement(tiempo, "Mensajes-Recibios")
            ms_recibido.text = str(len(fecha.lista_mensaje))

            us_mencionado = ET.SubElement(tiempo, "Usuarios-Mencionados")
            us_mencionado.text = str(len(consultar_menciones))

            hs_mencionado = ET.SubElement(tiempo, "Hashtag-Incluidos")
            hs_mencionado.text = str(len(consultar_hashtag))

            lista_hashtag.clear()
            lista_usuario.clear()
        datos=ET.tostring(mensajes_generales)
        datos=str(datos)
        self.xml_identado(mensajes_generales)
        arbol_xml=ET.ElementTree(mensajes_generales)
        arbol_xml.write("Resumen/resumenMensajes.xml",encoding="UTF-8",xml_declaration=True)
        return "Archivo Resumen Mensajes Generado Correctamente."

    def xml_identado(self, element, indent='  '):
        queue = [(0, element)]
        while queue:
            level, element = queue.pop(0)
            children = [(level + 1, child) for child in list(element)]
            if children:
                element.text = '\n' + indent * (level + 1)
            if queue:
                element.tail = '\n' + indent * queue[0][0]
            else:
                element.tail = '\n' + indent * (level - 1)
            queue[0:0] = children