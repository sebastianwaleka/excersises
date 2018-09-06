from socks import socks


def test_socks_correct():
    assert socks(9, ['10', '20', '20', '10', '10', '30', '50', '10', '20']) == 3
    assert socks(4, ['1', '2', '1', '2']) == 2
    assert socks(5, ['1', '2', '3', '4', '5']) == 0


def test_socks_false():
    assert not socks(3, ['1', '1', '1']) == 3
    assert not socks(7, ['1', '2']) == 1