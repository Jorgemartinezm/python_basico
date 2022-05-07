# palabra1 = str(input("Escribe algo a ver si es un palíndromo: "))
# palabra1 = palabra1.replace(" ", "")
# palabra1 = palabra1.lower()

# palabra2 = palabra1[::-1]

# if palabra1 == palabra2:
#     print("Es un palíndromo!")
# else:
#     print("No es un palíndromo")

def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[ ::-1]
    if palabra == palabra_invertida:
        return True
    else:
        False
       
        
def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palíndromo')
    else:
        print('No es palíndromo')


if __name__ == '__main__':
    run()