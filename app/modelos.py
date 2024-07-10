from enum import Enum, auto


class TipoEntrada(Enum):
    BEBE =  0
    NIÑO = 14
    ADULTO = 23
    JUBILADO = 18



class Entrada:
    def __init__(self, edad:int):
        self.__validate_edad(edad)
        self.__edad = edad
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

    def __validate_edad(self, edad):
        if edad < 0:
            raise ValueError("La edad no debe ser negativa.")
        elif edad > 99:
            raise ValueError("La edad no debe ser superior a 99 años.")          

class Grupo_Entrada():
    def __init__(self):
        self.total = 0       
        self.num_entradas = 0 
        self.tipos_entrada = {
            TipoEntrada.BEBE: {"precio" : 0, "Q" : 0 },
            TipoEntrada.NIÑO: {"precio" : 14, "Q": 0},
            TipoEntrada.ADULTO: {"precio" : 23, "Q":0},
            TipoEntrada.JUBILADO: {"precio" : 18, "Q":0}

        }     

    def add_entrada(self, edad):
        entrada = Entrada(edad)
        self.total += entrada.precio
        self.num_entradas += 1 
        self.tipos_entrada[entrada.tipo]["Q"] += 1

    def cantidad_entradas_tipo(self, tipo: TipoEntrada):
        return self.tipos_entrada[tipo]["Q"]    
 
    def subtotal_tipo(self, tipo: TipoEntrada):
        return self.tipos_entrada[tipo]["Q"] * self.tipos_entrada[tipo]["precio"]


 
