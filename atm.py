class ATM:
    def __init__(self):
        self.balance = 1000  # Initial balance

    def check_balance(self):
        return f"Your current balance is ${self.balance:.2f}"

    def deposit_money(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposit successful. Your new balance is ${self.balance:.2f}"
        else:
            return "Invalid deposit amount. Please enter a positive value."

    def withdraw_money(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrawal successful. Your new balance is ${self.balance:.2f}"
        elif amount <= 0:
            return "Invalid withdrawal amount. Please enter a positive value."
        else:
            return "Insufficient funds. Withdrawal unsuccessful."

def main():
    atm = ATM()

    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(atm.check_balance())
        elif choice == "2":
            amount = float(input("Enter the deposit amount: "))
            print(atm.deposit_money(amount))
        elif choice == "3":
            amount = float(input("Enter the withdrawal amount: "))
            print(atm.withdraw_money(amount))
        elif choice == "0":
            print("Exiting the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
