import pytest
import app

def test_addition_correct_behavior():
    """
    Test prévu lorsque le bug sera corrigé.
    Le test échouera tant que 'c' sera utilisé dans app.addition.
    """
    assert app.addition(2, 3) == 5

def test_addition_raises_error_with_current_bug():
    """
    Vérifie qu'avec le bug actuel (utilisation de 'c' non défini),
    la fonction lève bien une NameError.
    """
    with pytest.raises(NameError):
        app.addition(1, 1)
