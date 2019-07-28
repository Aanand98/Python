n = int(input())
list = [0,1]
for i in range(3,n+2):
    sum = list[-1] + list[-2]
    list.append(sum)
for ele in list:
    if ele != 0:
        print(ele,end = ' ')
