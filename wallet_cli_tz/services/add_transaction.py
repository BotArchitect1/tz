import logging
from datetime import date


def add_transaction(wallet):
    """
    Добавляет новую транзакцию.

    Args:
        wallet (Wallet): Объект класса Wallet.
    """
    try:
        date_str = input("Введите дату (ГГГГ-ММ-ДД): ")
        category = input("Введите категорию ('Доход' или 'Расход'): ")
        amount = float(input("Введите сумму: "))
        description = input("Введите описание (необязательно): ")
        if not description:
            description = "Нет описания"
        transaction_date = date.fromisoformat(date_str)
        wallet.add_transaction(transaction_date, category, amount, description)
    except Exception as e:
        logging.info(f"An error {e} occurred while adding a transaction")
    else:
        print("\nТранзакция успешно добавлена.")
        logging.info(f"Transaction for the amount {amount}:{category} added")
