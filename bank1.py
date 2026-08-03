from dataclasses import dataclass

@dataclass
class Account:
    account_id: int
    customer_name: str
    balance: float

accounts = {}
next_id = 1001

def create_account():
    global next_id
    name = input("Enter Customer Name: ")
    account = Account(next_id, name, 0)
    accounts[next_id] = account
    print("Account Created Successfully")
    print("Account ID:", next_id)
    next_id += 1

def deposit():
    acc_id = int(input("Enter Account ID: "))
    acc = accounts.get(acc_id)
    if acc:
        amount = float(input("Enter Amount: "))
        if amount > 0:
            acc.balance += amount
            print("Deposit Successful")
            print("Balance:", acc.balance)
        else:
            print("Invalid Amount")
    else:
        print("Account Not Found")
def withdraw():
    acc_id = int(input("Enter Account ID: "))
    acc = accounts.get(acc_id)
    if acc:
        amount = float(input("Enter Amount: "))
        if amount <= 0:
            print("Invalid Amount")
        elif amount > acc.balance:
            print("Insufficient Funds")
        else:
            acc.balance -= amount
            print("Withdrawal Successful")
            print("Balance:", acc.balance)
    else:
        print("Account Not Found")
def check_balance():
    acc_id = int(input("Enter Account ID: "))
    acc = accounts.get(acc_id)
    if acc:
        print("Customer Name:", acc.customer_name)
        print("Balance:", acc.balance)
    else:
        print("Account Not Found")
def close_account():
    acc_id = int(input("Enter Account ID: "))
    acc = accounts.get(acc_id)
    if acc:
        del accounts[acc_id]
        print("Account Closed Successfully")
    else:
        print("Account Not Found")
while True:
    print("\n===== SECURE BANK =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Close Account")
    print("6. Exit")
    choice = input("Enter Choice: ")
    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        close_account()
    elif choice == "6":
        print("Thank You!")
        break
    else:
        print("Invalid Choice")