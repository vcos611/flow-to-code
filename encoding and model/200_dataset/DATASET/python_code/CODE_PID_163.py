def fun163(string):
    length = len(string)
    count = 0
    i = 0
    while i < length:
        ascii = ord(string[i])
        if ascii >= 48 and ascii <= 57:
            count = count + 1
        
        i = i + 1

    return count