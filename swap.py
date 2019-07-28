list = [int(x) for x in input().split()]
temp = list [0]
list[0] = list[-1]
list[-1] = temp
for ele in list:
    print(ele,end = ' ')
    
