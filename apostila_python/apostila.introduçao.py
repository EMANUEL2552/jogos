def soma(a, b):
    return a+b
def imprime(a, b, foper):
    print(foper(a, b))

    imprime(5, 4, soma)

a = lambda x: x*2
print(a(3))
aumento = lambda a, b: (a*b/100)
aumento(100,5)
