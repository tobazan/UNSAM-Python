# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

pago_extra = 1000
meses = 0

while saldo > 0:
    saldo = saldo * (1+tasa/12)
    
    if meses < 12:
    	saldo = saldo - pago_mensual - pago_extra
    	total_pagado = total_pagado + pago_mensual + pago_extra
    	meses += 1
    
    else:
    	saldo = saldo - pago_mensual
    	total_pagado = total_pagado + pago_mensual
    	meses += 1

    print(f'Mes: {meses} - Total pagado {round(total_pagado, 2)}')