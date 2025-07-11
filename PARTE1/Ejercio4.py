numero = 0
c1 = 0
c2 = 0
c3 = 0
suma = 0
num = int(input('Digite un numero de 3 digitos: '))
c1 = int(numero/100)
c2 = int(numero % 100 / 10)
c3 = numero % 10
suma = c1**3 + c2**3 + c3**3
print (f'numero registrado: {numero}')
print ('suma al cubo de sus digitos: {suma}')
print ('¿es numero armstrong?: ')
print ((suma == numero))