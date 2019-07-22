list_values = input()
list_values = list_values.split()
list = []
for num in list_values:
    num = int(num)
    list.append(num)
N_time = list[0] 
Start = list[1]
Difference = list[-1]
num = Start
n = []
while N_time > 0:
    N_time = N_time - 1
    n.append(num)
    num = num + Difference
print(sum(n))
