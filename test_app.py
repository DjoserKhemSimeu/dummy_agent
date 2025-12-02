import pytest
import app

def test_addition_correct_behavior():
    """
    Test prévu lorsque le bug sera corrigé.
    Le test échouera tant que 'c' sera utilisé dans app.addition.
    """
    assert app.addition(2, 3) == 5

