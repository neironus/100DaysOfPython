import pytest

from account import Account


@pytest.fixture()
def account():
    return Account()


def test_balance(account):
    assert account.balance == 0
    account + 10
    assert account.balance == 10
    account - 5
    assert account.balance == 5


def test_without_contextman_balance_negative(account):
    assert account.balance == 0
    account - 5
    assert account.balance == -5


def test_with_contextman_performs_rollback(account):
    assert account.balance == 0
    with account as acc:
        acc - 5
    assert account.balance == 0
