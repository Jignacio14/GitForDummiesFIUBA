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
    Un conflicto les muestra sobre un archivo las coliciones que existen entre el codigo de Alan y Barbara. Barbara en algun momento habra enviado dos funciones al repo llamadas `for_dinamico` y `imprimirCosasRandom` en el momento que Alan realiza el merge todo se complica y debe solucionarlo

### Como solucionar un merge ?

Y bueno deben leer y entender que fue lo que paso en el merge. Vean con atencion que hay dos segmentos 

        ```python
            
            <<<HEAD 
                <Codigo de barbara>
            =======
                <Codigo de alan>
            >>> <Nombre de la rama de alan>
        ```
- El segmento <<<< HEAD es el que contiene los cambios que estan almacenados en el repo
- El segmento >>> <Nombre rama> son los cambios que tenemos de manera local y queremos agregar 

Tenemos 3 cosas por hacer para solucionar el codigo:

- Elimina la porcion del codigo head de barbara que no sirve de nada y que actualizamos de forma local
- Elimina tu codigo que quedo viejo en comparacion a los cambios que ingreso barbara y son una mejora en esa feature
- Combina los dos !! Si tanto el codigo de Alan como el de Barbara es el que debe quedar finalmente en el repo pues te toca mezclar el codigo

## Tarea

Tomen el codigo anterior en python y solicionen el conflicto a mano en algun editor de texto cualquiera !

[Una solucion al conflicto](https://github.com/Jignacio14/GitForDummiesFIUBA/blob/05-git-merge-destino-con-merge/merge.py)

Vean solo la solucion una vez hayan hecho algo !!! No sirve de nada que vean la respuesta, de lo contrario no se curtiran !

## Pull request 

Un pull request es una peticion para agregar codigo entre ramas, no es lo mismo que el merge, pero incluye los merges. La idea de esto es que vos mandes el codigo de tu rama a la rama de integracion o como mas te guste y le pidas a tu equipo que apruebe los cambios, asi, podes evaluar, corregir y mejorar el codigo de manera colaborativa. 

Antes de mandar un pull request a una rama cualquiera TENES que hacer un merge local, porque si tiene conflictos, estas mandando cualquiera !!!! 

Por eso es muy importante que te aprendas de memoria el algoritmo para realizar merges, si se te olvida, veni a este repo, no pasa nada, cuando lo hagas 3-4 veces te lo aprendes de memoria y te sale automatico !

### Mas sobre pull request

Ve a github y anda a la rama de pull request, observa los dos ejemplos de pull request ! 

NOTA: disculpen que me hice quilombo con el nombre de las ramas. 


