# programa en python.Dadas 3 variables que representan, total hipoteca,
# interés, aportación inicial, años de hipoteca. simule los pagos mensuales,
# cuanto se paga de intereses y cuanto se amortiza cada mes del total
# pedido en la hipoteca ( total hipoteca - aportación inicial ).
#
# total_vivienda: precio/importe total de la hipoteca.
# interes_anual: interés anual, por ejemplo 3.5 para un 3,5 %.
# aportacion_inicial: dinero aportado inicialmente.
# años: duración de la hipoteca.
# El capital realmente financiado será:
#
# total_vivienda - aportacion_inicial
#
# Suponemos que todas las cuotas son iguales

# total_vivienda = input("Dame el total de la hipoteca: ")
# while not total_vivienda.isdigit():
#     print("Escribe un valor númerico")
#     total_vivienda = input("Dame el total de la hipoteca: ")
# else:
#     total_vivienda = float(total_vivienda)
# aportacion_inicial = input("Dame la aportación inicial: ")
# while not aportacion_inicial.isdigit():
#     print("Escribe un valor númerico")
#     aportacion_inicial = input("Dame la aportación inicial: ")
# else:
#     aportacion_inicial = float(aportacion_inicial)
# # interes = input("Dame el interes: ")
# # while not interes.isdigit():
# #     print("Escribe un valor númerico")
# #     interes = input("Dame el interes: ")
# # else:
# #     interes = float(interes)
# longhipoteca = input("Dame la duración de la hipoteca: ")
# while not longhipoteca.isdigit():
#     print("Escribe un valor númerico")
#     longhipoteca = input("Dame la duración de la hipoteca: ")
# else:
#     longhipoteca = int(longhipoteca)

# temporal
total_vivienda = 250000
aportacion_inicial = 70000
longhipoteca = 15
tin = 3.5

capital_inicial = total_vivienda - aportacion_inicial
numcuotas = longhipoteca * 12
interes = (tin / 100) / 12
cuota = capital_inicial * (interes / (1 - (1 + interes) ** -numcuotas))
mes = 1
saldo = capital_inicial
total_cuotas = 0
total_interes = 0
total_amortizado = 0

menu = "\n" + "=" * 80 + "\n" + "SIMULACIÓN DE HIPOTECA" + "\n" + "=" * 80 + "\n" + \
       "{:24}{:,.2f} €\n".format("Precio total:", total_vivienda) + \
       "{:24}{:,.2f} €\n".format("Aportación inicial:", aportacion_inicial) + \
       "{:24}{:,.2f} €\n".format("Capital hipotecado:", capital_inicial) + \
       "{:24}{:.2f} %\n".format("Interés anual:", tin) + \
       "{:24}{} años\n".format("Duración:", longhipoteca) + \
       "{:24}{}\n".format("Número de cuotas:", numcuotas) + \
       "{:24}{:,.2f} €\n\n".format("Cuota mensual::", cuota)

body = "-" * 80 + "\n" + \
       "{:>5}{:>15}{:>15}{:>20}{:>20}\n".format("Mes", "Cuota", "Intereses", "Amortización", "Saldo Pendiente") + \
       "-" * 80 + "\n"
for i in range(0, 180):
    intereses = saldo * interes
    amortizacion = cuota - intereses
    saldo = saldo - amortizacion
    body = body + "{:5}{:15,.2f}{:15,.2f}{:20,.2f}{:20,.2f}\n".format(mes, cuota, intereses, amortizacion, saldo)
    mes = mes + 1
    total_cuotas = total_cuotas + cuota
    total_interes = total_interes + intereses
    total_amortizado = total_amortizado + amortizacion
footer = "-" * 80 + "\n" + "{:24}{:,.2f} €\n".format("Total pagado en cuotas:", total_cuotas) + \
         "{:24}{:,.2f} €\n".format("Total de intereses:", total_interes) + \
         "{:24}{:,.2f} €\n".format("Total amortizado:", total_amortizado) + \
         "{:24}{:,.2f} €".format("Capital inicial:", capital_inicial)

print(menu + body + footer)
