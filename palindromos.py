palabra1 = str(input("Escribe algo a ver si es un palíndromo: "))
palabra1 = palabra1.replace(" ", "")
palabra1 = palabra1.lower()

palabra2 = palabra1[::-1]

if palabra1 == palabra2:
    print("Es un palíndromo!")
else:
    print("No es un palíndromo")