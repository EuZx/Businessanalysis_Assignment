a = int(input())
w = (1000 - a) // 500
h = (1000 - a - 500*w) // 100
y = (1000 - a - 500*w - 100*h) // 50
m = (1000 - a - 500*w - 100*h - 50*y) // 10
e = (1000 - a - 500*w - 100*h - 50*y - 10*m) // 5
l = (1000 - a - 500*w - 100*h - 50*y - 10*m - 5*e) // 1
print('500',w,'100',h,'50',y,'10',m,'5',e,'1',l)
