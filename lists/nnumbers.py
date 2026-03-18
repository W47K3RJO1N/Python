from collections import deque

n = int(input("Enter n: "))
q = deque()

q.append("1")

for i in range(n):
    front = q.popleft()
    print(front)

    q.append(front + "0")
    q.append(front + "1")
