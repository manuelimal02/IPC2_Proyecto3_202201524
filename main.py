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

@app.route('/grabarMensajes', methods=['POST'])
def cargar_archivo_mensajes():
    if 'file' not in request.files:
        return jsonify({"message": "Error archivo mensaje: Error al cargar el archivo de mensajes."})
    archivo = request.files['file']
    contenido_xml=archivo.read().decode('utf-8')
    root = ET.fromstring(contenido_xml)
    for mensaje in root.findall(".//MENSAJE"):
        fecha = mensaje.find("FECHA").text
        texto = mensaje.find("TEXTO").text
        hashtag = encontrar_hashtag(texto)
        usuario = encontrar_usuario(texto)
        manejador_mensaje.nuevo_mensaje(fecha, usuario, hashtag, texto)
    manejador_mensaje.base_datos_mensaje()
    return jsonify({"message": "Archivo Mensaje: Archivo de mensajes cargado correctamente."})

@app.route('/grabarConfiguracion', methods=['POST'])
def cargar_archivo_configuracion():
    if 'file' not in request.files:
        return jsonify({"message": "Error archivo configuraciones: Error al cargar el archivo de configuraciones."})
    archivo = request.files['file']
    contenido_xml=archivo.read().decode('utf-8')
    root = ET.fromstring(contenido_xml)
    for sentimiento in root.findall(".//sentimientos_positivos/palabra"):
        manejador_sentimiento.nuevo_sentimiento_positivo(sentimiento.text.strip())
    for sentimiento in root.findall(".//sentimientos_negativos/palabra"):
        manejador_sentimiento.nuevo_sentimiento_negativo(sentimiento.text.strip())
    manejador_sentimiento.base_datos_configuracion()
    return jsonify({"message": "Archivo de configuraciones cargado correctamente."})

@app.route('/consulta/consultarHashtag', methods=['GET'])
def consultar_hashtag():
    respuesta=manejador_mensaje.consultar_hashtag()
    return jsonify({"message": f"{respuesta}"})

@app.route('/consulta/consultarMenciones', methods=['GET'])
def consultar_menciones():
    respuesta=manejador_mensaje.consultar_menciones()
    return jsonify({"message": f"{respuesta}"})

@app.route('/consulta/consultarSentimiento', methods=['GET'])
def consultar_sentimiento_mensaje():
    respuesta=manejador_sentimiento.consultar_sentimiento_mensaje(manejador_mensaje.lista_mensaje_fecha)
    return jsonify({"message": f"{respuesta}"})

@app.route('/grafica/grafica-consulta-hashtag', methods=['GET'])
def grafica_consulta_hashtag():
    respuesta=manejador_mensaje.grafica_consular_hashtag()
    return jsonify({"message": f"{respuesta}"})

@app.route('/grafica/grafica-consulta-menciones', methods=['GET'])
def grafica_consulta_menciones():
    respuesta=manejador_mensaje.grafica_consular_menciones()
    return jsonify({"message": f"{respuesta}"})

@app.route('/grafica/grafica-consulta-sentimiento', methods=['GET'])
def grafica_consultar_sentimiento_mensaje():
    respuesta=manejador_sentimiento.grafica_sentimiento_mensaje(manejador_mensaje.lista_mensaje_fecha)
    return jsonify({"message": f"{respuesta}"})

@app.route('/resumen/resumen-mensajes', methods=['GET'])
def resumen_mensajes():
    respuesta=manejador_mensaje.resumen_mensaje()
    return jsonify({"message": f"{respuesta}"})

@app.route('/resumen/resumen-configuraciones', methods=['GET'])
def resumen_configuraciones():
    respuesta=manejador_sentimiento.resumen_configuracion()
    return jsonify({"message": f"{respuesta}"})

@app.route('/informacion/informacion-estudiante', methods=['GET'])
def informacion_estudiante():
    respuesta="Carlos Manuel Lima y Lima"+"\n"+"202201524"+"\n"+"IPC2 - Segundo Semestre 20223"+"\n"+"Proyecto 3"
    return jsonify({"message": f"{respuesta}"})

@app.route('/limpiarDatos', methods=['GET'])
def resetear_datos():
    #Lista_Mensajes
    manejador_mensaje.resetear_datos_mensaje()
    #Lista_Sentimiento
    manejador_sentimiento.resetear_datos_sentimiento()
    #BBDD
    manejador_mensaje.base_datos_mensaje()
    manejador_sentimiento.base_datos_configuracion()
    #Comprobacion
    manejador_mensaje.imprimir_mensaje()
    manejador_sentimiento.imprimir_sentimiento()
    return jsonify({"message": "Resetear Datos: Datos Reseteados Correctamente."})

if __name__=="__main__":
    app.run(threaded=True,port=5000,debug=True)