def main():
    print("Hola mundo")
    return 0

def for_dinamico(n: int):
    for i in range(n): 
        print(n)



def factorial(numero: int):
    if numero <= 1: 
        return 1
    return numero * factorial(numero -1)
