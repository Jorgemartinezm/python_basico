dolar = input('''¡¡¡Bienvenido al transformamonedas!!!
      Ahora puede pasar de euro a dólares
      Elija la cantidad deseada: ''')

dolar = float(dolar)
euro = 0.94
resultado = dolar / euro
resultado = str(resultado)

print('Tienes ', resultado, 'euros')