'''
import random
# Lista vacía
componentes = []

elementos = input("ingrese un componente del avion: ")
componentes.append(elementos)
print(componentes)
numeros = []
aleatorio = random.randint(0,100)
numeros.append(aleatorio)
numeros.append(10)
for i in range(10):
    aleatorio = random.randint(0,100)
    numeros.append(aleatorio)
print(numeros)
'''
'''

# Lista con elementos
componentes = ["alas", "fuselaje", "motores", "tren de aterrizaje"]
print(componentes[0])
print(componentes[-1])

print(componentes[1:3])
print(componentes[:2])
print(componentes[2:])
'''
'''
# Lista de componentes con sus masas (kg) y posiciones (m)
componentes = ["motor izquierdo", "motor derecho", "fuselaje", "ala izquierda", "ala derecha", "cola"]
masas = [1200, 1200, 5000, 800, 800, 600]
posiciones_x = [2, 2, 0, -2, 2, -6]

# Cálculo del centro de masa en eje X sin list comprehensions
masa_total = 0
momento_total = 0

for i in range(len(masas)):
    masa_total += masas[i]
    momento_total += masas[i] * posiciones_x[i]

centro_masa_x = momento_total / masa_total

print(f"Centro de masa en eje X: {centro_masa_x:.2f} m")
'''

'''
import random
# Lista vacía

numeros = []
for i in range(100):
    aleatorio = random.randint(100,1000)
    numeros.append(aleatorio)
print(numeros)

suma = 0
for i in range(len(numeros)):
    suma += numeros[i]
prom = suma / len(numeros)
print(f"promedio = {prom}")

mayor = max(numeros)
menor = min(numeros)
print(f"mayor = {mayor}")
print(f"menor = {menor}")
'''