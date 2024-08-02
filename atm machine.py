import datetime

class ATM:
    def __init__(self):
        self.pin ="1325"
        self.balance = 15000
        self.transaction_history = []

    def account_balance_inquiry(self):
        print(f"Your current balance is: ${self.balance:.2f}")
        self.transaction_history.append({
            "date" : datetime.datetime.now(),
            "transaction":"Balance Inquiry",
            "amount" :0
        })
    def cash_withdrawal(self, amount):
        if amount <= 0:
            print("Invalid Amount")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdraw ${amount:.2f}.")
            self.transaction_history.append({
            "date" : datetime.datetime.now(),
            "transaction":"Cash Withdrawal",
            "amount" : -amount
        })
    def cash_deposit(self, amount):
        if amount <= 0:
            print("Invalid Amount")
        else:
            self.balance += amount
            print(f"Deposited ${amount:.2f}.")
            self.transaction_history.append({
            "date" : datetime.datetime.now(),
            "transaction":"Cash Deposit",
            "amount" : amount
        })
    def pin_change(self, old_pin, new_pin):
        if old_pin != self.pin:
            print("Incorrect pin")
        elif len(new_pin) != 4 or not new_pin.isdigit():
            print("New pin must be a 4 digit number.")
        else:
            self.pin = new_pin
            print("PIN successfully changed.")
    def transaction_history_inquiry(self):
        if not self.transaction_history:
            print("No Transaction found.")
        
        else:
            for record in self.transaction_history:
                print(f"{record['date']}-{record['transaction']}:${record['amount']:.2f}")
    def run(self):
        while True:
            print("\nATM Menu:")
            print("1. Account Balance Inquiry")
            print("2. Cash Withdrawal")
            print("3. Cash Deposit")
            print("4. PIN Change")
            print("5. Transaction History")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.account_balance_inquiry()
            elif choice == '2':
                amount = float(input("Enter amount to withdraw: "))
                self.cash_withdrawal(amount)
            elif choice == '3':
                amount = float(input("Enter amount to deposit: "))
                self.cash_deposit(amount)
            elif choice == '4':
                old_pin = input("Enter old PIN: ")
                new_pin = input("Enter new PIN (4 digits): ")
                self.pin_change(old_pin, new_pin)
            elif choice == '5':
                self.transaction_history_inquiry()
            elif choice == '6':
                print("Exiting the ATM simulation.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    atm = ATM()
    atm.run()
            
