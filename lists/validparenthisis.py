s = "({[]})"
stack = []
mapping = {')':'(', '}':'{', ']':'['}

for ch in s:
    if ch in mapping.values():
        stack.append(ch)
    else:
        if not stack or stack.pop() != mapping[ch]:
            print("Not Valid")
            break
else:
    print("Valid")
