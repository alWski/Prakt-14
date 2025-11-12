def find_divisors():
    num = int(input())
    delit = []
    for i in range(1, num + 1):
        if num % i == 0:
            delit.append(i)
    print(delit)

find_divisors()
