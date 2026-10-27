"""
programa que nos dice cuanto hemos de pagar de irpf según nuestros ingresos brutos
Tramos IRPF 2023                    Total
Desde 0 a 12.450€                    19%
Desde 12.450€ a 20.199€              24%
Desde 20.200€ a 35.200€              30%
Desde 35.200€ a 60.000€              37%
Desde 60.000€ a 300.000€             45%
Más de 300.000€                      47%
"""
gsalary = float(input("Digues el teus ingregos bruts: "))
irpf = 0

tramit1 = 12450 * 0.19
tramit2 = (20199 - 12450) * 0.24
tramit3 = (35200 - 20200) * 0.30
tramit4 = (60000 - 35200) * 0.37
tramit5 = (300000 - 60000) * 0.45

if gsalary < 12450:
    irpf = irpf + gsalary * 0.19
elif gsalary < 20199:
    irpf = irpf + tramit1 + (gsalary - 12450) * 0.24
elif gsalary < 35200:
    irpf = irpf + tramit1 + tramit2 + (gsalary - 20200) * 0.30
elif gsalary < 60000:
    irpf = irpf + tramit1 + tramit2 + tramit3 + (gsalary - 35200) * 0.37
elif gsalary < 300000:
    irpf = irpf + tramit1 + tramit2 + tramit3 + tramit4 + (gsalary - 60000) * 0.45
else:
    irpf = irpf + tramit1 + tramit2 + tramit3 + tramit4 + tramit5 + (gsalary - 300000) * 0.45
print(f"IRPF total a pagar: {irpf:.2f}€")