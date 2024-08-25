def main():
    print("Hola mundo")
    return 0

def factorial(numero: int):
    if numero <= 1: 
        return 1
    return numero * factorial(numero -1)
