def isBalanced(s):
    hashmap = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    
    stack = []
    
    for bracket in s:
        if bracket in hashmap:
            stack.append(bracket)
        
        else:
            if not stack or hashmap[stack[-1]] != bracket:
                return 'NO'
            stack.pop()
    
    return 'NO' if stack else 'YES'