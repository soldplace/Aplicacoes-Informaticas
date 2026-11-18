def dobro(num):
    return num * 2

def soma(num1, num2):
    return num1 + num2

def comparar(num1, num2):
    if num1 == num2:
        return True
    else:
        return False

numero1 = int(input('Primeiro valor: '))
numero2 = int(input('Segundo valor: '))

print("Dobro do 1º valor: ", dobro(numero1))
print("Dobro do 2º valoer: ", dobro(numero2))
print("Soma dos valores: ", soma(numero1, numero2))

if comparar(numero1, numero2):
    print("Os números introduzidos são iguais")
else:
    print("Os números introduzidos são diferentes")