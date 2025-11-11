num = list(map(int, input().split()))

newNum = num

while 3 in newNum:
    newNum.remove(3)
print(newNum)
