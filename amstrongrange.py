def amstrong(n):
    number = n
    list = []
    while number != 0:
        num = number % 10
        num = num ** 3
        list.append(num)
        number = int(number/10)
    number = sum(list)
    if number == n:
        return 1
    else:
        return 0
value = 0
list_values = input()
list_values = list_values.split()
list = []
for num in list_values:
    num = int(num)
    list.append(num)
start = list[0]
end = list[-1]
#print(start, end)
for i in range(start+1,end):
    value = amstrong(i)
    if value == 1:
        print("",i,end = '')
