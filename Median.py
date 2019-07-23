def sort(list,n):
    for i in range(0,n):
        for j in range(i,n):
            if list[i] > list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    return list
n = int(input())
list_values = input()
list_values = list_values.split()
list = []
for num in list_values:
    num = int(num)
    list.append(num)
list = sort(list,n)
#for num in list:
    #print("",num,end = '')
#print(n)
print(list[int(round((n)/2))]) 
