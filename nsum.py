list_value,range_val,list = [],[],[]
range_input = input()
range_input = range_input.split()
for num in range_input:
    num = int(num)
    range_val.append(num)
list_value = input()
list_value = list_value.split()
for num in list_value:
    num = int(num)
    list.append(num)
n = range_val[-1]
list = list[:n]
sum(list)
