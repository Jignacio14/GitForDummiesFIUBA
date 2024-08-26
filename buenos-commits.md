# Commits de calidad 

Cuando tengan un proyecto gigante la calidad de los commits es esencial, como decia, es una fotito. Si ustedes agregan un commit que representa 1234142123131 acciones en la pelicula de stop motion basicamente acabamos de destruir la pelicula, en este caso, destruimos la organizacion con la que venimos trabajando. Desde github abran la parte de commits y fijense como hago la carga de cambios y como agrego dise;o incremental (poco a poco) de funciones muy sencillas, que en caso de ser un proyecto gigante y mandase toda una feature en un solo commit nos estariamos arriesgando


## Por que insisto tanto ??

Asuman que tengo un proyecto con pruebas automaticas y estamos trabajando dos personas sobre el mismos. Si Luca mete un commit en donde cambia 180 archivos, hace 300000 inserciones y 1234123 eliminaciones; y se da el caso que las pruebas dejan de automaticas o el funcionamiento general de la aplicacion/proyecto falla, la unica seguridad que tendriamos es que Luca metio la pata... pero no sabriamos donde empezar a buscar, son un monton de cambios... ahora si luca fue subiendo cosas poco a poco, se puede ir buscando entre sus commits donde empezo el caos y esto nos facilita la vida 

(Tarea): Leer sobre git bisect 

### Paso 2 

Abran los commits y leanlos 

Nota: Por comodidad pueden leer los commits desde github, si lo quieren hacer "tryhard", desde su computadora pueden usar el comando git log (para salir del log presionen q)

Despues de leerlos en github mismo cambien de rama a `03-malos-commits` y vean que no estoy dandole ninguna informacion a mis compa;eros de lo que estoy haciendo en cada paso 
