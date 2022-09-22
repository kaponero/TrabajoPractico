# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 18:03:38 2022

@author: kapon
"""

from listadobleenlazada import ListaDobleEnlazada
import random

valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
palos = ['♠', '♥', '♦', '♣']

class JuegoGuerra:
        
        def __init__ (self,semilla):
            random.seed(semilla)
            self.jugador1 = ListaDobleEnlazada()
            self.jugador2 = ListaDobleEnlazada()
            
        def masos(self):
            maso = [self.genera_carta()] 
            i=1
            while (i<52):
                nueva_carta = (self.genera_carta())
                if nueva_carta not in maso: 
                    maso.append(nueva_carta)
                    i+=1
            print(maso)
            
            i=0
            while(i<52):
                self.jugador1.anexar(maso[i])
                self.jugador2.anexar(maso[i+1])
                i+=2
        
        def genera_carta(self):
            carta = []
            carta.append(valores[random.randint(0, 12)])
            carta.append(palos[random.randint(0, 3)])
            return carta
        