n = int(input())
flag = True
if n == 2:
    print("yes")
elif n > 2:
    limit = int(n/2)
    for num in range(2,limit):
        if n % num == 0:
            print("no")
            flag = False
            break
if flag == True:
    print("yes")
