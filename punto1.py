

print("Programa Impares")
def contadorImpares():
	n=int(input("Introduzca un numero: "))
	for i in range(1,n+1):
		if i%2!=0:
			print(i)
contadorImpares()