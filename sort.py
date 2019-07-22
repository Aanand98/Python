import numpy as np
n = int(input())
list_values = input()
list_values = list_values.split()
list = []
for num in list_values:
    num = int(num)
    list.append(num)
list = np.sort(list)
for num in list:
    print("",num,end = '')
