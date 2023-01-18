print("           **** BIENVENIDO A LA CALCULADORA DE PROPINAS ****".center(30))
print()
valor_a_pagar = int(input("Ingrese el valor total de la factura: $"))
porcentaje_propina = int(input("Ingrese el porcentaje de propina que quieres dar, (5%, 10%, 15%, o el que quieras): "))
compartir_factura = int(input("Ingrese entre cuantas personas quieres dividir el pago?: "))
resultado1 = (valor_a_pagar / compartir_factura)
resultado2 = resultado1 * porcentaje_propina / 100
calculo_final = round(resultado2 + resultado1)

print(f"el valor a pagar entre {compartir_factura} es de: ${calculo_final} pesos por cada persona")

