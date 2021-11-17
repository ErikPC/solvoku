from caso_test_solvoku import *

def check_sudoku(sudoku):
	numeros_sudoku=[]
	for fila in sudoku:
		# cojemos el contenido de una lista y lo concatenamos con otra
		numeros_sudoku+=fila
	for i in range(len(sudoku)):
		# comprueba que los numeros de la primera lista sean los mismos que la longitud
		if numeros_sudoku.count(sudoku[0][i]) != len(sudoku):
			return False
	return True


   
if __name__ == '__main__':
    assert check_sudoku(correct) == True
    assert check_sudoku(incorrect) == False
    assert check_sudoku(incorrect1) == True
    assert check_sudoku(incorrect2) == False 
    assert check_sudoku(incorrect3) == False 
    assert check_sudoku(incorrect4) == True
    assert check_sudoku(incorrect5) == True
    assert check_sudoku(irregular) == True
    assert check_sudoku(irregular2) == False