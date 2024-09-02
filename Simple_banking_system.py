# Banking System

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful! Your new balance is: {}".format(self.balance))
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        elif amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        else:
            self.balance -= amount
            print("Withdrawal successful! Your new balance is: {}".format(self.balance))

    def display_balance(self):
        print("Account owner: {}".format(self.owner))
        print("Current balance: {}".format(self.balance))


def main():
    print("Welcome to the Simple Banking System")
    
    # Create an account
    owner_name = input("Enter account owner's name: ")
    initial_deposit = float(input("Enter initial deposit amount: "))
    account = BankAccount(owner_name, initial_deposit)
    print("Account created successfully for {} with balance {}.".format(owner_name, initial_deposit))

    while True:
        print("\nOptions:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. View Balance")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)

        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)

        elif choice == '3':
            account.display_balance()

        elif choice == '4':
            print("Thank you for using the Simple Banking System!")
            break

        else:
            print("Invalid choice, please select a valid option.")


if __name__ == "__main__":
    main()
