def mixSweetness(value1, value2):
    return value1 + (value2 * 2)

def cookies(k, A):
    heapq.heapify(A)
    count = 0
    
    while True:
        value1 = heapq.heappop(A)
        if value1 >= k:
            return count
        
        if A:
            value2 = heapq.heappop(A)
            heapq.heappush(A, mixSweetness(value1, value2))
            count += 1
        
        else:
            return -1