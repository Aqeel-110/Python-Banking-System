import pickle


class Account:
    def __init__(self, acc_number, acc_holder, balance=0):
        self.acc_number = acc_number
        self.acc_holder = acc_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount:.2f} into account {self.acc_number}. \n New balance: ${self.balance:.2f}"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrew ${amount:.2f} from account {self.acc_number}.\n New balance: ${self.balance:.2f}"
        else:
            return "Insufficient balance."

    def get_balance(self):
        return f"Account {self.acc_number} balance: ${self.balance:.2f}"


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, acc_number, acc_holder, balance=0):
        account = Account(acc_number, acc_holder, balance)
        self.accounts.append(account)
        return f"Account {account.acc_number} ({account.acc_holder}) added to the bank."

    def save_accounts_to_file(self, filename):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self.accounts, file)
            return "Accounts data saved to file."
        except Exception as e:
            return f"Error saving accounts data: {str(e)}"

    def load_accounts_from_file(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.accounts = pickle.load(file)
            return "Accounts data loaded from file."
        except Exception as e:
            return f"Error loading accounts data: {str(e)}"


# Usage
bank = Bank()

# Adding accounts
print(bank.add_account(1001, "Alice", 500))
print(bank.add_account(1002, "Bob", 1000))

# Performing transactions
print(bank.accounts[0].deposit(200))
print(bank.accounts[1].withdraw(300))

# Saving and loading accounts
print(bank.save_accounts_to_file("accounts_data.pkl"))
print(bank.load_accounts_from_file("accounts_data.pkl"))

# Displaying account information
print("\nAccount Information:")
print("=" * 50)
for account in bank.accounts:
    print(f"Account Number: {account.acc_number}")
    print(f"Account Holder: {account.acc_holder}")
    print(f"Balance: ${account.balance:.2f}")
    print("=" * 50)
