num = list(map(int, input().split()))

chet = 0
nechet = 0

for i in num:
    if i % 2 == 0:
        chet += i
    else:
        nechet += i

print(chet, nechet)
