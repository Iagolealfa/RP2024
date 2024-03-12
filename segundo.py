def fibonacci(number):
    a, b = 0, 1
    while a <= number:
        if a == number:
            return True
        a, b = b, a + b
    return False

number = int(input("Digite um numero: "))

if fibonacci(number):
    print(f"{number} pertence à sequência de Fibonacci.")
else:
    print(f"{number} não pertence à sequência de Fibonacci.")
