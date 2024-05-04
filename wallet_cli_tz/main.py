import logging

from wallet.wallet import Wallet
from wallet_cli_tz.logging_logic.loger import register_logger
from wallet_cli_tz.services import services


def print_menu():
    """
    Функция для вывода меню на экран.
    """
    print("\nМеню:")
    print("1. Вывод баланса")
    print("2. Добавить транзакцию")
    print("3. Редактировать транзакцию")
    print("4. Поиск транзакций")
    print("5. Выход")


def main():
    """
    Главная функция для запуска приложения.
    """
    register_logger()

    wallet = Wallet("transactions.xlsx")

    while True:
        print_menu()
        choice = input("Выберите операцию (1-5): ")

        if choice in services:
            services[choice](wallet)
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        logging.error("Stopping app")
