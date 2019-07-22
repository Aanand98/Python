def prime(n):   
    flag = True
    if n == 2:
        return 1
    elif n > 2:
        limit = int(n/2)
        for num in range(2,limit+1):
            if n % num == 0:
                return 0
                flag = False
                break
    if flag == True:
        return 1
value = 0
list_values = input()
list_values = list_values.split()
for num in list_values:
    num = int(num)
    list.append(num)
start = list[0]
end = list[-1]
#print(start, end)
for i in range(start+1,end):
    value = prime(i)
    if value == 1:
        print("",i,end = '')
