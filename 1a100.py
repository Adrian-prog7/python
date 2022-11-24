# Programa realizado por: Adrian Camero Esteban
# Fecha de entrega:24/10/2022
#______________________________________________________________________________________________________
#|                                  Explicación:                                                       |
#|_____________________________________________________________________________________________________|
#| Hacer un pseudocódigo que imprima los números del 1 al 100.                                         |
#|Que calcule la suma de todos los números pares por un lado, y por otro, la de todos los impares.     |
#|_____________________________________________________________________________________________________|

print("--------------------------------")
print("|    Numeros del 1 al 100      |")
print("--------------------------------")
#inicializamos variables
a = 1
acumula_pares=0
acumula_impares=0
suma_pares=0
suma_impares=0
suma_total=0
#Con un bucle while imprimimos.Contabilizamos y sumamos pares e impares con if-else 
while a <= 100:
    print(a)
    suma_total=suma_total+a
    if a % 2 ==0 :
        acumula_pares +=1
        suma_pares=suma_pares+a
    elif a % 2 ==1:
        acumula_impares +=1
        suma_impares=suma_impares+a
    a = a + 1
#Imprimimos los resultados por consola
print(f" ________________________________________________________")
print(f"| Cantidad de numeros PARES ==> {acumula_pares}                       |")
print(f"| Cantidad de numeros IMPARES ==> {acumula_impares}                     |")
print(f"|________________________________________________________|")
print(f"| La suma de esos numeros PARES es ==> {suma_pares}              |")
print(f"| La suma de esos numeros IMPARES es ==> {suma_impares}            |")
print(f"| La suma TOTAL de los numeros de 1 al 100 es ==> {suma_total}   |")
print(f"|________________________________________________________|")
