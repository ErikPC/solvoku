from check_cuadrado import check_cuadrado
from check_columnas import check_columnas
from check_filas import check_filas
from check_sudoku import check_sudoku
from check_entero import check_entero
from caso_test_solvoku import *

def solvoku(sudoku):
	# if not check_cuadrado(sudoku):
	# 	return False
	# if not check_columnas(sudoku):
	# 	return False
	# if not check_filas(sudoku):
	# 	return False
	# if not check_entero(sudoku):
	# 	return False
	# if not check_sudoku(sudoku):
	# 	return False
	# return True

	# Si hay False en la tupla, 'in' devuelve True, y lo negamos y devolvemos False
	# Si no hay False en la tupla, 'in' devuelve False, y lo negamos y devolvemos True
	return not False in (check_cuadrado(sudoku), 
						 check_columnas(sudoku),
						 check_filas(sudoku),
						 check_entero(sudoku),
						 check_sudoku(sudoku))

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