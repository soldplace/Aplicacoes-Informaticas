def calcularDivisores(numero, inicio, fim):
    divisores = []
    print(numero, inicio, fim)
    for i in range(inicio, fim + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores
a = int(input('Inserir um numero: '))
b = int(input('Inserir o início do intervalo: '))
c = int(input('Inserir o fim do intervalo: '))
print(calcularDivisores(a, b, c))