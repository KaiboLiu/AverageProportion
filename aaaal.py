def al1(x, y, k):
    if y == 0: return 0
    y1 = min(max(x-k+1, 1), y)
    a = list(range(k, k+y1))
    b = list(range(k, x+1))[:y] if x >=k else [x]

    s = sum(range(k, k+y1)) - x*y/2*(y1/y)**2

    return a==b if a==b else (a,b), s


x, y, k = 5,4,1
print(x,y,k,al1(x,y,k))

x, y, k = 5,7,1
print(x,y,k,al1(x,y,k))

x, y, k = 7,5,1
print(x,y,k,al1(x,y,k))

x, y, k = 5,7,3
print(x,y,k,al1(x,y,k))

x, y, k = 7,5,3
print(x,y,k,al1(x,y,k))

x, y, k = 7,5,8
print(x,y,k,al1(x,y,k))
