list = []
input_list = input()
input_list = input_list.split()
for num in input_list:
  num = int(num)
  list.append(num)
print(max(list))
