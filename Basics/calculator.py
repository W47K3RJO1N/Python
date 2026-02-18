
print("Simple Calculator")


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))


print(f"\nResults:")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")

if b != 0:
    print(f"{a} / {b} = {a / b}")
else:
    print(f"{a} / {b} = Cannot divide by zero!")
