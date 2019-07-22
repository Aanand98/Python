list = []
list_values = input()
list_values = list_values.split()
for num in list_values:
    num = int(num)
    list.append(num)
start = list[0]
end = list[-1]
for i in range(start+1,end):
    if i % 2 == 0:
        print("",i,end = '')
