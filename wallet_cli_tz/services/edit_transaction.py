import logging
from datetime import date


def edit_transaction(wallet):
    """
    Редактирует существующую транзакцию.

    Args:
        wallet (Wallet): Объект класса Wallet.
    """
    try:
        while True:
            try:
                index = int(input("Введите индекс транзакции для редактирования: "))
                break
            except ValueError:
                print("Некорректный ввод. Попробуйте снова.")

        update_data = {}

        date_str = input(
            "Введите новую дату (ГГГГ-ММ-ДД) или нажмите Enter для пропуска: "
        )
        if date_str:
            update_data["date"] = date.fromisoformat(date_str)
        category = input(
            "Введите новую категорию ('Доход' или 'Расход') или нажмите Enter для пропуска: "
        )
        if category:
            update_data["category"] = category
        amount_str = input("Введите новую сумму или нажмите Enter для пропуска: ")
        if amount_str:
            update_data["amount"] = float(amount_str)
        description = input("Введите новое описание или нажмите Enter для пропуска: ")
        if description:
            update_data["description"] = description
        wallet.edit_transaction(index, **update_data)

    except Exception as e:
        logging.info(f"An error {e} occurred while editing a transaction")
    else:
        print(f"\nТранзакция успешно отредактирована.")
        logging.info(f"Transaction for the index {index} edited")
