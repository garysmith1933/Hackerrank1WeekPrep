def superDigit(n, k):
    res = 0
    
    for num in n:
        res += (int(num) * k)
    
    if res > 10:
        return superDigit(str(res), 1)
    
    return res