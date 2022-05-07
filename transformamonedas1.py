def datos_moneda(valor):
    dolar = input('Elija la cantidad deseada: ')
    dolar = float(dolar)
    moneda = valor
    resultado = dolar / moneda
    resultado = round(resultado, 2)
    resultado = str(resultado)
    print('Tienes ', resultado, 'dolares')

menu = """
Bienvenido al conversor de monedas

1 - Euros
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = input(menu)
if opcion == '1':
    datos_moneda(1.06)

elif opcion == '2':
    datos_moneda(95)
    
elif opcion == '3':
    datos_moneda(24)

else:
      print("Elige una opción válida")








