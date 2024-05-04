import pytest
from openpyxl import load_workbook
from wallet_cli_tz.wallet.wallet import Wallet


@pytest.fixture
def wallet():
    file_path = "test_file.xlsx"
    wallet = Wallet(file_path=file_path)
    wallet.load_transactions()
    yield wallet

    try:
        wb = load_workbook(filename=file_path)
        wb.close()
    except FileNotFoundError as e:
        print(e)
