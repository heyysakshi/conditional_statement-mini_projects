name = input("Enter the Name of Account Holder: ")
balance = int(input("Enter the Current Balance: "))
withdraw = int(input("Enter the Withdrawal Amount: "))
print("Account Holder : ", name)
if withdraw <= 0:
    print("Transaction Status: Failed")
    print("Reason: Withdrawal amount must be greater than 0...")
elif withdraw > balance:
    print("Transaction Status: Failed")
    print("Reason: Withdrawal amount must not exceed the current balance...")
elif withdraw > 20000:
    print("Transaction Status: Failed")
    print("Reason: Maximum withdrawal allowed in one transaction is 20,000...")
else:
    remaining_balance = balance - withdraw
    print("Transaction Status: Successful")
    print("Withdrawn Amount: ", withdraw)
    print("Remaining Balance: ", remaining_balance)
    if remaining_balance < 1000:
        print("Low Balance Warning...")