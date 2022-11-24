print("CALCULAR EL IMC")
peso=float(input("¿Cuanto pesa?"))
altura=float(input("¿Cuanto mide en metros?"))
imc = float(peso/pow(altura,2))
print(f"Su imc es {imc} ")
if imc>20 :
    print("su imc es demasiado alto gordo")
elif imc<10:
    print("Su imc es demasiado bajo desnutrido")
else:
    print("su imc es perfecto siga asi")
