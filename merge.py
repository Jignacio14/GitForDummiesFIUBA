def main(): 
    print("Hola mundo")
    return 0

def for_dinamico(n: int):
    for i in range(n): 
        print(n)

def imprimirCosasRandom():
    print("Quiero crear un conflicto")

def factorial(n: int):
    if n <= 0 or n == 1:
        return 1
    return n * factorial(n - 1)
