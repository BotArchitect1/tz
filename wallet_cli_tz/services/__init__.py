from wallet_cli_tz.services.show_balance import show_balance
from wallet_cli_tz.services.add_transaction import add_transaction
from wallet_cli_tz.services.edit_transaction import edit_transaction
from wallet_cli_tz.services.search_transactions import search_transactions

services = {
    "1": show_balance,
    "2": add_transaction,
    "3": edit_transaction,
    "4": search_transactions,
}
