queue = []


queue.append(10)
queue.append(20)
queue.append(30)

if queue:
    print("Removed:", queue.pop(0))

if queue:
    print("Front:", queue[0])

print("Queue:", queue)
