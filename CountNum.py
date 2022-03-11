def CountNum(text):
    count = 0
    for x in text:
        if x>='a' and x<='z':
            count += 1
    return count