menu = """
Bienvenido al conversor de monedas

1 - Euros
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = input(menu)

if opcion == '1':
    dolar = input('Elija la cantidad deseada: ')
    dolar = float(dolar)
    euro = 0.94
    resultado = dolar / euro
    resultado = round(resultado, 2)
    resultado = str(resultado)
    print('Tienes ', resultado, 'euros')

elif opcion == '2':
    dolar = input('Elija la cantidad deseada: ')
    dolar = float(dolar)
    pargentino = 65
    resultado = dolar / pargentino
    resultado = round(resultado, 2)
    resultado = str(resultado)
    print('Tienes ', resultado, 'pesos argentinos')
    
elif opcion == '3':
    dolar = input('Elija la cantidad deseada: ')
    dolar = float(dolar)
    pmexicano = 24
    resultado = dolar / pmexicano
    resultado = round(resultado, 2)
    resultado = str(resultado)
    print('Tienes ', resultado, 'pesos mexicanos')

else:
      print("Elige una opción válida")








