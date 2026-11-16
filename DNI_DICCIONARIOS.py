lettersDni = ('T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E')
user1 = {"nombre":"Pedro Javier Morales",  "direccion": "Flores 36 8º 2º", "tfn":["+0034345345345"],"compras":[1234,423,23]}
user2 = {"nombre":"Maite Lopez Miravet", "direccion":"Balmes 31 1º 2º","tfn":["+0034234234235","+0034239999235"],"compras":[12344]}
user3 = {"nombre":"Marta Garcia Suarez",  "direccion":"Valencia 21 3º 1º","tfn": ["+0075766576575"],"compras":[34,423,23,6]}
users = {"47474747X":user1,"24536425T":user2,"76767676H":user3}
data = ""
for user in users:
    name = users[user]["nombre"]
    address = users[user]["direccion"]
    tfn = users[user]["tfn"]
    buy = users[user]["compras"]


