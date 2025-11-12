def sum_all(numbers):
    chet = 0
    nechet = 0
    
    for i in numbers:
        if i % 2 == 0:
            chet += i
        else:
            nechet += i
            
    return chet, nechet

num = list(map(int, input().split()))

chet_sum, nechet_sum = sum_all(num)
print(chet_sum, nechet_sum)
