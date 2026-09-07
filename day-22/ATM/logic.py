data = {
    123456: {'name': 'lakshmi', 'pin': 1234, 'balance': 10000, 'history': []},
    123451: {'name': 'vishnu', 'pin': 1234, 'balance': 50000, 'history': []},
    123452: {'name': 'baji', 'pin': 1234, 'balance': 1000, 'history': []},
    123454: {'name': 'sunitha', 'pin': 1234, 'balance': 60000, 'history': []},
    123457: {'name': 'siva', 'pin': 1234, 'balance': 1000000, 'history': []}
}

def login():
    global acc_num
    acc_num = int(input("Enter account number: "))
    pin = int(input("Enter PIN: "))
    if acc_num in data and data[acc_num]['pin'] == pin:
        print("Login Successfully")
        return True
    else:
        print("Invalid account number or PIN")
        return False
def menu():
    print(f"\nWelcome to the ATM, {data[acc_num]['name']}")
    print("[C] Check Balance")
    print("[D] Deposit")
    print("[W] Withdraw")
    print("[V] View Transaction")
    print("[E] Exit")

def checkbalance():
    print(f"\nHello {data[acc_num]['name']}")
    print("Balance:", data[acc_num]["balance"])

def deposit():
    amount = int(input("Enter amount: "))

    data[acc_num]["balance"] += amount
    data[acc_num]["history"].append(f"{amount} is deposited")

    print(f"{amount} is deposited successfully")
def withdraw():
    amount = int(input("Enter amount: "))

    if data[acc_num]["balance"] >= amount:
        data[acc_num]["balance"] -= amount
        data[acc_num]["history"].append(f"{amount} is withdrawn")

        print(f"{amount} is withdrawn successfully")
    else:
        print("Insufficient balance")

    checkbalance()

def viewtransaction():
    if data[acc_num]["history"]:
        print("\n========= Transaction History =========")

        for i in data[acc_num]["history"]:
            print(i)

        print("============= End of History =============")
    else:
        print("No transaction history")
