x1 = int(input())
x2 = int(input())
y = int(input())
account1 = x1 - y
account2 = x2 + y
if y > x1:
    account1 = 0
    account2 = x1 + x2
else:
    account1 = x1 - y
    account2 = x2 + y
print(account1, account2)
