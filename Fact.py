n = int(input())
num,new_num = 1,1
while new_num <= n:
    num = num * new_num
    new_num = new_num + 1
print(num)
