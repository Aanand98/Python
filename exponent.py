list = []
list_input = input()
list_input = list_input.split()
for num in list_input:
    num = int(num)
    list.append(num)
n = list[0]
exp = list[-1]
print(n**exp)
