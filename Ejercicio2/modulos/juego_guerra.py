# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 18:03:38 2022

@author:    Gabriela González
            Maximiliano Pérez Albarracín
            Alvaro Labanca
"""

from LDE import ListaDobleEnlazada
import random

valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
palos = ['♠', '♥', '♦', '♣']
num = {'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'10':9,'J':10,'Q':11,'K':12,'A':13 }

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
        self._cartas = ListaDobleEnlazada()     
        
    def Mezclar(self):
        cartas_ordenadas = []
        for valor in valores:
            for palo in palos:
                carta=Carta(valor,palo)
                cartas_ordenadas.append(carta)
        random.shuffle(cartas_ordenadas)
        for carta in cartas_ordenadas:
            self._cartas.anexar(carta)
        # print("Mazo mesclado: ")
        # print(self._cartas)
        # print("")
        
    @property
    def cartas(self):
        return self._cartas
    
    def __str__(self):
       return str(self._cartas)
    
            
#----------- Clase Juego de _guerra --------------       
class JuegoGuerra:
        
    def __init__ (self,random_seed):
        self._semilla = random_seed
        self._jugador1 = ListaDobleEnlazada()
        self._jugador2 = ListaDobleEnlazada()
        self._cartas_en_mesa = ListaDobleEnlazada()
        self._guerra = False
        self._turnos_jugados = 0
        self._ganador = None
        self._empate = False
        self._sin_cartas = False
        
    @property
    def turnos_jugados(self):
        return self._turnos_jugados
        
    @property
    def ganador(self):
        return self._ganador 
    
    @property
    def empate(self):
        return self._empate 
        
    
    # repartimos el mazo en las dos barajas para cada jugador
    def repartir_cartas(self, mazo):                            #MODIFICADO
        # repartimos las cartas a cada jugador
        while mazo.cartas.tamanio > 0:
            self._jugador2.anexar(mazo.cartas.extraer(0).dato)
            self._jugador1.anexar(mazo.cartas.extraer(0).dato)
    
    
###############################################################################
#
#                               pantalla
#
###############################################################################

    def mostrar_pantalla(self):
        print("-------------------------------------------------") #esto es una barra separadora
        if self._cartas_en_mesa.tamanio>3:
            print("                ",end="")
            print("**** Guerra!! ****")
        
        print("Turno: " + str(self.turnos_jugados))
        
        #-------------------cartas jugador 1-----------------------------------
        print("Jugador 1: ")
        fin = ''
        contador=1
        for carta in self._jugador1:
            if contador%10 == 0: # logica para mostrar las cartas boca abajo en filas de a 10
                fin = '\n'
            else:
                fin = ''
            if carta.dato.boca_abajo:
                print(" "+carta.dato.poner_boca_abajo(), end=fin)
            contador += 1
        print("")
        
        #---------------cartas jugadas-----------------------------------------
        print("")
        print("         ",end="")
        posicion = 1
        for carta in self._cartas_en_mesa:
            if  not carta.dato.boca_abajo:
                print(carta.dato.poner_boca_arriba() + " ", end="")
            else:
                print(carta.dato.poner_boca_abajo() + " ", end="")
            posicion += 1
        print("")
        
        #-------------------cartas jugador 2-----------------------------------
        print("")
        print("Jugador 2: ")
        # print("\n" + "Jugador 2: ")
        fin = ''
        contador = 1
        for carta in self._jugador2:
            if contador%10 == 0:
                fin = '\n'
            else:
                fin = ''
            if carta.dato.boca_abajo:
                print(" "+carta.dato.poner_boca_abajo(), end=fin)
            contador += 1
        print("\n")
        # print("-------------------------------------------------")
    

    # def guerra(self):
                
#------------------------metodo que inicia el juego----------------------------

    def iniciar_juego(self):
        random.seed(self._semilla)
        mazo = Mazo() #creamos mazo
        mazo.Mezclar() #mezclamos mazo
        self.repartir_cartas(mazo)

###############################################################################
#
#                            INICIO WHILE
#
###############################################################################
        while self.turnos_jugados < 10000:
            self._turnos_jugados += 1
            
            #extraemos 2 cartas y las jugamos en la mesa        
            carta1 = self._jugador1.extraer(0).dato
            carta2 = self._jugador2.extraer(0).dato
            carta1.boca_abajo = False
            carta2.boca_abajo = False
            self._cartas_en_mesa.anexar(carta1)
            self._cartas_en_mesa.anexar(carta2)
            
            # print(carta1)
            # print(carta2)
            
###############################################################################
#
#                           Guerra!!!
#
###############################################################################
            
            if carta1.valor == carta2.valor:
                self._guerra = True 
            else: 
                self._guerra = False
                             
            while self._guerra:
                if self._jugador1.tamanio>3 and self._jugador2.tamanio>3:
                    for i in range (1,4):
                            carta1 = self._jugador1.extraer(0).dato
                            carta2 = self._jugador2.extraer(0).dato
                            self._cartas_en_mesa.anexar(carta1)
                            self._cartas_en_mesa.anexar(carta2)
                    carta1 = self._jugador1.extraer(0).dato
                    carta2 = self._jugador2.extraer(0).dato
                    carta1.boca_abajo = False
                    carta2.boca_abajo = False
                    self._cartas_en_mesa.anexar(carta1)
                    self._cartas_en_mesa.anexar(carta2)
                else:
                    self._sin_cartas = True
                    break
                if carta1.valor != carta2.valor:
                    self._guerra= False
            
            if self._guerra and self._sin_cartas:
                break
            # print(f'tam 1 : {self._jugador1.tamanio} tam 2: {self._jugador2.tamanio} ')
            self.mostrar_pantalla()
                        
###############################################################################
#
#                           Logica del juego
#
###############################################################################

            if not self._guerra:
                for carta in self._cartas_en_mesa:
                    carta.dato.boca_abajo = True 
                # print(f'carta1: {carta1.valor} carta2: {carta2.valor}')
                if num[carta1.valor] > num[carta2.valor]:
                    if self._jugador1.tamanio==0:
                        self._jugador1 = self._cartas_en_mesa
                    else:
                        self._jugador1 = self._jugador1 + self._cartas_en_mesa
                elif num[carta1.valor] < num[carta2.valor]:
                    if self._jugador2.tamanio==0:
                        self._jugador2 = self._cartas_en_mesa
                    else:
                        self._jugador2 = self._jugador2 + self._cartas_en_mesa
                    # print("gana2")
                    # print(self._cartas_en_mesa)
                    
                self._cartas_en_mesa = ListaDobleEnlazada()
            # print(f'J1 : {self._jugador1}')
            # print(f'J2 : {self._jugador2}')
            if self._jugador1.tamanio == 0 or self._jugador2.tamanio == 0:
                break
###############################################################################
#
#                       FIN DEL WHILE
#
###############################################################################
        print("-------------------------------------------------")
        if self.turnos_jugados == 10000:
            self._empate = True
            print("***** Empate *****")
            print(f'Turnos jugados: {self.turnos_jugados}')
        elif self._jugador1.tamanio > self._jugador2.tamanio: 
            self._ganador = 'jugador 1'
            print("***** jugador 1 gana la partida *****")
            print(f'Turnos jugados: {self.turnos_jugados}')
        elif self._jugador2.tamanio > self._jugador1.tamanio:
            self._ganador = 'jugador 2'
            print("***** jugador 2 gana la partida *****")
            print(f'Turnos jugados: {self.turnos_jugados}')
       


#PRUEBAS
if __name__ == "__main__":
    
               
    m = JuegoGuerra(314) # el 17 fuerza la _guerra
    m.iniciar_juego()
    # cartas = ListaDobleEnlazada()
    # cartas2 = ListaDobleEnlazada()
    # cartas.agregar(Carta(valores[0], palos[1]))
    # cartas.agregar(Carta(valores[1], palos[1]))
    # cartas.agregar(Carta(valores[2], palos[1])) 
    # nueva_carta = Carta(valores[3], palos[1])
    # nueva_carta.boca_abajo = False
    # cartas2.agregar(nueva_carta)
    
    # cartas = cartas + cartas2
    # for carta in cartas:
    #     carta.dato.boca_abajo = True
    
    
    # for carta in cartas:
    #     if  carta.dato.boca_abajo:
    #         print(carta.dato.valor)
        

