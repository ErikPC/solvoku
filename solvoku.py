from src.check_cuadrado import check_cuadrado
from src.check_columnas import check_columnas
from src.check_filas import check_filas
from src.check_sudoku import check_sudoku
from src.check_entero import check_entero
from test.caso_test_solvoku import *

def solvoku(sudoku):
    if not check_cuadrado(sudoku):
        return False
    if not check_columnas(sudoku):
        return False
    if not check_filas(sudoku):
        return False
    if not check_entero(sudoku):
        return False
    if not check_sudoku(sudoku):
        return False
    return True

if __name__ == "__main__":
	assert solvoku(correct) == True
	assert solvoku(incorrect) == False
	assert solvoku(incorrect1) == False
	assert solvoku(incorrect2) == False
	assert solvoku(incorrect3) == False
	assert solvoku(incorrect4) == False
	assert solvoku(incorrect5) == False
	assert solvoku(irregular) == False
	assert solvoku(irregular2) == False