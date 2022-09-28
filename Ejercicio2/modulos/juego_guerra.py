# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 18:03:38 2022

@author: kapon
"""

from LDE import ListaDobleEnlazada
import random

valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
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
        cadena=self.valor + " "+ self.palo
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

# repartimos el mazo en las dos barajas para cada jugador
        def repartir_cartas(self, mazo):
            # repartimos las cartas a cada jugador
            while mazo.cartas.tamanio > 2:
                self.jugador1.anexar(mazo.cartas.extraer().dato)
                self.jugador2.anexar(mazo.cartas.extraer().dato)
            # aca hay un error con la ultima carta y por eso lo hacemos aparte
            self.jugador1.anexar(mazo.cartas.extraer().dato)
            print(mazo.cartas.tamanio)
            self.jugador2 + mazo.cartas
            # mostramos las cartas de ambos jugadores
            print(self.jugador1) 
            print(self.jugador2) 
        
        # FUNCION inicio del juego
        def iniciar_juego(self):
            mazo = Mazo() #creamos mazo
            mazo.Mezclar() #mezclamos mazo
            self.repartir_cartas(mazo) 
             
            # iniciamos TURNOS de combate
            # while self.jugador1.tamanio > 0 or self.jugador2.tamanio > 0:
            # while self.jugador1 or self.jugador2 or self.empate:    
            self.turnos_jugados += 1 #contador de turnos
             
            print("-------------------------------------------------") #esto es una barra separadora
            print("Turno: " + str(self.turnos_jugados))
            print("Jugador 1: ")
            fin = ''
            contador = 1
            # extraemos las cartas de arriba de cada jugador
            cartas_en_mesa = ListaDobleEnlazada()
            
            carta1 = self.jugador1.extraer().dato
            carta2 = self.jugador2.extraer().dato
            carta1.boca_abajo = False
            carta2.boca_abajo = False
            cartas_en_mesa.anexar(carta1)
            cartas_en_mesa.anexar(carta1)
            carta2 = carta1
            
            # for para mostrar las cartas de jugador 1 boca abajo

#----------------logica de guerra----------------------------------------------
            if carta1.valor == carta2.valor:
                self.guerra=True
                for n in range(1,3): #si hay guerra sacamos 3 cartas boca abajo
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
#------------------------------------------------------------------------------
            for carta in self.jugador1:
                if contador%10 == 0: # logica para mostrar las cartas boca abajo en filas de a 10
                    fin = '\n'
                else:
                    fin = ''
            # print(carta.dato.is_boca_abajo(), end=fin)
                if (carta.dato.boca_abajo):
                    print(" "+carta.dato.poner_boca_abajo(), end=fin)
                contador += 1

            print("\n")
             
            print("              ",end="")
            for carta in cartas_en_mesa:
                if  not carta.dato.boca_abajo:
                    print(carta.dato.poner_boca_arriba() + " ", end="")
                else:
                    print(carta.dato.poner_boca_abajo() + " ", end="")
                #print(f'          {carta} {carta2}') # mostramos las cartas que combaten

                 
             # for para mostrar las cartas de jugador 1 boca abajo                
            print("\n" + "Jugador 2: ")
            fin = ''
            contador = 1
            for carta in self.jugador2:
                if contador%10 == 0:
                    fin = '\n'
                else:
                    fin = ''
                # print(carta.dato.is_boca_abajo(), end=fin)
                if (carta.dato.boca_abajo):
                    print(" "+carta.dato.poner_boca_abajo(), end=fin)
                contador += 1
            print("\n")
            print("-------------------------------------------------")
             
            #-------------------------logica del juego------------------------
             

# class JuegoGuerra:
        
          
#         def masos(self):
#             maso = [self.genera_carta()] 
#             i=1
#             while (i<52):
#                 nueva_carta = (self.genera_carta())
#                 if nueva_carta not in maso: 
#                     maso.append(nueva_carta)
#                     i+=1
#             print(maso)
            
#             i=0
#             while(i<52):
#                 self.jugador1.anexar(maso[i])
#                 self.jugador2.anexar(maso[i+1])
#                 i+=2
        
#         def genera_carta(self):
#             carta = []
#             carta.append(valores[random.randint(0, 12)])
#             carta.append(palos[random.randint(0, 3)])
#             return carta
        
#         def jugar(self):
#             turno = 0
#             en_juego = []
#             while (self.jugador1.tamanio()!=0 or self.jugador2.tamanio()!=0):
#             #while (turno<2):
#                 en_juego.append(self.jugador1.extraer())
#                 en_juego.append(self.jugador2.extraer())
                
#                 if en_juego[len(en_juego)-2][0]=='A' and en_juego[len(en_juego)-1][0]=='A' or en_juego[len(en_juego)-2][0]==en_juego[len(en_juego)-1][0]:
#                     print("Guerra!")
#                     turno+=1
#                     continue

#                 print("-------------------------------------------")
#                 print(f'Turno: {turno}')
#                 print("Jugador 1:")
#                 for j in range(1, self.jugador1.tamanio()+1):
#                     if j%10 == 0 :
#                         fin_de_linea = '\n'
#                     else:
#                         fin_de_linea = ""
#                     print("-X ",end=fin_de_linea)
                    
#                 print("")
#                 print("            ",end="")
#                 print(en_juego[len(en_juego)-2][0] + en_juego[len(en_juego)-2][1] + " ",end="")
#                 print(en_juego[len(en_juego)-1][0] + en_juego[len(en_juego)-1][1])
#                 print("")
                
#                 if en_juego[len(en_juego)-2][0]>en_juego[len(en_juego)-1][0]:
#                         self.jugador1.agregar(en_juego.pop())
#                         self.jugador1.agregar(en_juego.pop())
#                 print("Jugador 2:")
#                 for j in range(1, self.jugador2.tamanio()+1):
#                     if j%10 == 0 :
#                         fin_de_linea = '\n'
#                     else:
#                         fin_de_linea = ""
#                     print("-X ",end=fin_de_linea)
#                 print("")
#                 turno+=1
 
# #PRUEBAS
if __name__ == "__main__":
    

#   car = Carta('2','♥')       
#   #car.mostrar_carta()    
#   #car.is_boca_arriba()    
#   car.is_boca_abajo()            
                            

#   car = Carta('2','♥')
#   print(car)       
#   #car.mostrar_carta()    
#   #car.is_boca_arriba()    
#   car.is_boca_abajo()
 
 
    # cartitas=ListaDobleEnlazada()
    # cartitas.anexar(Carta(valores[0],palos[0]))
    # cartitas.anexar(Carta(valores[2],palos[3])) 
    # print(cartitas)
    # mazo = Mazo()  
    # mazo.Mezclar()
    # print(mazo.cartas.extraer(0))      
                
    m = JuegoGuerra(45)
    m.iniciar_juego()
    
        
