lettersDni = ('T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E')
user1 = {"nombre":"Pedro Javier Morales",  "direccion": "Flores 36 8o 2o", "tfn":["+0034345345345"],"compras":[1234,423,23]}
user2 = {"nombre":"Maite Lopez Miravet", "direccion":"Balmes 31 1o 2o","tfn":["+0034234234235","+0034239999235"],"compras":[12344]}
user3 = {"nombre":"Marta Garcia Suarez",  "direccion":"Valencia 21 3o 1o","tfn": ["+0075766576575"],"compras":[34,423,23,6]}
users = {"47474747X":user1,"24536425T":user2,"76767676H":user3}
menu = "*" * 90 + "\n{:10}{:25}{:25}{:15}{:>15}\n".format("DNI", "Nombre", "Direccion", "Tfn","Total Compras") + "*" * 90 + "\n"
data = ""
for dni in users:
    totalb = 0
    name = users[dni]["nombre"]
    address = users[dni]["direccion"]
    buy_list = users[dni]["compras"]
    for buy in buy_list:
        totalb = totalb + buy
    tfns = users[dni]["tfn"]
    for i in range(len(tfns)):
        if i == 0:
            data = data + "{:10}{:25}{:25}{:15}{:>15}\n".format(dni, name, address, tfns[i], totalb)
        else:
            data = data + "{:60}{:15}\n".format("",tfns[i])
    data = data + "-" * 90 + "\n"
print(menu + data)