# Explicacion breve

No explicare en detalle que es git pero si puedo darles una idea basica de lo que es. Saben que es una pelicula en stop motion? Pues git es una herramienta que permite que nuestro proyecto sea como una de esas peliculas. El proyecto (nuestro codigo) se compone de muchas fotitos pequeñas que almacenan el estado en ese momento de como habiamos progresado. Esta fotito se llama `commit` y para poder generarlo debemos primero saber un par de cosas 

# Paso 1 

Entra en el archivo punto .py y completa el programa supremo que nos garantiza aprender todo lenguaje. Nuestro poderoso "Hola mundo!". 

Una vez completes el string a imprimir utiliza el siguiente comandos 

```
git status
```

## Git status

Git status nos muestra en un principio cuales son las actualizaciones que realizamos respecto el ultimo cambio. Ojo! estas actualizaciones no estan subidas aun en el repo y en caso de querer revertir los cambios lo podriamos hacer de manera sencilla. Observa que git es bastante descriptivo con lo que ocurrio, el estado de `primer-archivo.py` estara modificado y aparecera en color rojo.

Lee atentamente todo lo que muestra git, fijate que tira opciones copadas, add para agregar tus archivos y restore, para restaurarlos (valga la redundancia). Es hora de realizar nuestra primera tarea. 

## Git add 

Sigamos las recomendaciones de git y utilicemos el siguiente comando ! 

```
git add
```

***IMPORTANTE***

Aca podes hacer dos cosas, pero en proyectos mas grandes es importante que sepas esto !

```
git add .
```

Agrega todos los archivos que estan en estado modifeid (en este caso nuestro unico archivo). Por otro lado 

```
git add <nombre-del-archivo>
```

Agregaria los cambios del nombre del archivo que estas seleccionado siempre y cuando tengas algun cambio !! 

## Git commit 

Hace git status de vuelta y fijate que nuestro archivo modificado pasa ahora a estar en color verde. Esto es denomidado como: "staged", eso significa que nuestros cambios, de manera local, han sido seleccionados para subir al repo. Volviendo a la anecdota anterior es como que tomaste una fotito para un nuevo frame de la pelicula ! 

Como es el ultimo cambio digamos que nos podemos arrepentir y echarlo para atras, alli es donde entra `restore`, pero no entremos en detalles y sigamos con nuestro perfecto "hola mundo" el cual queremos mandar al repo. Para eso usaremos el comando 

```
git commit
```

(Tarea): busquen en google como cambiar de editor de texto para que git commit abra otro editor que no sea el notepad o vim (eso si no saben usar vim)

Git commit es decidir que esos cambios iran al repo y esto es inmutable, no se puede echar para atras o cambiar, una vez que finalice el commit esos cambios se iran en el. Los pueden revertir pero seria agregar otro commit cambiando las cosas; por ahora, eso no importa. 

Una vez tengan el commit hecho al cual le tienen que agregar un mensaje descriptivo (siguiente seccion) podemos realizar el envio de los cambios al repo.

## Git push 

WARINING: no hagan git push en este repo ! (please)

Cuando su commit este listo y quieran mandar las cosas al repo, o incluso tengan varios commits locales los cuales quieren enviar, deben utilizar el siguiente comando: 

```        
git commit
```

WARINING2: Pueden usar `git commit -m <mensaje>`. Un ejemplo de esto seria:

```
git commit -m "Agrego los nuevos cambios"
```

Lo cual funciona de la misma manera que git commit pero esto incita a malas practicas. En fin. Vuelvan a confiar en mi y hagan

```
git switch 02-buenos-commits
```

