balance = 10000

print("1. Deposit")
print("2. Withdraw")
print("3. Check Balance")

choice = int(input("Enter choice: "))

if choice == 1:
    amount = int(input("Enter deposit amount: "))
    balance += amount
    print("New balance:", balance)

elif choice == 2:
    amount = int(input("Enter withdraw amount: "))
    if amount <= balance:
        balance -= amount
        print("New balance:", balance)
    else:
        print("Insufficient balance")

elif choice == 3:
    print("Balance:", balance)

else:
    print("Invalid choice")
