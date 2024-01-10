class BankAccount:
    def __init__(self, account_holder, account_number, balance=0.0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient funds. Cannot complete withdrawal.")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ${self.balance}")


def create_account():
    print("Creating a new bank account:")
    account_holder = input("Enter account holder's name: ")
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: $"))
    return BankAccount(account_holder, account_number, initial_balance)


def main():
    print("Welcome to the Pragati Banking System!")
    while True:
        print("\nOptions:")
        print("1. Create a new bank account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Check account balance")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            account = create_account()
            print("\nBank account created successfully!")
            account.display_balance()

        elif choice == '2':
            if 'account' not in locals():
                print("Error: No account exists. Please create an account first.")
            else:
                amount = float(input("Enter the deposit amount: $"))
                account.deposit(amount)

        elif choice == '3':
            if 'account' not in locals():
                print("Error: No account exists. Please create an account first.")
            else:
                amount = float(input("Enter the withdrawal amount: $"))
                account.withdraw(amount)

        elif choice == '4':
            if 'account' not in locals():
                print("Error: No account exists. Please create an account first.")
            else:
                account.display_balance()

        elif choice == '5':
            print("Thank you for using the Banking System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
