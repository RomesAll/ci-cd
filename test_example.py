from main import calc

def test_add_positive_numbers():
    calc.a = 1
    calc.b = 3
    assert calc.set_plus() == 4