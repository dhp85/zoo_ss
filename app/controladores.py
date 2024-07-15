from app.modelos import Grupo_Entrada
from app.vistas import VistaInput, VistaGrupo, VistaInputEntero
from simple_screen import DIMENSIONS, Screen_manager, cls, locate, Input



with Screen_manager:
    
    class zoo:
        def __init__(self):
            
            self.grupo_entradas = Grupo_Entrada()
            self.x = (DIMENSIONS.w - 37) // 2

            self.vista_grupo = VistaGrupo(self.grupo_entradas, self.x, 1)
            self.entrada_edad = VistaInputEntero("Edad: ", self.x, 12)
            self.entrada_seguir = VistaInput("Otra vez (S/N): ", self.x, 14)

        def run(self):
            while True:
                cls()
                self.vista_grupo.paint()
                edad =self.entrada_edad.paint()
                if edad == "":
                    respuesta = self.entrada_seguir.paint()
                    if respuesta == "S":
                        grupo_entradas = Grupo_Entrada() # asigna por referencia
                        self.vista_grupo.grupo = grupo_entradas
                        continue
                    else:
                        break
                
                
                edad = int(edad)
                self.grupo_entradas.add_entrada(edad) # asigna por referencia


 