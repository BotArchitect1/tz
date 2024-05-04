import logging


def show_balance(wallet):
    """
    Выводит текущий баланс, общую сумму доходов и общую сумму расходов.

    Args:
        wallet (Wallet): Объект класса Wallet.
    """
    try:
        balance, total_income, total_expense = wallet.get_balance()
    except Exception as e:
        logging.info(f"An error {e} occurred while showing transactions")
    else:
        print(f"\nБаланс: {balance:.2f}")
        print(f"Общая сумма доходов: {total_income:.2f}")
        print(f"Общая сумма расходов: {total_expense:.2f}")
