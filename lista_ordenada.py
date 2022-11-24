# Programa realizado por: Adrian Camero Esteban
# Fecha de entrega:24/10/2022
#______________________________________________________________________________________________________
#|                                  Explicación:                                                       |
#|_____________________________________________________________________________________________________|
#|Hacer un pseudocódigo que imprima el mayor y el menor de una serie de cinco números que vamos        | 
#|introduciendo por teclado.                                                                           |
#|_____________________________________________________________________________________________________|



print("--------------------------------")
print("|    Lista ordenada            |")
print("--------------------------------")
#Introducimos cada numero por consola
numero_1 = float(input("Escriba el primer numero: "))
numero_2 = float(input("Escriba el segundo número: "))
numero_3 = float(input("Escriba el tercer número: "))
numero_4 = float(input("Escriba el cuarto número: "))
numero_5 = float(input("Escriba el quinto número: "))
#Metemos los numeros en una lista y la imprimimos
numeros = [numero_1, numero_2, numero_3, numero_4, numero_5]
print(f"Esta es la lista de numeros dada por el usuario==> ",numeros)
print("_________________________________________________________________")
#Primer metodo con el sort para la ordenacion de la lista en ambos sentidos invirtiendo con "reserve=true"
ordenados_MenosMas = sorted(numeros)
ordenados_MasMenos= sorted(numeros,reverse=True)
#Imprimimos ambas listas ordenadas
print("Esta es la lista ordenada de menor a mayor==>",ordenados_MenosMas[0])
print("Esta es la lista ordenada de mayor a menor==>",ordenados_MasMenos[0])
#Segundo metodo comparar cada numero fuera de la lista por ello es que  hemos iniciado cada numero por separado
#y despues los hemos introducido en una lista para mostrar ambos metodos de ordenacion y comparar cual es mas eficaz
mayor=numero_1
menor=numero_1

if numero_2>mayor:
    mayor=numero_2
if numero_3>mayor:
    mayor=numero_3
if numero_4>mayor:
    mayor=numero_4
if numero_5>mayor:
    mayor=numero_5
print("El mayor es ",mayor)
if numero_2<menor:
    menor=numero_2
if numero_3<menor:
    menor=numero_3
if numero_4<menor:
    menor=numero_4
if numero_5<menor:
    menor=numero_5
print("El menor es: ",menor)





