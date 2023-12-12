stack = []
string = ''
q = int(input())

for i in range(q):
    query = input().split()
    
    if query[0] == '1':
        stack.append(string)
        string += query[1]
    
    elif query[0] == '2':
        stack.append(string)
        string = string[:-int(query[1])]
        
    elif query[0] == '3':
        print(string[int(query[1]) - 1])
    
    else:
        string = stack.pop()
