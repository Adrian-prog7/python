from msilib.schema import Media
from statistics import median, median_grouped, median_high, median_low


cadenaejemplo = "en un lugar de la mancha..."
#primera en mayus
print(cadenaejemplo.capitalize())
#mayus y minus
print(cadenaejemplo.upper())

print(cadenaejemplo.lower())

#boolean
print(cadenaejemplo.isalnum())#alfanumerico

print(cadenaejemplo.isalpha())#solo alfa

print(cadenaejemplo.isdigit())#digitos

print(cadenaejemplo.islower())#solo minusculas

print(cadenaejemplo.isupper())#solo mayusculas

print(len(cadenaejemplo))
#espacios derecha izq y todos
print(cadenaejemplo.lstrip())

print(cadenaejemplo.rstrip())

print(cadenaejemplo.strip())



nombres=["adrian","juan","jesus","andres"]

lista2=[]
#meter en una lista
lista2.append("hola")
lista2.append("ixaoi")
lista2.append("holawdui")
lista2.insert(2,"hola")
print(lista2)

#listar una lista o los elementos de una palabra
lista3=list(nombres)
print(lista3)

#concatenar
lista3.extend(nombres)
print(lista3)

#un elemento esta en una lista
if "adrian" in nombres:
    print("el elemento es")
print(min(nombres))

numeros=[76,12,4,3,314]
print(max(numeros))
print(min(numeros))
print(median(numeros))
print((numeros))
