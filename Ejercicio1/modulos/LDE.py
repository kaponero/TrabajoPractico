# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 16:13:56 2022

@author: kapon
"""

class Nodo:
    def __init__(self,data):
        self.dato = data
        self.siguiente = None
        self.anterior = None


class ListaDobleEnlazada:
    
    #inicialmente solo contendra un elemento que apunta al inicio de la lista
    def __init__ (self):
        self.cabeza = None
        self.cola = None
    
    @property
    def cabeza(self):
        return self._cabeza
    
    @cabeza.setter
    def cabeza(self,nodo):
        if nodo is None:
            self._cabeza = None
        else:
            self._cabeza = nodo
    
    @property
    def cola(self):
        return self._cola
    
    @cola.setter
    def cola(self,nodo):
        if nodo is None:
            self._cola = None
        else:
            self._cola = nodo
    
    #verifica si la lista esta vacia
    @property    
    def esta_vacia(self):
        esta_vacia = False
        if self.cabeza is None:
            esta_vacia = True
        return esta_vacia
    
    #devuelve la cantidad de items de la lista
    @property
    def tamanio(self):
        tamanio = 0
        n = self.cabeza
        while n is not None:
            tamanio += 1
            n = n.siguiente
        return tamanio
            
    #agrega un elemento al inicio de la lista
    # @property
    def agregar(self,dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        if self.cola is None:
            self.cola = self.cabeza
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza.anterior = nuevo_nodo
        self.cabeza = nuevo_nodo
        
    #insertar elementos al final
    # @property   
    def anexar(self,dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        if self.cola is None:
            self.cola = nuevo_nodo
            self.cola.anterior = self.cabeza
            self.cabeza.siguiente = self.cola
            return
        nuevo_nodo.anterior = self.cola
        self.cola.siguiente = nuevo_nodo
        self.cola = nuevo_nodo
   
    
    #insertar un nuevo elemento en una posicion
    # @property
    def insertar(self,posicion,dato):
        pos=0
        n = self.cabeza
        if posicion == 0:
            self.agregar(dato)
            return
        if posicion == self.tamanio:
            self.anexar(dato)
            return
        
        while pos < posicion:
            pos += 1
            n = n.siguiente
        nuevo_nodo = Nodo(dato)
        n.anterior.siguiente = nuevo_nodo
        nuevo_nodo.anterior =n.anterior
        nuevo_nodo.siguiente = n
        n.anterior = nuevo_nodo
            
    #elimina y extrae
    # @property        
    def extraer(self,*posicion):
        if len(posicion)==0: #elimina y devuelve el item en ultimo posicion
            if self.esta_vacia:
                print("lista vacia")
                return
            n = self.cabeza 
            if n.siguiente is None:
                self.cabeza = None
                return n.dato
            n = self.cola
            n.anterior.siguiente = None
            self.cola = n.anterior
            return n.dato
        else: #elimina y devuelve el item en la posicion enviada
            pos = 0
            n = self.cabeza
            while pos < posicion[0] and n is not None:
                n = n.siguiente
                pos += 1
            if n is None:
                print("no existe posicion")
            else:
                if n.siguiente is None:
                    n.anterior.siguiente = None
                else:
                    n.anterior.siguiente = n.siguiente
                    n.siguiente.anterior = n.anterior
                return n.dato
             
#---- Realiza una COPIA de la lista elemento a elemento y devuelve la copia-------
    def copiar(self):
        lista_copia = ListaDobleEnlazada()
        nodo = self.cabeza
        while nodo is not None:
            lista_copia.anexar(nodo.dato)
            nodo = nodo.siguiente
        return lista_copia

         
#---------- invierte el orden de los elementos ----------
    def invertir(self):
        if self.cabeza is None:
            print('NO se puede')
            return
        p = self.cabeza
        q = p.siguiente
        p.siguiente = None
        p.anterior = q
        while q is not None:
            q.anterior = q.siguiente
            q.siguiente = p
            p = q
            q = q.anterior
        self.cabeza = p
        
#---------- muestra la lista de elementos desde el primero al ultimo----------
    def mostrar_lista(self):
        nodo = self.cabeza
        cant = self.tamanio
        print('Tamaño de la lista: ' + str(cant))
        while nodo.siguiente is not None:
            print(nodo.dato)
            nodo = nodo.siguiente
        print(nodo.dato)
        
#---------- ordena los elemento de menor a mayor ----------

# El algoritmo de ordenamiento del método “ordenar” de la Lista debe tener la eficiencia del
# algoritmo de ordenamiento por inserción, o mejor.(cumple?)

    def ordenar(self):
        end = None
        while end != self.cabeza:
            p = self.cabeza
            while p.siguiente != end:
                q = p.siguiente
                if p.dato > q.dato:
                    p.dato, q.dato = q.dato, p.dato
                p = p.siguiente
            end = p

#---------- concatena dos listas enlazadas ----------    
    def concatenar(self, Lista):
        nodo = Lista.cabeza
        while nodo is not None:
            self.anexar(nodo.dato)
            nodo = nodo.siguiente
        
    
#----------- sobracarga del operador "+" para concatenar -------
# la suma de dos cadenas agregara el segundo sumando al primero a = a + b
    def __add__(self,Lista):
        nodo = Lista.cabeza
        while nodo.siguiente is not None:
            self.anexar(nodo.dato)
            nodo = nodo.siguiente
        self.anexar(nodo.dato)
        return
    
    
#------------------iterar sobre la lista-------------------------
            
    def __iter__(self):
        n = self.cabeza
        while n is not None:
            yield n
            n = n.siguiente
            



# lista = ListaDobleEnlazada()
# lista.agregar(20)
# lista.agregar(22)
# lista.insertar(1,21)





