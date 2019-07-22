n = int(input())
number = n
list = []
while number != 0:
    num = number % 10
    num = num ** 3
    list.append(num)
    number = int(number/10)
number = sum(list)
if number == n:
    print("yes")
else:
    print("no")
