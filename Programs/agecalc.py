birth_year = int(input("Enter birth year: "))
current_year = 2026

age = current_year - birth_year
print("Your age is:", age)

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
