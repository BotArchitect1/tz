from openpyxl import load_workbook
from datetime import date
import pytest


def test_save_transactions(wallet):
    if len(wallet.transactions) == 0:
        wallet.add_transaction(date(2022, 1, 1), "Доход", 100, "Описание")
        wallet.add_transaction(date(2022, 1, 2), "Расход", 200)
        wallet.add_transaction(date(2022, 1, 3), "Доход", 300)

    assert len(wallet.transactions) == 3
    assert wallet.transactions[0].category == "Доход"
    assert wallet.transactions[0].amount == 100
    assert wallet.transactions[1].category == "Расход"
    assert wallet.transactions[1].amount == 200
    assert wallet.transactions[2].category == "Доход"
    assert wallet.transactions[2].amount == 300
    assert wallet.transactions[0].date == date(2022, 1, 1)
    assert wallet.transactions[1].date == date(2022, 1, 2)
    assert wallet.transactions[2].date == date(2022, 1, 3)
    assert wallet.transactions[0].description == "Описание"
    assert wallet.transactions[1].description == None
    assert wallet.transactions[2].description == None


def test_load_transactions(wallet):
    assert wallet.transactions[0].category == "Доход"
    assert wallet.transactions[1].category == "Расход"
    assert wallet.transactions[2].category == "Доход"
    assert wallet.transactions[0].amount == 100
    assert wallet.transactions[1].amount == 200
    assert wallet.transactions[2].amount == 300



def test_search_transactions(wallet):
    result = wallet.search_transactions(category="Доход")
    assert len(result) == 4
    result = wallet.search_transactions(category="Расход")
    assert len(result) == 2


def test_edit_transaction(wallet):

    wallet.edit_transaction(0, category="Расход", amount=150)
    assert wallet.transactions[0].category == "Расход"
    assert wallet.transactions[0].amount == 150

    wallet.edit_transaction(1, date=date(2024, 1, 3), description="Новое описание")
    assert wallet.transactions[1].date == date(2024, 1, 3)
    assert wallet.transactions[1].description == "Новое описание"
