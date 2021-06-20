def solve(s):
    a = s.split(" ")
    lst = []
    for i in a:
        lst.append(i.capitalize())
    st = ' '.join(lst)
    return st

s = input()
ans = solve(s)
print(ans)
