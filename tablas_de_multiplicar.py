print("Hasta que numero deseas visualizar la tabla de multiplicar")
r = int(input())
matriz1 = [[str() for ind0 in range(r)] for ind1 in range(r)]
e = 1
while e<=r:
	t = 1
	while t<=r:
		multi = e*t
		print(multi," ", end="")
		t = t+1
	print("")
	e = e+1

