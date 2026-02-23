price = int(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

if total >= 5000:
    discount = total * 0.1
    total -= discount
    print("Discount applied:", discount)

print("Final Bill:", total)
