# Programa realizado por: Adrian Camero Esteban
# Fecha de entrega:24/10/2022
#______________________________________________________________________________________________________
#|                                  Explicación:                                                       |
#|_____________________________________________________________________________________________________|
#|1. No reciba parámetros                                                                              |
#2. Pregunte un password.                                                                              |
#3. Elimine los espacios en blanco antes y después.                                                    |
#4. Longitud mínima 12 caracteres.                                                                     |
#5. Debe contener, al menos, una minúscula.                                                            |
#6. Debe contener, al menos, una mayúscula.                                                            |
#7. Debe contener, al menos, un número.                                                                |
#8. Debe contener, al menos, uno de los siguientes signos = + - *                                      |
#9. Si no cumple todo lo anterior vuelve a preguntar                                                   |
#10. Devuelve la cadena correcta                                                                       | 
#|_____________________________________________________________________________________________________|


from pickle import TRUE


def password():
    p=input("Introduce una contraseña: ")
    p1=input("Introduce de nuevo la contraseña: ")
    p.lstrip()
    p.rstrip()
    p1.lstrip()
    p1.rstrip()
    if p!=p1:
        print("las contraseñas no coinciden")
        password()
    if len(p)<12:
        print("La contraseña no contiene al menos 12 caracteres")
        password()
    validar=False
    espacio=True  #variable para identificar espacios
    mayuscula=False #variable para identificar letras mayúsculas
    minuscula=False #variable para contar identificar letras minúsculas
    numeros=False #variable para identificar números
    correcto=True

   
    for carac in p: #ciclo for que recorre caracter por caracter en la contraseña

        if carac.isspace()==True: #Saber si el caracter es un espacio
            espacio=False #si encuentra un espacio se cambia el valor 
                
        if carac.isupper()== True: #saber si hay mayuscula
            mayuscula=True #acumulador o contador de mayusculas
                
        if carac.islower()== True: #saber si hay minúsculas
            minuscula=True #acumulador o contador de minúsculas
               
        if carac.isdigit()== True: #saber si hay números
            numeros=True #acumulador o contador de numeros
                
            
    if mayuscula == True and minuscula ==True and numeros == True  and espacio ==True:
        validar = True #Cumple el requisito de tener mayuscula, minuscula, numeros y no alfanuméricos
    else:
        correcto=False #uno o mas requisitos de mayuscula, minuscula, numeros y no alfanuméricos no se cumple
           
    if validar == True and correcto==False:
        print("La contraseña elegida no es segura: debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico")

    if validar == True and correcto ==True:
        print("la contraseña es valida")
    
    
password()



