def comp():
    a = [i for i in range(1, 10 + 1) if i % 2 == 0]
    print('com: ', a)
    
a = []
for i in range(1, 10 + 1):
    if i % 2 == 0:
        a.append(i)
    
print(a)
comp()