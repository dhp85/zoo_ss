from enum import Enum, auto
from collections import namedtuple

Datos_Entrada = namedtuple("Datos_Entrada", ("precio", "edad_max"))


class TipoEntrada(Enum):
    BEBE = Datos_Entrada(0, 2)
    NIÑO = Datos_Entrada(14, 12)
    ADULTO = Datos_Entrada(23, 64)
    JUBILADO = Datos_Entrada(18, 99)



class Entrada:
    def __init__(self, edad:int):
        self.__validate_edad(edad)
        self.__edad = edad

        for tipo in TipoEntrada:
            if edad <= tipo.value.edad_max:
                self.tipo = tipo
                self.precio = tipo.value.precio
                break
        """    
        if edad <= 2:
            self.tipo = TipoEntrada.BEBE
            self.precio = 0
        elif edad <13:
            self.tipo = TipoEntrada.NIÑO
            self.precio = 14
        elif edad <65:    
            self.tipo = TipoEntrada.ADULTO
            self.precio = 23
        else:
            self.tipo = TipoEntrada.JUBILADO
            self.precio = 18 
        """      

    def __validate_edad(self, edad):
        if edad < 0:
            raise ValueError("La edad no debe ser negativa.")
        elif edad > 99:
            raise ValueError("La edad no debe ser superior a 99 años.")          

class Grupo_Entrada():
    def __init__(self):
        self.total = 0       
        self.num_entradas = 0 
        self.tipos_entrada = {}
        for tipo in TipoEntrada:
            self.tipos_entrada[tipo] = {"Q": 0, "P": tipo.value.precio}

            #con dict comprehension
            #self.tipos_entrada = {tipo.name: {"p": tipo.value, "Q": 0} for tipo in TipoEntrada}  


    def add_entrada(self, edad):
        entrada = Entrada(edad)
        self.total += entrada.precio
        self.num_entradas += 1 
        self.tipos_entrada[entrada.tipo]["Q"] += 1

    def cantidad_entradas_tipo(self, tipo: TipoEntrada):
        return self.tipos_entrada[tipo]["Q"]    
 
    def subtotal_tipo(self, tipo: TipoEntrada):
        return self.tipos_entrada[tipo]["Q"] * self.tipos_entrada[tipo]["P"]


 
