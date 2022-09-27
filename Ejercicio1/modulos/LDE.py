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

        
    def __str__(self):
        return str(self.dato)
        
class InsertarListaError(Exception):
    """error al ingresar valor negativo"""
    
class ExtraerListaError(Exception):
        """error al extraer"""

# except IndexError:
# print("list index out of range")
# sys.exit(1)


class ListaDobleEnlazada:
    
    #inicialmente solo contendra un elemento que apunta al inicio de la lista
    def __init__ (self):
        self.cabeza = None
        self.cola = None
        self._tamanio = 0
    
    @property
    def tamanio(self):
        return self._tamanio    
    
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
    
            
    #agrega un elemento al inicio de la lista
    # @property
    def agregar(self,dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self._tamanio += 1
            return
        if self.cola is None:
            self.cola = self.cabeza
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza.anterior = nuevo_nodo
        self.cabeza = nuevo_nodo
        self._tamanio += 1
        
    #insertar elementos al final
    # @property   
    def anexar(self,dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self._tamanio += 1
            return
        if self.cola is None:
            self.cola = nuevo_nodo
            self.cola.anterior = self.cabeza
            self.cabeza.siguiente = self.cola
            self._tamanio += 1
            return
        nuevo_nodo.anterior = self.cola
        self.cola.siguiente = nuevo_nodo
        self.cola = nuevo_nodo
        self._tamanio += 1
    
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
        if posicion < 0:
            raise InsertarListaError("La posicion no puede ser negativa")
            return
        if posicion > self.tamanio:
            raise InsertarListaError("No existe posicion")
            return
        
        while pos < posicion:
            pos += 1
            n = n.siguiente
        nuevo_nodo = Nodo(dato)
        n.anterior.siguiente = nuevo_nodo
        nuevo_nodo.anterior =n.anterior
        nuevo_nodo.siguiente = n
        n.anterior = nuevo_nodo
        self._tamanio += 1
            
    #elimina y extrae
    # @property        
    # def extraer(self,*posicion):
    def extraer(self,posicion=-1):
        if len(posicion)==0: #elimina y devuelve el item en ultimo posicion
            if self.esta_vacia:
                raise ExtraerListaError("La lista esta vacia")
                return
            n = self.cabeza 
            if n.siguiente is None:
                self.cabeza = None
                return n.dato
            n = self.cola
            n.anterior.siguiente = None
            self.cola = n.anterior
            return n
        #else: #elimina y devuelve el item en la posicion enviada
        
        elif posicion[0]==0:
            n = self.cabeza
            n.siguiente.anterior = None
            self.cabeza = n.siguiente
            return n
        elif posicion[0] < 0:
            raise IndexError("list index out of range")
            # raise ExtraerListaError("La posicion no puede ser negativa")
        elif posicion[0] >= self.tamanio:
            raise ExtraerListaError("No existe posicion")
        else:
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
                return n
 #ESTE ES EL METODO QUE YO (GAby) HABIA PROBADO, PERO EL TEST_EXTRAER_EXTREMOS NO FUNCIONA, EL ERROR QUE ME TIRA ES :AttributeError: 'int' object has no attribute 'dato',
 #no se porque, porque si esta dando un dato
 # def extraer(self,posicion):
    #     # Verificación de los límites
    #         if (posicion < 0) or (posicion >= self.tamanio):
    #             raise IndexError("Índice fuera de rango")
    #     # Si no se recibió i, se devuelve el último.
    #         if posicion == None:
    #             posicion = self.tamanio - 1
    #     # Caso particular, si es el primero,hay que saltar la cabecera de la lista
    #         if posicion == 0:
    #             data = self.cabeza.dato
    #             self.cabeza = self.cabeza.siguiente
    #     #porcion de codigo correspondiente a la busqueda
    #         nodo_ant = self.cabeza
    #         nodo_actual =nodo_ant.siguiente
    #         for pos in range(1, posicion):
    #             nodo_ant = nodo_actual
    #             nodo_actual = nodo_ant.siguiente
                
    #     # Guarda el dato y elimina el nodo a borrar
    #         data = nodo_actual.dato
    #         nodo_ant.siguiente = nodo_actual.siguiente
    #     # hay que restar 1 de tamanio
    #         self._tamanio = self._tamanio - 1
    #     # y devolver el valor borrado
    #         return data
             
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
        self.cola = p
        while q is not None:
            q.anterior = q.siguiente
            q.siguiente = p
            p = q
            q = q.anterior
        self.cabeza = p
        

        
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
    def concatenar(self, lista):
        self._tamanio += lista.tamanio
        self.cola.siguiente = lista.cabeza
        lista.cabeza.anterior = self.cola
        self.cola = lista.cola
        return self
        
    
#----------- sobracarga del operador "+" para concatenar -------
# la suma de dos cadenas agregara el segundo sumando al primero a = a + b
    def __add__(self,lista):
        return self.concatenar(lista)
        

    
    
#------------------iterar sobre la lista-------------------------
            
    def __iter__(self):
        n = self.cabeza
        while n is not None:
            yield n
            n = n.siguiente
            

#---------------sobrecarga de str para mostrar por pantalla---------
    def __str__(self):
        nodo = self.cabeza
        cadena = '['
        while nodo.siguiente is not None:
            cadena += str(nodo.dato) +', '
            nodo = nodo.siguiente
        cadena += str(nodo.dato) + ']'
        return cadena
    
#-------------sobrecarga de repr para cambiar ese valor-------------
    # def __repr__(self):
    #     nodo = self.cabeza
    #     cadena = '['
    #     while nodo.siguiente is not None:
    #         cadena += str(nodo.dato) +', '
    #         nodo = nodo.siguiente
    #     cadena += str(nodo.dato) + ']'
    #     return cadena

if __name__ == "__main__":
    lista = ListaDobleEnlazada()
    lista1 = ListaDobleEnlazada()
    
    lista.anexar(90)
    lista.anexar(50)
    lista.anexar(30)
    lista.anexar(10)
    lista.anexar(10)
    lista.agregar(-10)
    print(lista.tamanio)
    
    
    lista1.anexar(0)
    lista1.anexar(20)
    
    print(lista)
    lista3 = lista + lista1
    print(lista3)
    print(lista3.tamanio)
    





