"""Python nos permite controlar las excepciones usando:
   try/except
"""

print("Inicio de operación...")


num1 = input("ingrese un número")

num2 = int(input("ingrese un segundo número"))

try:
    print(num1/num2)
except ZeroDivisionError:
    print("¡ No se puede dividir por cero ! Vuelva a intentarlo")
    #print(f"El ERROR fue:{e}")
except TypeError:
    print("Ocurrio un error inesperado en la operación")
except Exception as e:
    print("Ocurrio un error")


print("Programa finalizado")