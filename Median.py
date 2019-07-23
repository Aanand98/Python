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
