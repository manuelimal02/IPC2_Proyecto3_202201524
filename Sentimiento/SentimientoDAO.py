from Sentimiento.Sentimiento_Positivo import Sentimiento_Positivo
from Sentimiento.Sentimiento_Negativo import Sentimiento_Negativo

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