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
        
    def mostrar_carta(self):
      print(self.valor + self.palo)
    
    def is_boca_arriba(self):
         boca_arriba = True
         self.mostrar_carta()
            
    def is_boca_abajo(self):
        boca_abajo = True
        print('X')
        
<<<<<<< HEAD
        
#----------- Clase MAZO ------------
=======
    def __str__(self):
        cadena=self.valor + " "+ self.palo
        return cadena
#----------------------------------------
>>>>>>> cae463bc9fb5a9693e647efa5e09aa064caf5dc4
class Mazo:
    def __init__(self):
        self.cartas = ListaDobleEnlazada()
        
    def Mezclar(self):
        cartas_ordenadas = []
        for valor in valores:
            for palo in palos:
                carta=Carta(valor,palo)
                cartas_ordenadas.append(carta)
        random.shuffle(cartas_ordenadas)
        for carta in cartas_ordenadas:
            self.cartas.anexar(carta)
            
<<<<<<< HEAD
=======
        def __str__(self):
           return str(self.cartas)
            
                
>>>>>>> cae463bc9fb5a9693e647efa5e09aa064caf5dc4

    def Mostrar_Mazo(self):
        
        print(self.cartas)

# class JuegoGuerra:
        
#         def __init__ (self,semilla):
#             random.seed(semilla)
#             self.jugador1 = ListaDobleEnlazada()
#             self.jugador2 = ListaDobleEnlazada()
            
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
# if __name__ == "__main__":
    
<<<<<<< HEAD
  # car = Carta('2','♥')       
  # #car.mostrar_carta()    
  # #car.is_boca_arriba()    
  # car.is_boca_abajo()            
                            
=======
 car = Carta('2','♥')
 print(car)       
 #car.mostrar_carta()    
 #car.is_boca_arriba()    
 car.is_boca_abajo()
 
 
 cartitas=ListaDobleEnlazada()
 cartitas.anexar(Carta(valores[0],palos[0]))
 cartitas.anexar(Carta(valores[2],palos[3])) 
 print(cartitas)
 mazo = Mazo()  
 mazo.Mezclar()
 print(mazo.cartas.extraer(0))
 
                
                
                
>>>>>>> cae463bc9fb5a9693e647efa5e09aa064caf5dc4
        
