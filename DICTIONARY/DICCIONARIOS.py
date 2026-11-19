diccionario = {"clave1":"valor1","clave2":"valor2","clave3":[2,3,4]}
diccionario1 = {123:10000}
print(diccionario["clave3"][2])
print(diccionario.get("clavex", "Valor por defecto"))
diccionario1.update(diccionario)
print(diccionario)
print(diccionario1)
for clave in diccionario:
    print(diccionario[clave])
diccionario[(1,2,3)] = 100
print(diccionario)
del(diccionario["clave1"])
print(diccionario)
# diccionario.clear()
# print(diccionario)
lista_claves = list(diccionario.keys())
print(lista_claves)
print(type(lista_claves))
lista_valores = diccionario.values()
print(lista_valores)
lista_elemtos = diccionario.items()
print(lista_elemtos)
for clave, valor in diccionario.items():
    print(clave, valor)
