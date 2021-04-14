def enQ(x):
    global rear
    if rear == len(Q) - 1:
        print("full")
    else:
        rear += 1
        Q[rear] = x


def deQ():
    global front
    if front == rear:
        print("empty")
    else:
        front += 1
        print(Q[front])


Q = [0] * 100  # 적당히

front, rear = -1, -1

enQ(1)
enQ(2)
enQ(3)
enQ(4)

deQ()
deQ()
deQ()
deQ()
deQ()
