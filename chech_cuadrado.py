from caso_test_solvoku import *

def check_cuadrado(sudoku):
    for lista in sudoku:
        if len(lista) != len(sudoku):
            return False
    return True
   
if __name__ == '__main__':
    # assert check_cuadrado(correct) == True
    # assert check_cuadrado(incorrect) == False
    # assert check_cuadrado(incorrect1) == False
    # assert check_cuadrado(incorrect2) == False
    # assert check_cuadrado(incorrect3) == False
    # assert check_cuadrado(incorrect4) == False
    # assert check_cuadrado(incorrect5) == False
    assert check_cuadrado(irregular) == False
    assert check_cuadrado(irregular2) == False