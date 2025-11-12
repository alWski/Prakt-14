def calcul_average(number):
    n_list = list(map(int, number.split()))
    average = sum(n_list) / len(n_list)
    return average

num = input()
result = calcul_average(num)
print(result)
