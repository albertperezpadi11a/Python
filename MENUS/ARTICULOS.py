cabecera = "Lista de la Compra".center(40,"*") + "\n" + \
    "{:20}{:>10}{:>10}\n".format("Articulos","Cantidad","Precio") + \
    "*" * 40 + "\n"
lista = ""
#Primer articulo
articulo = input("Articulo: ")
cantidad = input("Cantidad: ")
precio = input("Precio: ")
precio = float(precio)
lista = lista + "{:20}{:>10}{:10.2f}\n".format(articulo, cantidad, precio)
print(cabecera + lista)
#Segundo articulo
articulo = input("Articulo: ")
cantidad = input("Cantidad: ")
precio = input("Precio: ")
precio = float(precio)
lista = lista + "{:20}{:>10}{:10.2f}\n".format(articulo, cantidad, precio)
print(cabecera + lista)