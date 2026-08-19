from dataclasses import dataclass
from collections import defaultdict
@dataclass
class Account:
    id: int
    name: str
    balance: float = 0
@dataclass
class Transaction:
    type: str
    amount: float
accounts = {}
transactions = defaultdict(list)
customer_accounts = defaultdict(list)
id = 1001
while True:
    print("\n--- BANK ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Close Account")
    print("6. Display Account Details")
    print("7. Transfer Money")
    print("8. Reverse Last Transaction")
    print("9. Find Customer Accounts")
    print("10. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        name = input("Enter name: ")
        accounts[id] = Account(id, name)
        customer_accounts[name].append(id)
        print("Account created")
        print("Your Account ID:", id)
        id += 1
    elif choice == "2":
        acc = int(input("Enter Account ID: "))
        if acc in accounts:
            amount = float(input("Enter amount: "))
            if amount > 0:
                accounts[acc].balance += amount
                transactions[acc].append(
                    Transaction("Deposit", amount)
                )
                print("Deposit successful")
            else:
                print("Invalid amount")
        else:
            print("Account not found")
    elif choice == "3":
        acc = int(input("Enter Account ID: "))
        if acc in accounts:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Invalid amount")
            elif amount <= accounts[acc].balance:
                accounts[acc].balance -= amount
                transactions[acc].append(
                    Transaction("Withdraw", amount)
                )
                print("Withdraw successful")
            else:
                print("Insufficient balance")
        else:
            print("Account not found")
    elif choice == "4":
        acc = int(input("Enter Account ID: "))
        if acc in accounts:
            print("Name:", accounts[acc].name)
            print("Balance:", accounts[acc].balance)
        else:
            print("Account not found")
    elif choice == "5":
        acc = int(input("Enter Account ID: "))
        if acc in accounts:
            name = accounts[acc].name
            del accounts[acc]
            customer_accounts[name].remove(acc)
            print("Account closed")
        else:
            print("Account not found")
    elif choice == "6":
        if len(accounts) == 0:
            print("No accounts available")
        else:
            print("\n--- Account Details ---")
            for account in accounts.values():
                print("Account ID:", account.id)
                print("Name:", account.name)
                print("Balance:", account.balance)
                print("----------------------")
    elif choice == "7":
        sender = int(input("Enter Sender Account ID: "))
        receiver = int(input("Enter Receiver Account ID: "))
        if sender not in accounts:
            print("Sender account not found")
        elif receiver not in accounts:
            print("Receiver account not found")
        else:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Invalid amount")
            elif amount > accounts[sender].balance:
                print("Insufficient balance")
            else:
                accounts[sender].balance -= amount
                accounts[receiver].balance += amount
                transactions[sender].append(
                    Transaction("Transfer", amount)
                )
                transactions[receiver].append(
                    Transaction("Transfer", amount)
                )
                print("Transfer successful")
    elif choice == "8":
        acc = int(input("Enter Account ID: "))
        if acc not in accounts:
            print("Account not found")
        elif len(transactions[acc]) == 0:
            print("No transaction to reverse")
        else:
            last = transactions[acc].pop()
            if last.type == "Deposit":
                accounts[acc].balance -= last.amount
                print("Last deposit reversed")
            elif last.type == "Withdraw":
                accounts[acc].balance += last.amount
                print("Last withdrawal reversed")
            else:
                print("Transfer reversal needs both accounts")
    elif choice == "9":
        name = input("Enter customer name: ")
        if name in customer_accounts:
            print("\nAccounts of", name)
            for acc in customer_accounts[name]:
                if acc in accounts:
                    print(
                        "Account ID:", acc,
                        "Balance:", accounts[acc].balance
                    )
        else:

            print("Customer not found")
    elif choice == "10":

        print("Thank you!")
        break
    else:
        print("Invalid choice")