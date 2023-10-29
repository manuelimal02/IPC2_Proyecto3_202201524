import xml.etree.ElementTree as ET
from flask import Flask,jsonify,request
from flask_cors import CORS
from Mensaje.MensajeDAO import MensajeDAO
from Sentimiento.SentimientoDAO import SentimientoDAO
import re

manejador_mensaje=MensajeDAO()
manejador_sentimiento=SentimientoDAO()

app= Flask(__name__)
CORS(app)

def encontrar_hashtag(cadena):
    hashtag = re.findall(r'#(.*?)#', cadena)
    return hashtag

def encontrar_usuario(cadena):
    usuario = re.findall(r'@(\w+)', cadena)
    return usuario

@app.route("/")
def index():
    return "<h1>Prueba Proyecto 3</h1>"

@app.route('/grabarMensajes',methods=['POST'])
def cargar_archivo_mensajes():
    if 'archivo_xml_mensajes' not in request.files:
        return jsonify({"Mensajes": "No se ha enviado un archivo."})
    archivo = request.files['archivo_xml_mensajes']
    contenido_xml=archivo.read().decode('utf-8')
    root = ET.fromstring(contenido_xml)
    for mensaje in root.findall(".//MENSAJE"):
        fecha = mensaje.find("FECHA").text
        texto = mensaje.find("TEXTO").text
        hashtag = encontrar_hashtag(texto)
        usuario = encontrar_usuario(texto)
        manejador_mensaje.nuevo_mensaje(fecha, usuario, hashtag, texto)
    manejador_mensaje.imprimir_mensaje()
    return jsonify({"Mensaje": "Archivo Mensajes Leído."})  

@app.route('/grabarConfiguracion', methods=['POST'])
def cargar_archivo_configuracion():
    if 'archivo_xml_configuracion' not in request.files:
        return jsonify({"Configuraciones": "No se ha enviado un archivo."})
    archivo = request.files['archivo_xml_configuracion']
    contenido_xml=archivo.read().decode('utf-8')
    root = ET.fromstring(contenido_xml)
    for sentimiento in root.findall(".//sentimientos_positivos/palabra"):
        manejador_sentimiento.nuevo_sentimiento_positivo(sentimiento.text.strip())
    for sentimiento in root.findall(".//sentimientos_negativos/palabra"):
        manejador_sentimiento.nuevo_sentimiento_negativo(sentimiento.text.strip())
    manejador_sentimiento.imprimir_sentimiento()
    return jsonify({"Configuraciones": "Archivo Configuraciones Leído."})

@app.route('/limpiarDatos', methods=['POST'])
def resetear_datos():
    #Lista_Mensajes
    manejador_mensaje.lista_mensaje.clear()
    #Lista_Sentimiento
    manejador_sentimiento.lista_sentimiento_positivo.clear()
    manejador_sentimiento.lista_sentimiento_positivo_rechazado.clear()
    manejador_sentimiento.lista_sentimiento_negativo.clear()
    manejador_sentimiento.lista_sentimiento_negativo_rechazado.clear()
    manejador_mensaje.imprimir_mensaje()
    manejador_sentimiento.imprimir_sentimiento()
    return jsonify({"Resetar Datos": "Datos Reseteados Correctamente"})

if __name__=="__main__":
    app.run(threaded=True,port=5000,debug=True)