a = int(input())
b = [input() for i in range(a)]
lst = []
for i in b:
    if i not in lst:
        lst.append(i)
print(len(lst))
lst1 = []
for i in lst:
    c = b.count(i)
    lst1.append(c)
    
for i in lst1:
    print(i,end=" ")
