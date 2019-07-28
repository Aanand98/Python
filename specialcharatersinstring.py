a = input()
count = 0
special = ['!','@','#','$','%','^','&','*','(',')','_','.','/',';',':','>','<']
for ch in a:
    if ch in special:
        count = count + 1
print(count)
