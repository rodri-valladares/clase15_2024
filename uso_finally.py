"""finally permite ejecutar código 
a pesar del resultado de los
bloques try/except
"""

print("Inicio de operación...")


num1 = int(input("ingrese un número"))


num2 = int(input("ingrese un segundo número"))

try:
    print(num1/num2)
except Exception as e:
    print("Ocurrio un error")
finally:
    print("Programa finalizado")


