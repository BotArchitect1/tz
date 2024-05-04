from datetime import date
from typing import Optional


class Transaction:
    """
    Класс для представления записей о доходах и расходах.

    Атрибуты:
        date (date): Дата транзакции.
        category (str): Категория транзакции ('Доход' или 'Расход').
        amount (float): Сумма транзакции.
        description (Optional[str]): Описание транзакции.
    """

    def __init__(
        self,
        date: date,
        category: str,
        amount: float,
        description: Optional[str] = None,
    ):
        self._date = date
        self._category = category
        self._amount = amount
        self._description = description

    @property
    def date(self) -> date:
        return self._date

    @date.setter
    def date(self, date: date):
        self._date = date

    @property
    def category(self) -> str:
        return self._category

    @category.setter
    def category(self, category: str):
        self._category = category

    @property
    def amount(self) -> float:
        return self._amount

    @amount.setter
    def amount(self, amount: float):
        self._amount = amount

    @property
    def description(self) -> Optional[str]:
        return self._description

    @description.setter
    def description(self, description: Optional[str]):
        self._description = description

    def __str__(self):
        return f"Дата: {self.date}\nКатегория: {self.category}\nСумма: {self.amount}\nОписание: {self.description or 'Нет описания'}"
