# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 18:03:38 2022

@author:    González, Gabriela
            Labanca, Alvaro
            Pérez Albarracín, Maximiliano    
"""

from LDE import ListaDobleEnlazada
import random

valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
num = {'2':2,'3': 3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'A':14} # DICCIONARIO PARA ASIGNAR VALORES
palos = ['♠', '♥', '♦', '♣']

#----------- Clase CARTA ------------
class Carta:
    
    def __init__ (self,val,pal):
        self.valor = val
        self.palo = pal
        self.boca_abajo = True
        
    def mostrar_carta(self):
        print(self.valor + self.palo)
    
    def poner_boca_arriba(self):
        self.boca_abajo = False
        cadena=self.valor + self.palo
        return cadena
            
    def poner_boca_abajo(self):
        self.boca_abajo = True
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
    
            
#----------- Clase Juego de _guerra --------------       
class Juego_guerra:
        
        def __init__ (self,semilla):
            random.seed(semilla)
            self._jugador1 = ListaDobleEnlazada()
            self._jugador2 = ListaDobleEnlazada()
            self._turnos_jugados = 0
            self._ganador = " "
            self._empate = False
            self._guerra = False
        
        @property
        def turnos_jugados(self):
            return self._turnos_jugados
        
        @property
        def ganador(self):
            self._ganador = ''
            return self._ganador
        
        @property
        def empate(self):
            self._empate = False
            return self._empate
        
        def terminar(self):
            if self._ganador == 'jugador 1':
                print("***** jugador 1 gana la partida *****")
            if self._ganador == 'jugador 2':
                print("***** jugador 2 gana la partida *****")
            if self._empate:
                print("\n")
                print("***** empate *****")
        
        # repartimos el mazo en las dos barajas para cada jugador
        def repartir_cartas(self, mazo):
            # repartimos las cartas a cada jugador
            while mazo.cartas.tamanio > 2:
                self._jugador1.anexar(mazo.cartas.extraer().dato)
                self._jugador2.anexar(mazo.cartas.extraer().dato)
            # aca hay un error con la ultima carta y por eso lo hacemos aparte
            self._jugador1.anexar(mazo.cartas.extraer().dato)
            self._jugador2 + mazo.cartas

        # FUNCION inicio del juego
        def iniciar_juego(self):
            mazo = Mazo() #creamos mazo
            mazo.Mezclar() #mezclamos mazo
            self.repartir_cartas(mazo) 
             
            # iniciamos TURNOS de combate
            while self._turnos_jugados < 10000 and self.empate == False:
                
                self._turnos_jugados += 1 #contador de turnos
                                
                contador = 1
                # extraemos las cartas de arriba de cada jugador
                cartas_en_mesa = ListaDobleEnlazada()
                if self._jugador1.tamanio == 0 or self._jugador2.tamanio == 0:
                    self.terminar()
                    return
                else:
                    carta1 = self._jugador1.extraer(0).dato
                    carta2 = self._jugador2.extraer(0).dato
                    carta1.boca_abajo = False
                    carta2.boca_abajo = False
                    cartas_en_mesa.anexar(carta1)
                    cartas_en_mesa.anexar(carta2)
                    if carta1.valor == carta2.valor:
                        self._guerra = True    
                
                while self._guerra == True and self._jugador1.tamanio > 0:
                    for n in range(1,4): #si hay guerra sacamos 3 cartas boca abajo
                        if self._jugador1.tamanio < 2 or self._jugador2.tamanio < 2: #si un jugador se queda sin  cartas terminamos la partida
                            if self._jugador1.tamanio < 2:
                                # print("\n")
                                print("-------------------------------------------------") 
                                print("Turno: " + str(self._turnos_jugados))
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
                                print("-------------------------------------------------") 
                                print("** GUERRA: jugador 1 no posee suficientes cartas **")
                                self._ganador = 'jugador 2'
                            else:
                                print("-------------------------------------------------") 
                                print("Turno: " + str(self._turnos_jugados))
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
                                print("-------------------------------------------------") 
                                print("** GUERRA: jugador 2 no posee suficientes cartas **")
                                self._ganador = 'jugador 1'
                            self.terminar()
                            return
                        #sacamos cartas alternativamente a cada jugador
                        carta1 = self._jugador1.extraer(0).dato
                        carta2 = self._jugador2.extraer(0).dato
                        cartas_en_mesa.anexar(carta1)
                        cartas_en_mesa.anexar(carta2)
                        carta1.boca_abajo = True
                        carta2.boca_abajo = True
                    #y sacamos una carta boca arriba para ver quien gana la guerra
                    carta1 = self._jugador1.extraer(0).dato
                    carta2 = self._jugador2.extraer(0).dato
                    carta1.boca_abajo = False
                    carta2.boca_abajo = False
                    cartas_en_mesa.anexar(carta1)
                    cartas_en_mesa.anexar(carta2)
                    if carta1.valor != carta2.valor:
                        self._guerra = False
                
#---------------------------------MOSTRAR TABLERO----------------------------------------
                print("-------------------------------------------------") 
                print("Turno: " + str(self._turnos_jugados))
                print("Jugador 1: ")
                # mostrar cartas jugador 1
                fin = ''
                if self._jugador1.tamanio > 0:
                    for carta in self._jugador1:
                        # carta.dato.boca_abajo = True
                        if contador%10 == 0: fin = '\n'
                        else: fin = ''
                        if (carta.dato.boca_abajo):
                            print(" " + carta.dato.poner_boca_abajo(), end=fin)
                        contador += 1
                    
                # mostrar cartas jugadas en la mesa
                print("\n")
                print("         ",end="")
                posicion = 1
                for carta in cartas_en_mesa:
                    if  not carta.dato.boca_abajo:
                        print(carta.dato.poner_boca_arriba() + " ", end="")
                    else:
                        print(carta.dato.poner_boca_abajo() + " ", end="")
                    posicion += 1
                     
                # mostrar cartas jugador 2    
                print("\n")
                print("Jugador 2: ")
                contador = 1
                fin = ''
                if self._jugador2.tamanio > 0:
                    for carta in self._jugador2:
                        # carta.dato.boca_abajo = True
                        if contador%10 == 0: fin = '\n'
                        else: fin = ''
                        if (carta.dato.boca_abajo):
                            print(" " + carta.dato.poner_boca_abajo(), end=fin)
                        contador += 1
                elif self._jugador2.tamanio == 0:
                    self._jugador2 = ListaDobleEnlazada()
                
                print("\n")
                print("-------------------------------------------------")
                
#-------------------------Asignacion de cartas al ganador------------------------
                if num[carta1.valor] > num[carta2.valor]:
                    # self._jugador1 + cartas_en_mesa
                    if self._jugador1.tamanio == 0:
                        for carta in cartas_en_mesa:
                            self._jugador1.agregar(carta.dato)
                    else:
                        self._jugador1 + cartas_en_mesa
                        
                else:
                    if self._jugador2.tamanio == 0:
                        for carta in cartas_en_mesa:
                            self._jugador2.agregar(carta.dato)
                    else:
                        self._jugador2 + cartas_en_mesa
                #"guardamos" las cartas boca abajo en el mazo
                for carta in self._jugador1:
                    carta.dato.boca_abajo = True
                
                for carta in self._jugador2:
                    carta.dato.boca_abajo = True
                                
                cartas_en_mesa = ListaDobleEnlazada() #reseteamos la LDE "cartas en mesa"
                print("Cantidad de cartas jugador 1: " + str(self._jugador1.tamanio))
                print("Cantidad de cartas jugador 2: " + str(self._jugador2.tamanio))
                
                # MOSTRAMOS LAS CARTAS DE CADA JUGADOR
                if self._jugador1.tamanio > 0 and self._jugador1.tamanio < 52:
                    print("Cartas jugador 1: ")
                    print(self._jugador1)
                if self._jugador2.tamanio > 0 and self._jugador2.tamanio < 52:
                    print("Cartas jugador 2: ")
                    print(self._jugador2)
                
                # MOSTRAMOS EL TAMAÑO DE CADA MAZO 
                if self._jugador1.tamanio == 52:
                    self._ganador = 'jugador 1'
                    self.terminar()
                    return
                elif self._jugador2.tamanio == 52:
                    self._ganador = 'jugador 2'
                    self.terminar()
                    return
                        
            if self.turnos_jugados == 10000:
                self._empate = True # YA SE JUGARON 10000 TURNOS
                self.terminar()


# ##########################################################################################
# #PRUEBAS
if __name__ == "__main__":
    
    m = Juego_guerra(117)
    # m = Juego_guerra(314)
    # m = Juego_guerra(59)
    # m = Juego_guerra(883)
    # m = Juego_guerra(167)
    # m = Juego_guerra(190)
    # m = Juego_guerra(735) # EMPATE
    # m = Juego_guerra(547)
    # m = Juego_guerra(296)
    # m = Juego_guerra(137) # EMPATE
    # m = Juego_guerra(683) # EMPATE
    # m = Juego_guerra(1383)
    # m = Juego_guerra(145)
    # m = Juego_guerra(1112)
    # m = Juego_guerra(1373)
    
    m.iniciar_juego()
    
        
