class BankAccount:
    account_counter = 1000  # Hər hesaba unikal nömrə vermək üçün

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.account_number = BankAccount.account_counter
        BankAccount.account_counter += 1
        self.history = []

    def display_balance(self):
        print(f"{self.name}, your current balance is ${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(f"Deposited ${amount}")
            print(f"${amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Withdrew ${amount}")
            print(f"${amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def transfer(self, amount, target_account):
        if amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount
            self.history.append(f"Transferred ${amount} to {target_account.name}")
            target_account.history.append(f"Received ${amount} from {self.name}")
            print(f"Transferred ${amount} to {target_account.name}")
        else:
            print("Transfer failed: insufficient balance.")

    def show_history(self):
        print("\nTransaction history:")
        for record in self.history:
            print("-", record)


# ==============================

def main():
    # 2 hesablə test edək
    account1 = BankAccount("Alice", 500)
    account2 = BankAccount("Bob", 300)

    current_account = account1  # Hal-hazırda istifadə olunan hesab

    while True:
        print(f"\n=== Welcome, {current_account.name} ===")
        print("1. View Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. View History")
        print("6. Switch Account")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            current_account.display_balance()
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            current_account.deposit(amount)
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            current_account.withdraw(amount)
        elif choice == "4":
            amount = float(input("Enter amount to transfer: "))
            target = account2 if current_account == account1 else account1
            current_account.transfer(amount, target)
        elif choice == "5":
            current_account.show_history()
        elif choice == "6":
            current_account = account2 if current_account == account1 else account1
        elif choice == "7":
            print("Thanks for using our bank system.")
            break
        else:
            print("Invalid option. Try again.")

# Call the function
main()
