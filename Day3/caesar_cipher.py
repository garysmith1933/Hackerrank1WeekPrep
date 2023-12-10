def caesarCipher(s, k):
    temp = []
    
    for char in s:
        temp.append(ord(char))
    
    for i in range(len(temp)):
        if 65 <= temp[i] <= 90:  # uppercase - 65 = 90
            temp[i] = (65 + (temp[i] - 65 + k) % 26)
        
        elif 97 <= temp[i] <= 122:  # lowercase - 97 to 122
            temp[i] = (97 + (temp[i] - 97 + k) % 26)
        
    return ''.join(map(chr, temp))