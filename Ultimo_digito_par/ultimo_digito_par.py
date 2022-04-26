""""programa:
verificar si el eltimo digito de un numero es par"""

print("-------------------------------------------")
print("-------------------------------------------")
print("-------------ULTIMO DIGITO PAR-------------")
print("-------------------------------------------")
print("-------------------------------------------")

# input 
X = int(input("Digite el valor de X: "))


# procesing
r = X % 10 
if r % 2 == 0 : 
    msj = ("El ultimo digito es par")

print("El ultimo digito de " + str(X) + msj)