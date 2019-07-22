number = int(input())
num = 0
n = number
while n != 0:
    num = (num * 10) + (n % 10)
    n = n / 10
    n = int(n)
if number == num:
    print("yes")
else:
    print("no")
