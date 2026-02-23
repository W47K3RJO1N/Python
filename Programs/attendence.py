total = int(input("Total classes: "))
attended = int(input("Classes attended: "))

percentage = (attended / total) * 100

print("Attendance:", percentage, "%")

if percentage >= 75:
    print("Eligible for exam")
else:
    print("Not eligible for exam")
