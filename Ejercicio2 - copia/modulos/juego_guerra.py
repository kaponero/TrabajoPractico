# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 18:03:38 2022

@author: kapon
"""

from LDE import ListaDobleEnlazada
import random

valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
# valores = ['2','2','2','2','2','2','2','5','5','5','5','5','5']
palos = ['♠', '♥', '♦', '♣']
boca_arriba = False
boca_abajo = False


#----------- Clase CARTA ------------
class Carta:
    
    def __init__ (self,val,pal):
        self.valor = val
        self.palo = pal
        self.boca_abajo = True
        
    def mostrar_carta(self):
      print(self.valor + self.palo)
    
    def poner_boca_arriba(self):
        cadena=self.valor + self.palo
        return cadena
            
    def poner_boca_abajo(self):
        return "-X"
        
    def __str__(self):
        cadena=self.valor + self.palo
        return cadena
#----------- Clase MAZO ------------

class Mazo:
    def __init__(self):
        self.cartas = ListaDobleEnlazada()
        self.ganador1 = False
        self.ganador2 = False
        self.empate = False
      
        
    def Mezclar(self):
        cartas_ordenadas = []
        for valor in valores:
            for palo in palos:
                carta=Carta(valor,palo)
                cartas_ordenadas.append(carta)
        random.shuffle(cartas_ordenadas)
        for carta in cartas_ordenadas:
            self.cartas.anexar(carta)
 
        def __str__(self):
           return str(self.cartas)
    
            
#----------- Clase Juego de Guerra --------------       
class JuegoGuerra:
        
        def __init__ (self,semilla):
            random.seed(semilla)
            self.turnos_jugados = 0
            self.empate = False
            self.jugador1 = ListaDobleEnlazada()
            self.jugador2 = ListaDobleEnlazada()
            self.guerra = False
            
        def terminar(self):
            if self.jugador1.tamanio > 40:
                print("***** jugador 1 gana la partida *****")
            else:
                print("***** jugador 2 gana la partida *****")
            if self.empate:
                print("***** empate *****")
        
        # repartimos el mazo en las dos barajas para cada jugador
        def repartir_cartas(self, mazo):
            # repartimos las cartas a cada jugador
            while mazo.cartas.tamanio > 2:
                self.jugador1.anexar(mazo.cartas.extraer().dato)
                self.jugador2.anexar(mazo.cartas.extraer().dato)
            # aca hay un error con la ultima carta y por eso lo hacemos aparte
            self.jugador1.anexar(mazo.cartas.extraer().dato)
            # print(mazo.cartas.tamanio)
            self.jugador2 + mazo.cartas

        
        # FUNCION inicio del juego
        def iniciar_juego(self):
            mazo = Mazo() #creamos mazo
            mazo.Mezclar() #mezclamos mazo
            self.repartir_cartas(mazo) 
             
            # iniciamos TURNOS de combate
            # while self.jugador1.tamanio > 0 or self.jugador2.tamanio > 0:
            
            while self.turnos_jugados < 100 and self.empate == False:
                
                # while self.jugador1 or self.jugador2 or self.empate:    
                self.turnos_jugados += 1 #contador de turnos
                
                
                contador = 1
                # extraemos las cartas de arriba de cada jugador
                cartas_en_mesa = ListaDobleEnlazada()
                if self.jugador1.tamanio == 1 or self.jugador2.tamanio == 1:
                    self.terminar()
                    return
                else:
                    carta1 = self.jugador1.extraer().dato
                    carta2 = self.jugador2.extraer().dato
                    carta1.boca_abajo = False
                    carta2.boca_abajo = False
                    cartas_en_mesa.anexar(carta1)
                    cartas_en_mesa.anexar(carta2)
                    if carta1.valor == carta2.valor:
                        self.guerra = True    
                
                while self.guerra == True and self.jugador1.tamanio > 0:
                    for n in range(1,4): #si hay guerra sacamos 3 cartas boca abajo
                        if self.jugador1.tamanio < 2 or self.jugador2.tamanio < 2:
                            self.terminar()
                            return
                        carta1 = self.jugador1.extraer().dato
                        carta2 = self.jugador2.extraer().dato
                        cartas_en_mesa.anexar(carta1)
                        cartas_en_mesa.anexar(carta2)
                    #y sacamos una carta boca arriba
                    carta1 = self.jugador1.extraer().dato
                    carta2 = self.jugador2.extraer().dato
                    carta1.boca_abajo = False
                    carta2.boca_abajo = False
                    cartas_en_mesa.anexar(carta1)
                    cartas_en_mesa.anexar(carta2)
                    if carta1.valor != carta2.valor:
                        self.guerra = False

                    # print('cartas mesa: ' + str(cartas_en_mesa))
                
                
#---------------------------------MOSTRAR TABLERO----------------------------------------
                print("-------------------------------------------------") #esto es una barra separadora
                print("Turno: " + str(self.turnos_jugados))
                print("Jugador 1: ")
                fin = ''
                for carta in self.jugador1:
                    carta.dato.boca_abajo = True
                    if contador%10 == 0: # logica para mostrar las cartas boca abajo en filas de a 10
                        fin = '\n'
                    else:
                        fin = ''
                    if (carta.dato.boca_abajo):
                        print(" "+carta.dato.poner_boca_abajo(), end=fin)
                    contador += 1
    
                print("\n")
                print("         ",end="")
                posicion = 1
                for carta in cartas_en_mesa:
                    if  not carta.dato.boca_abajo:
                        print(carta.dato.poner_boca_arriba() + " ", end="")
                    else:
                        print(carta.dato.poner_boca_abajo() + " ", end="")
                    posicion += 1
                     
                print("\n")
                print("Jugador 2: ")
                # print("\n" + "Jugador 2: ")
                fin = ''
                contador = 1
                for carta in self.jugador2:
                    carta.dato.boca_abajo = True
                    if contador%10 == 0:
                        fin = '\n'
                    else:
                        fin = ''
                    
                    print(" "+carta.dato.poner_boca_abajo(), end=fin)
                    contador += 1
                print("\n")
                print("-------------------------------------------------")
                 
#-------------------------Asignacion de cartas al ganador------------------------
                if carta1.valor == 'A' or carta2.valor == 'A':
                    if carta1.valor == 'A':
                        self.jugador1 + cartas_en_mesa
                        # print('Condicion 1 - carta 1 es mayor')
                    if carta2.valor == 'A':
                        self.jugador2 + cartas_en_mesa
                        # print('Condicion 2 - carta 2 es mayor')
                elif carta1.valor != 'A' and carta2.valor != 'A':
                    if carta1.valor > carta2.valor:
                        self.jugador1 + cartas_en_mesa
                        # print('Condicion 3 - carta 1 es mayor')
                    if carta1.valor < carta2.valor:
                        self.jugador2 + cartas_en_mesa
                        # print('Condicion 4 - carta 2 es mayor')
                
                for carta in self.jugador1:
                    carta.dato.boca_abajo = True
                    carta.dato.boca_arriba = False
                
                for carta in self.jugador2:
                    carta.dato.boca_abajo = True
                    carta.dato.boca_arriba = False
                
                # if carta1.valor == carta.valor
                                
                cartas_en_mesa = ListaDobleEnlazada() #reseteamos las cartas en mesa
                print("Cartas jugador 1: ")
                print(self.jugador1)
                print("Tamaño jugador 1: " + str(self.jugador1.tamanio))
                print("Cartas jugador 2: ")
                print(self.jugador2)
                print("Tamaño jugador 2: " + str(self.jugador2.tamanio))
                # print("Tamaño de cartas en mesa:" + str(cartas_en_mesa.tamanio))
                                    
            # print(self.jugador1)
            # print('')
                
            # print('')
            # print(self.jugador1.tamanio) 
            # print(self.jugador2.tamanio)
            
                if self.empate:
                    print()
##########################################################################################
##########################################################################################

# #PRUEBAS
if __name__ == "__main__":
    
               
    m = JuegoGuerra(1) # el 17 fuerza la guerra
    m.iniciar_juego()
    
        
