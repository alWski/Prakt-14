numbers = []
for i in range(10):
    num = int(input())
    numbers.append(num)

nList = []
for j in range(1, 9):
    nList.append(numbers[j-1] + numbers[j+1])

print(nList)
