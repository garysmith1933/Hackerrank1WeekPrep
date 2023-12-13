def preOrder(root):
    stack = [root]
    res = []
    
    while stack:
        node = stack.pop()
        
        res.append(str(node.info))
        
        if node.right:
            stack.append(node.right)
        
        if node.left:
            stack.append(node.left)

    string = ' '.join(res)
    print(string)