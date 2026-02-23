name = input("Enter student name: ")
math = int(input("Math marks: "))
science = int(input("Science marks: "))
english = int(input("English marks: "))

total = math + science + english
percentage = total / 3

print("\nStudent:", name)
print("Total:", total)
print("Percentage:", percentage)

if percentage >= 60:
    print("Result: First Class")
elif percentage >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")
