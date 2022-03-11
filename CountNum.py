with open('./test/test.txt','r') as f:
    text = f.read()
print(text)
count = 0
for x in text:
    if x>='a' and x<='z':
        count += 1
print(count)