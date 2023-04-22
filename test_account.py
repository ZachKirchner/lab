import pytest
from account import *

account1 = Account('Real Name')


def test_init():
    assert account1.get_name() == 'Real Name'
    assert account1.get_balance() == 0


def test_deposit():
    assert account1.deposit(0) is False
    assert account1.get_balance() == 0

    assert account1.deposit(-1) is False
    assert account1.get_balance() == 0

    assert account1.deposit(72) is True
    assert account1.get_balance() == 72

    assert account1.deposit(1.2) is True
    assert account1.get_balance() == pytest.approx(73.2, abs=0.01)

    assert account1.deposit(-73.2) is False
    assert account1.get_balance() == pytest.approx(73.2, abs=0.01)


def test_withdraw():
    assert account1.withdraw(0) is False
    assert account1.get_balance() == pytest.approx(73.2, abs=0.01)

    assert account1.withdraw(-19) is False
    assert account1.get_balance() == pytest.approx(73.2, abs=0.01)

    assert account1.withdraw(53.2) is True
    assert account1.get_balance() == 20

    assert account1.withdraw(5) is True
    assert account1.get_balance() == 15

    assert account1.withdraw(16) is False
    assert account1.get_balance() == 15
