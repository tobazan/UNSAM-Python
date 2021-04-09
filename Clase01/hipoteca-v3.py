# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

pago_extra = 1000
comienzo_extra = 60
fin_extra = 107

meses = 0

while saldo > 0:
    saldo = saldo * (1+tasa/12)
    
    if comienzo_extra <= meses <= fin_extra:
    	saldo = saldo - pago_mensual - pago_extra
    	total_pagado = total_pagado + pago_mensual + pago_extra
    	meses += 1
    
    else:
    	saldo = saldo - pago_mensual
    	total_pagado = total_pagado + pago_mensual
    	meses += 1

    print(round(total_pagado, 2), saldo)

print(f'Total Pagado: {round(total_pagado, 2)}')
print(f'Mese: {meses}')