print("La secuencia de Fibonacci es: ")
fibonacci1 = 0
fibonacci2 = 1
print(fibonacci1)
print(fibonacci2)
for i in range(fibonacci2,9):
    result = fibonacci1 + fibonacci2
    print(result)
    fibonacci1 = fibonacci2
    fibonacci2 = result
