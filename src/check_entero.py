from ..test.caso_test_solvoku import *

def check_entero(sudoku):
    for fila in sudoku:
        for numero in fila:
            # comprueba si numero es un entero.
            if not isinstance(numero, int):
                return False
    return True


if __name__ == '__main__':
    assert check_entero(correct) == True
    assert check_entero(incorrect) == True
    assert check_entero(incorrect1) == True
    assert check_entero(incorrect2) == True
    assert check_entero(incorrect3) == True
    assert check_entero(incorrect4) == False
    assert check_entero(incorrect5) == False
    assert check_entero(irregular) == True
    assert check_entero(irregular2) == True