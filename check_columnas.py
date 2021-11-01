from caso_test_solvoku import *

def check_columnas(sudoku):
    longitud = len(sudoku)
    for i in range(longitud):
        # i es el index actual de la fila, j es el index actual de la columna.
        # añade a columna cada numero en el index actual de todas las filas.
        # entonces tenemos todos los index 0 de las filas almacenados en la columna.
        columna = [sudoku[j][i] for j in range(longitud) if longitud == len(sudoku[j])]
        for numero in columna:
            if columna.count(numero) > 1:
                return False
    return True


if __name__ == '__main__':
    assert check_columnas(correct) == True
    assert check_columnas(incorrect) == False
    assert check_columnas(incorrect1) == False
    assert check_columnas(incorrect2) == False
    assert check_columnas(incorrect3) == True
    assert check_columnas(incorrect4) == True
    assert check_columnas(incorrect5) == True
    assert check_columnas(irregular) == True
    assert check_columnas(irregular2) == True