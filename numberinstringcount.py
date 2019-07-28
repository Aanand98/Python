a = input()
numbers = ['1','2','3','4','5','6','8','7','9','0']
count = 0
for ch in a:
    if ch in numbers:
        count = count + 1
print(count)
