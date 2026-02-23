balance = 5000

print("1. Check Balance")
print("2. Withdraw Money")
choice = int(input("Enter choice: "))

if choice == 1:
    print("Your balance is:", balance)
elif choice == 2:
    amount = int(input("Enter withdrawal amount: "))
    if amount <= balance:
        balance -= amount
        print("Please collect your cash")
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance")
else:
    print("Invalid choice")
