list = [int(x) for x in input().split()]
list[0] = list [0] ^ list[-1]
list[-1] = list [0] ^ list[-1]
list[0] = list [0] ^ list[-1]
for ele in list:
    print(ele,end = ' ')
