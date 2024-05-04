import logging
from datetime import date


def search_transactions(wallet):
    """
    Выполняет поиск транзакций по заданным критериям.

    Args:
        wallet (Wallet): Объект класса Wallet.
    """
    try:
        category = input(
            "Введите категорию ('Доход' или 'Расход') или нажмите Enter для пропуска: "
        )
        date_str = input("Введите дату (ГГГГ-ММ-ДД) или нажмите Enter для пропуска: ")
        amount_str = input("Введите сумму или нажмите Enter для пропуска: ")
        category = category if category else None
        transaction_date = date.fromisoformat(date_str) if date_str else None
        amount = float(amount_str) if amount_str else None
        transactions = wallet.search_transactions(category, transaction_date, amount)
    except Exception as e:
        logging.info(f"An error {e} occurred while searching transactions")
    else:
        if transactions:
            print("\nНайденные транзакции:")
            for i, tx in enumerate(transactions, 1):
                print(f"{i}. {tx}")
        else:
            print("Транзакции не найдены.")
