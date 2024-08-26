# Explicacion breve

No explicare en detalle que es git pero si puedo darles una idea básica de lo que es. Saben que es una película en stop motion? Pues git es una herramienta que permite que nuestro proyecto sea como una de esas películas. El proyecto (nuestro codigo) se compone de muchas fotitos pequeñas que almacenan el estado en ese momento de como habíamos progresado. Esta fotito se llama `commit` y para poder generarlo debemos primero saber un par de cosas 

# Paso 1 

Entra en el archivo punto .py y completa el programa supremo que nos garantiza aprender todo lenguaje. Nuestro poderoso "Hola mundo!". 

Una vez completes el string a imprimir utiliza el siguiente comandos 

```
git status
```

## Git status

Git status nos muestra cuales son las actualizaciones que realizamos respecto el último cambio. Ojo! estas actualizaciones no están subidas aun en el repo y en caso de querer revertir los cambios lo podríamos hacer de manera sencilla. Observa que git es bastante descriptivo con lo que ocurrió, el estado de `primer-archivo.py` estará modificado y aparecerá en color rojo.

Lee atentamente todo lo que muestra git, fijate que tira opciones copadas, add para agregar tus archivos y restore, para restaurarlos (valga la redundancia). Es hora de realizar nuestra primera tarea. 

## Git add 

Sigamos las recomendaciones de git y utilicemos el siguiente comando ! 

```
git add
```

***IMPORTANTE***

Acá podes hacer dos cosas, pero en proyectos mas grandes es importante que sepas esto !

```
git add .
```

Agrega todos los archivos que están en estado modified (en este caso nuestro único archivo). Por otro lado 

```
git add <nombre-del-archivo>
```

Agregaría los cambios del nombre del archivo que estas seleccionado siempre y cuando tengas algún cambio !! 

## Git commit 

Hace git status de vuelta y fijate que nuestro archivo modificado pasa ahora a estar en color verde. Esto es denominado como _staged_, eso significa que nuestros cambios, de manera local, han sido seleccionados para subir al repo. Volviendo a la anécdota anterior es como que tomaste una fotito para un nuevo frame de la película ! 

Como es el ultimo cambio digamos que nos podemos arrepentir y echarlo para atrás, allí es donde entra `restore`, pero no entremos en detalles y sigamos con nuestro perfecto "hola mundo" el cual queremos mandar al repo. Para eso usaremos el comando 

```
git commit
```

(Tarea): busquen en Google como cambiar de editor de texto para que git commit abra otro editor que no sea el notepad o vim (eso si no saben usar vim)

Git commit es decidir que esos cambios irán al repo y esto es inmutable, no se puede echar para atrás o cambiar, una vez que finalice el commit esos cambios se irán en él. Los pueden revertir pero seria agregar otro commit cambiando las cosas; por ahora, eso no importa. 

Una vez tengan el commit hecho al cual le tienen que agregar un mensaje descriptivo (siguiente sección) podemos realizar el envio de los cambios al repo.

### Aclaración

El hecho del color con el que aparecen los nombres de los archivos modificados al hacer `git status` tienen una razón de ser:

- <span style="color:red">Hay cambios en los archivos marcados pero que aún no fueron commiteados</span>
- <span style="color:green">Hay cambios en los archivos marcados y que fueron commiteados al repo.</span>

## Git push 

WARINING: no hagan git push en este repo ! (please) (de todas formas no poseen permisos para hacerlo pero no viene al caso ese detalle)

Cuando su commit este listo y quieran mandar las cosas al repo, o incluso tengan varios commits locales los cuales quieren enviar, deben utilizar el siguiente comando: 

```        
git commit
```

WARINING2: Pueden usar `git commit -m <mensaje>`. Un ejemplo de esto sería:

```
git commit -m "Agrego los nuevos cambios"
```

Lo cual funciona de la misma manera que git commit pero esto incita a malas practicas. En fin, Vuelvan a confiar en mi y hagan

```
git switch 02-buenos-commits
```

