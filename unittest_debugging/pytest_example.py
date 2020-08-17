import pytest

def sum(num1 , num2):
    return num1 + num2 

@pytest.mark.test1
def test_uppercase():
    assert "foo".upper() == "FOO"

@pytest.mark.parametrize('num1, num2, expected',[(3,5,8),(-2,-2,-4), (-1,5,4), (3,-5,-2), (100,5,5)])
def test_sum(num1, num2, expected):
        assert sum(num1, num2) == expected