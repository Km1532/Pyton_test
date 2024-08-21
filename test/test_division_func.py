from leeson17 import  division
import pytest

@pytest.mark.parametrize("a, b, expcted_result", [(10 , 2 ,5),
                                                 (10, 20 , 2),
                                                 (30, -3, -10),
                                                 (5, 2, 2.5)])

def test_division_good(a, b, expcted_result):
    assert division(10, 2) == 5

def test_division_with_error():
    with pytest.raises(ZeroDivisionError):
        division(10, 0)


#def test_type_error():
    #with pytest.raises(TypeError):
        #division(10, "2")