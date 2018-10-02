def al1(x, y, k):
    if y == 0: return 0
    curr = list(range(k, x+1))[:y] if x >=k else [x]
    y1 = len(curr)
    s = sum(curr) - x*y/2*(y1/y)**2
    return s, y1, y, s/y1

# diagonal of catchup 1112 
def al2(x,y,k):
    if y == 0: return 0

    inc = [1,1,1,1,0]
    start = 1
    curr = [k] if x >=k else [x]
    for i in range(1, y): 
        if curr[-1] == x: break
        newval = curr[-1]+inc[i % 5]
        curr.append(newval)
    y1 = len(curr)
    s = sum(curr) - x*y/2*(y1/y)**2
    #return s/y1
    return s, y1, y, s/y1

x, y, k = 5,4,1
print(x,y,k,al1(x,y,k))
print(x,y,k,al2(x,y,k))
x, y, k = 5,7,1
print(x,y,k,al1(x,y,k))
print(x,y,k,al2(x,y,k))

x, y, k = 7,5,1
print(x,y,k,al1(x,y,k))
print(x,y,k,al2(x,y,k))

x, y, k = 5,7,3
print(x,y,k,al1(x,y,k))
print(x,y,k,al2(x,y,k))

x, y, k = 7,5,3
print(x,y,k,al1(x,y,k))
print(x,y,k,al2(x,y,k))

x, y, k = 96,36,8
print(x,y,k,al1(x,y,k))
print(x,y,k,al2(x,y,k))

'''
x, y, k = 22,25,8
for k in range(1,11):
	print(x,y,k,al1(x,y,k))
	print(x,y,k,al2(x,y,k))
'''