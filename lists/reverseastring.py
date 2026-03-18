string = "hello"
stack = []

for ch in string:
    stack.append(ch)

rev = ""

while stack:
    rev += stack.pop()

print("Reversed:", rev)
