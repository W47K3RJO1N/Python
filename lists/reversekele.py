from collections import deque

q = deque([1, 2, 3, 4, 5])
k = 3

stack = []

for i in range(k):
    stack.append(q.popleft())

while stack:
    q.appendleft(stack.pop())

print(q)
