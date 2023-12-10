def minimumBribes(q):
    bribes = 0
    
    for i in range(len(q)-1, -1, -1):
        expectedNum = i + 1
        if q[i] != expectedNum:
            # find where it is at
            if q[i-1] == expectedNum:
                bribes += 1
                q[i - 1], q[i] = q[i], q[i - 1]
            
            elif q[i-2] == expectedNum:
                bribes += 2
                q[i - 2], q[i - 1], q[i] = q[i - 1], q[i], q[i - 2]
            
            else:
                print('Too chaotic')
                return
    print(bribes)