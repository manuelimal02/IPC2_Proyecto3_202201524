from Mensaje.Mensaje import Mensaje
class MensajeDAO:
    def __init__(self):
        self.lista_mensaje=[]
    
    def nuevo_mensaje(self, fecha, usuario, hasthag, mensaje):
        nuevo_mensaje = Mensaje(fecha, usuario, hasthag, mensaje)
        self.lista_mensaje.append(nuevo_mensaje)
        return True
    
    def imprimir_mensaje(self):
        print("------------------------")
        for mensaje in self.lista_mensaje:
            print("--")
            print(mensaje.fecha)
            print(mensaje.usuario)
            print(mensaje.hashtag)
            print(mensaje.mensaje)
        print("------------------------")
