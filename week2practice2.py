a = int(input())
w =(1000- a)//500
x = (1000-a-500*w) // 100
y = (1000-a-500*w-100*x) // 50
z = (1000-a-500*w-100*x-50*y) // 10
c = (1000-a-500*w-100*x-50*y-10*z) // 5
d = (1000-a-500*w-100*x-50*y-10*z-5*c) // 1


print(w,x,y,z,c,d)

