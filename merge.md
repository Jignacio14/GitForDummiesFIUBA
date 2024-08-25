# Merge

Bueno llegamos al capitulo final de la primera version de git for dummies 

Como aprendimos en el capitulo anterior, necesitamos poder juntar los avances en el proyecto que hicieron tanto Alan como Barbara. Siguiendo un poco el modelo de ramas que les explique anteriormente digamos que alan quiere enviar sus cambios a la rama `integracion` para eso les voy a compartir el algoritmo TOP para realizar merges entre ramas y que nunca falle.

## Como hacer merges

Seamos Alan por 5 minutos 

1. git switch a la rama de integracion 
            git switch integracion 
2. queremos los cambios mas recientes de esta rama, por lo tanto vamos a hacer pull de todo lo que pueda haber en esa rama. Entonces:
            git pull
3. Ya tenemos los ultimos cambios que pudo haber enviado barbara al repo, ahora volvemos a nuestra rama:
            git switch <rama de alan>
4. Aca se viene lo picante y este es el comamndo al cual mas miedo le temen todos los novatos de git:
            git merge integracion
5. Pueden pasar dos cosas:
    5.1.  No tienen conflictos. Este es el escenario feliz, por lo tanto, una vez tengan todo listo hacen simplemente push (si solo push, los merge generan automaticamente un commit llamado merge)
    5.2 Si tienen conflictos se veran de la siguiente manera en local: 
        
    ```python
        def main(): 
            print("Hola mundo")
            return 0

        <<<<<<< HEAD
        def for_dinamico(n: int):
            for i in range(n): 
                print(n)

        def factorial(numero: int):
            if numero <= 1: 
        =======
        def imprimirCosasRandom():
            print("Quiero crear un conflicto")

        def factorial(n: int):
            if n <= 0 or n == 1:
        >>>>>>> 05-git-merge-origen
                return 1
            return n * factorial(n - 1)
    ```
