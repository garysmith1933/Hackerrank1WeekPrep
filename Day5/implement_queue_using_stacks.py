s1 = [] # stack 1 is the queue
s2 = [] # use this stack to reverse contents of s1

def enqueue(num):
    # Easiest operation - append to q
    s1.append(num)
    
def dequeue():
    # Will need to use two stacks here
    if s2:
        # s2 contains reversed queue
        s2.pop()
    elif s1:
        # refill s2
        while s1:
            s2.append(s1.pop())
        s2.pop() # remove the front of the "queue"
    else:
        return 
        
def printqueue():
    # Print front of queue a.k.a. peek
    if s2:
        print(s2[-1])
    elif s1:
        print(s1[0])

for _ in range(int(input())):
    query = input()
    if " " in query:
        if query.split()[0] == "1":
            enqueue(query.split()[1])
    else:
        if query == "2":
            dequeue()
        if query == "3":
            printqueue()