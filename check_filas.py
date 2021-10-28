from caso_test_solvoku import *

def check_filas(sudoku):
	for lista in sudoku:
		for numero in lista:
			if lista.count(numero) > 1:
				return False
	return True

if __name__ == '__main__':
    assert check_filas(correct) == True
    assert check_filas(incorrect) == False
    assert check_filas(incorrect1) == True
    assert check_filas(incorrect2) == False 
    assert check_filas(incorrect3) == True
    assert check_filas(incorrect4) == True
    assert check_filas(incorrect5) == True
    assert check_filas(irregular) == True
    assert check_filas(irregular2) == True