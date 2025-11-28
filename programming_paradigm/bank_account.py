import sys

class BankAccount:
    def __init__(self, initial_balance: float = 0):
        self.__account_balance = initial_balance  # private attribute for encapsulation

    def deposit(self, amount: float):
        if amount is None or amount < 0:
            return
        self.__account_balance += amount

    def withdraw(self, amount: float) -> bool:
        if amount is None or amount < 0:
            return False
        if self.__account_balance >= amount:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance:,.2f}")


# Optional CLI interaction directly on the class file (if run alone)
if __name__ == "__main__":
    account = BankAccount(100)
    if len(sys.argv) < 2:
        print("Usage: python bank_account.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit":
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw":
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")
