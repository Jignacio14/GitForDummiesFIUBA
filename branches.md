# Branches

Bueno, aca probablemente nos pongamos un poco mas teoricos. Es hora de explicar para que sirven las branches de git. 

Supongamos que Alan y Barbara trabajan en equipo para hacer un TP de fiuba. Alan crea el repo y se lo pasa a Barbara y apartir de ese momento empiezan a trabajar sin ningun tipo de cordinacion ni a hablarse entre ellos, como ya sabran esto terminara en desastre y mas tarde explicare que pasara, obviando la desorganizacion entre los dos miembros del equipo. 

En el siguiente TP Alan y Barbara saben muy bien como tienen que comenzar porque ahora si saben que son las branches ! y que por no usarlas la lleva al caos mismo. 

Una branch en git es es una linea de tiempo donde evoluciona un proyecto ! Con esto en mente veamos como crear una branch local.

## Crear una branch

            git branch <nombre-rama>

La branch resultante sera una una linea de linea de trabajo que considere los cambios realizados hasta ese momento en la rama sobre la cual estan "parados", entonces por ejemplo, si crear una rama a partir de main en este momento, podran subir cambios a este repo considerando solo el estado actual en el que esta la rama main 

### Nombrando una rama 

Para nombrar una rama lo mejor es hacer lo siguiente: <nombre de la feature> + "-" + <sus iniciales> 

Si tienen que construir la clase personaje entonces la rama seria: personaje-jc

### Que otras ramas hay en mi pc ?

Facil, utilicen el comando git branch para ver todas las ramas locales que tienen en su pc, si crean la rama desde github deben hacer pull antes para poder verla de manera local

### Como cambio entre ramas ? 

Y bueno ya lo saben, lo vienen haciendo hace rato !! 

            git switch <nombre de la rama>

Esto lo pueden hacer siempre y cuando no tengan cambios que commitear, de resto este comando les permite saltar entre cambiar entre ramas sin ningun problema ! 

### Ya no estoy usando una rama! 

Para borrar una rama tienen el siguiente comando:

            git branch -d <nombre de rama>

Si tienen quilombos de algo:

            git branch -D <nombre rama>

Si siguien teniendo quilombos 

[AyudaDocente;)](https://chat.openai.com/)
