def decodeHuff(root, s):
    temp = root
    res = []
    for char in s:
        if char == '0':
            temp = temp.left
        
        else:
            temp = temp.right
        
        if not temp.left and not temp.right:
            res.append(temp.data)
            temp = root
    
    print(''.join(res))