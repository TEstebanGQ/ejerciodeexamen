h1 = 0
h2 = 0
h3 = 0
h4 = 0
milisegundos = 0
h1 = int(input('Digite dias: '))
h2 = int(input('Digite horas: '))
h3 = int(input('Digite minutos: '))
h4 = int(input('Digite segundos: '))
milisegundos = (h1 * 2460601000) + (h2 *60601000) + (h3 * 601000) + (h4 * 1000)
print(f'Los milisegundos son: {milisegundos}')