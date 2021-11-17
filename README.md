# Solvoku

---

Solvoku es un ejercicio realizado con el lenguaje de programacion python siguiendo los principios de SOLID. Su funcion funcion es mediante modulos , comprobar que una matriz , sea un sudoku correcto.

## Modulos

Lo hemos separado en 5 modulos para separar las resposabilidades y segir la "S" de SOLID, Single responsabilty.
Los modulos por separado para comprobar el sudoku son:

- check_cuadrado
- check_columnas
- check_filas
- check_sudoku
- check enteros

### Check_cuadrado

Comprueba que sea un cuadrado, es decir, que tenga la misma cantidad de alto de de ancho. Ya que un sudoku siempre tiene que tenerla mismo rango de numeros.

### Check_columnas

Este modulo Ya empieza a comprobar si lo escrito en el sudoku esta bien hecho. Comprueba que no se repita ningun numero en la columna.

### Check_fila

Este modulo comprueba que no se repita ningun numero en la misma fila.

### Check_sudoku

Este modulo comprueba que no en el sudoku haya el mismo rango de numeros, es decir , que si es 3x3 no haya un 9.

### Check enteros

Este modulo comprueba que no haya decimales dentro del sudoku.

## Solvoku

Solvoku ya es el programa con todos los modulos unidos que comprueba que el sudoku este bien realizado.

## caso_test_solvoku

Aqui se han preparado los casos test sobre los que se han realizado las pruebas para comprobar si el solvoku y sus modulos estan bien realizadso.

---

Espero que este ejercicio sea de ayuda para comprender un poco más el lenguaje de python, a mi me ayudo a entender mejor las listas de python y trabajar sobre ellas. En este perfil se iran subiendo actividades que se vayan realizando y proyectos, Que tenga un buen día.
