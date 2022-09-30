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
        # self._ganador1 = False
        # self._ganador2 = False
        # self._empate = False
      
        
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
    
            
#----------- Clase Juego de _guerra --------------       
class Juego_guerra:
        
        def __init__ (self,semilla):
            random.seed(semilla)
            self._jugador1 = ListaDobleEnlazada()
            self._jugador2 = ListaDobleEnlazada()
            self._guerra = False
            self._turnos_jugados = 0
            #self._ganador = None
            #self._empate = False
            
        @property
        def turnos_jugados(self):
            return self._turnos_jugados
        
        @property
        def ganador(self):
            self._ganador = ' '
            return self._ganador 
        
        @property
        def empate(self):
            self._empate = False
            return self._empate 
        
            
        def terminar(self):
          #COMO PODRIA SER PARA LA GUERRA  
            if self._guerra == True:
                if self._jugador1.tamanio < 4: 
                    self._ganador = 'jugador 1'
                    print("***** jugador 1 gana la partida *****")
                elif self._jugador2.tamanio < 4:
                    self._ganador = 'jugador 2'
                    print("***** jugador 2 gana la partida *****")
                    
            elif self._jugador1.tamanio == 0:
                    self._ganador = 'jugador 2'
                    print("***** jugador 2 gana la partida *****")
            else:
                self._ganador = 'jugador 1'
                print("***** jugador 1 gana la partida *****")
            
        
        # repartimos el mazo en las dos barajas para cada jugador
        def repartir_cartas(self, mazo):                            #MODIFICADO
            # repartimos las cartas a cada jugador
            while mazo.cartas.tamanio > 0:
                self._jugador1.anexar(mazo.cartas.extraer().dato)
                self._jugador2.anexar(mazo.cartas.extraer().dato)
         

        
        # FUNCION inicio del juego
        def iniciar_juego(self):
            mazo = Mazo() #creamos mazo
            mazo.Mezclar() #mezclamos mazo
            self.repartir_cartas(mazo) 
             
            # iniciamos TURNOS de combate
            # while self._jugador1.tamanio > 0 or self._jugador2.tamanio > 0:
            
            while self.turnos_jugados < 10000 and self.empate == False:
                
                # while self.__jugador1 or self._jugador2 or self._empate:    
                self._turnos_jugados += 1 #contador de turnos
                
                
                contador = 1
                # extraemos las cartas de arriba de cada jugador
                cartas_en_mesa = ListaDobleEnlazada()
                if self._jugador1.tamanio == 0 or self._jugador2.tamanio == 0:#MODIFICADO
                    self.terminar()
                    return
                else:
                    carta1 = self._jugador1.extraer().dato
                    carta2 = self._jugador2.extraer().dato
                    carta1.boca_abajo = False
                    carta2.boca_abajo = False
                    cartas_en_mesa.anexar(carta1)
                    cartas_en_mesa.anexar(carta2)
                    if carta1.valor == carta2.valor:
                        self._guerra = True    
                
                while self._guerra == True and self._jugador1.tamanio > 0:
                    for n in range(1,4): #si hay _guerra sacamos 3 cartas boca abajo
                        if self._jugador1.tamanio < 4 or self._jugador2.tamanio < 4:
                            self.terminar()
                            return
                        carta1 = self._jugador1.extraer().dato
                        carta2 = self._jugador2.extraer().dato
                        cartas_en_mesa.anexar(carta1)
                        cartas_en_mesa.anexar(carta2)
                    #y sacamos una carta boca arriba
                    carta1 = self._jugador1.extraer().dato
                    carta2 = self._jugador2.extraer().dato
                    carta1.boca_abajo = False
                    carta2.boca_abajo = False
                    cartas_en_mesa.anexar(carta1)
                    cartas_en_mesa.anexar(carta2)
                    if carta1.valor != carta2.valor:
                        self._guerra = False

                    # print('cartas mesa: ' + str(cartas_en_mesa))
                
                
#---------------------------------MOSTRAR TABLERO----------------------------------------
                print("-------------------------------------------------") #esto es una barra separadora
                print("Turno: " + str(self.turnos_jugados))
                print("Jugador 1: ")
                fin = ''
                for carta in self._jugador1:
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
                for carta in self._jugador2:
                    carta.dato.boca_abajo = True
                    if contador%10 == 0:
                        fin = '\n'
                    else:
                        fin = ''
                    
                    print(" "+carta.dato.poner_boca_abajo(), end=fin)
                    contador += 1
                print("\n")
                print("-------------------------------------------------")
                 
#-------------------------Asignacion de cartas al _ganador------------------------
                if carta1.valor == 'A' or carta2.valor == 'A':
                    if carta1.valor == 'A':
                        self._jugador1 + cartas_en_mesa
                        # print('Condicion 1 - carta 1 es mayor')
                    if carta2.valor == 'A':
                        self._jugador2 + cartas_en_mesa
                        # print('Condicion 2 - carta 2 es mayor')
                elif carta1.valor != 'A' and carta2.valor != 'A':
                    if carta1.valor > carta2.valor:
                        self._jugador1 + cartas_en_mesa
                        # print('Condicion 3 - carta 1 es mayor')
                    if carta1.valor < carta2.valor:
                        self._jugador2 + cartas_en_mesa
                        # print('Condicion 4 - carta 2 es mayor')
                
                for carta in self._jugador1:
                    carta.dato.boca_abajo = True
                    carta.dato.boca_arriba = False
                
                for carta in self._jugador2:
                    carta.dato.boca_abajo = True
                    carta.dato.boca_arriba = False
                
                # if carta1.valor == carta.valor
                                
                cartas_en_mesa = ListaDobleEnlazada() #reseteamos las cartas en mesa
               
                print("Cartas jugador 1: ")
                print(self._jugador1)
                print("Tamaño jugador 1: " + str(self._jugador1.tamanio))
                print("Cartas jugador 2: ")
                print(self._jugador2)
                print("Tamaño jugador 2: " + str(self._jugador2.tamanio))
                # print("Tamaño de cartas en mesa:" + str(cartas_en_mesa.tamanio))
                                    
            # print(self._jugador1)
            # print('')
                
            # print('')
            # print(self._jugador1.tamanio) 
            # print(self._jugador2.tamanio)
            
            if self._turnos_jugados == 10000: #MODIFICADO
                    self.empate = True
                    print("***** Empate *****")
# ##########################################################################################
# ##########################################################################################

# #PRUEBAS
if __name__ == "__main__":
    
               
    m = Juego_guerra(314) # el 17 fuerza la _guerra
    m.iniciar_juego()
    
        

