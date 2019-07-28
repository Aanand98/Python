list = [int(x) for x in input().split()]
max = 0
for ele in list:
  if ele > max:
    max = ele
print(max)
