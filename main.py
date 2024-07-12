from app.modelos import Grupo_Entrada
from app.vistas import VistaEntrada, VistaGrupo
from simple_screen import DIMENSIONS, Screen_manager, cls, locate, Input



with Screen_manager:
    # Instanciamos lo necesario
    grupo_entradas = Grupo_Entrada()
    x = (DIMENSIONS.w - 37) // 2

    vista_grupo = VistaGrupo(grupo_entradas, x, 1)
    entrada_edad = VistaEntrada("Edad: ", x, 12)
    entrada_seguir = VistaEntrada("Otra vez (S/N): ", x, 14)



    # bucle de pantalla
    while True:
        cls()
        vista_grupo.paint()
        edad = entrada_edad.paint()
        if edad == "":
            respuesta = entrada_seguir.paint()
            if respuesta == "S":
                grupo_entradas = Grupo_Entrada() # asigna por referencia
                vista_grupo.grupo = grupo_entradas
                continue
            else:
                break
        
        
        edad = int(edad)
        grupo_entradas.add_entrada(edad) # asigna por referencia

    


    locate(1, DIMENSIONS.h - 2)
    Input("Pulse enter para salir")
    


"""
from app.controladores import Zoo

zoo = Zoo()
zoo.run()
"""