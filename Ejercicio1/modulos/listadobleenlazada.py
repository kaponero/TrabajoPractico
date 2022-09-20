# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 16:13:56 2022

@author: kapon
"""

from node import Node

class ListaDobleEnlazada:
    
    #inicialmente solo contendra un elemento que apunta al inicio de la lista
    def __init__ (self):
        self.nodo_inicial = None
    
    @property
    def nodo_inicial(self):
        return self._nodo_inicial
    
    @nodo_inicial.setter
    def nodo_inicial(self,nodo):
        if nodo is None:
            self._nodo_inicial = None
        else:
            self._nodo_inicial = nodo
    
    #verifica si la lista esta vacia
    @property    
    def esta_vacia(self):
        esta_vacia = False
        if self.nodo_inicial is None:
            esta_vacia = True
        return esta_vacia
    
    #devuelve la cantidad de items de la lista
    #@property
    def tamanio(self):
        tamanio = 0
        n = self.nodo_inicial
        while n is not None:
            tamanio += 1
            n = n.nref
        return tamanio
            
    #agrega un elemento al inicio de la lista
    # @property
    def agregar(self,dato):
        if self.nodo_inicial is None:
            nuevo_nodo = Node(dato)
            self.nodo_inicial = nuevo_nodo
            return
        nuevo_nodo = Node(dato)
        nuevo_nodo.nref = self.nodo_inicial
        self.nodo_inicial.pref = nuevo_nodo
        self.nodo_inicial = nuevo_nodo
        
    #insertar elementos al final
    # @property
    def anexar(self,dato):
        if self.nodo_inicial is None:
            nuevo_nodo = Node(dato)
            self.nodo_inicial = nuevo_nodo
            return
        n = self.nodo_inicial
        while n.nref is not None:
            n = n.nref
        nuevo_nodo = Node(dato)
        n.nref = nuevo_nodo
        nuevo_nodo.pref = n
        
    #insertar un nuevo elemento en una posicion
    # @property
    def insertar(self,posicion,dato):
        pos=0
        n = self.nodo_inicial
        while pos <= posicion and n is not None:
            pos+=1
            n = n.nref
        if n is None:
            print("no existe posicion")
        else:
            nuevo_nodo = Node(dato)
            nuevo_nodo.nref = n #el nodo actual pasa a ser el siguiente nodo
            nuevo_nodo.pref = n.pref #el nodo anterior sigue siendo el anterior
            if n.pref is not None:
                n.pref.nref = nuevo_nodo # si el nodo anterior no es el primero, tengo q decirle a su nref que el siguiente dato es el nuevo
            n.pref = nuevo_nodo #finalmente le digo al dato que estaba en n que su dato anterior es el nuevo dato
            
    #elimina y extrae
    # @property        
    def extraer(self,*posicion):
        if len(posicion)==0: #elimina y devuelve el item en ultimo posicion
            if self.esta_vacia:
                print("lista vacia")
                return
            n = self.nodo_inicial 
            if n.nref is None:
                self.nodo_inicial = None
                return n.item
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None
            return n.item
        else: #elimina y devuelve el item en la posicion enviada
            #aca hay q hacer la otra aprte
            return n.item
            
    #elimina y devuelve el item en la posicion
    # def extraer(self,posicion):
    #     if self.esta_vacia:
    #         print("lista vacia")
    #     else:
    #         n = self.nodo_inicial
    #         # if posicion is None:
    #         #     while n.nref is not None:
    #         #         n = n.nref
    #         # else:
    #         pos=0 
    #         while pos <= posicion and n is not None:
    #             n = n.nref
    #             pos += 1
    #         if n is None:
    #             print("no existe posicion")
    #         else:
    #             #falta conciderar los extremos
    #             n.pref.nref = n.nref
    #             n.nref.pref = n.pref          
    #         return n
        
    #Realiza una copia de la lista elemento a elemento y devuelve la copia
    # @property
    def copiar(self):
        copia_lista = ListaDobleEnlazada
        n = self.nodo_inicial
        while n is not None:
            copia_lista.nodo_inicial = n
            n = n.nref
        return copia_lista
   

         
        