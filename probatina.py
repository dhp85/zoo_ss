from app.modelos import Entrada, Grupo_Entrada, TipoEntrada

grupo_de_noemi = Grupo_Entrada()

grupo_de_noemi.add_entrada(82)
grupo_de_noemi.add_entrada(37)

entrada = Entrada(16)
print("hola")
print(entrada.tipo)
print(entrada.precio)
print(entrada._Entrada__edad)
