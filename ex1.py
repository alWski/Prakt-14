def sum_num():
    numbers = []
    for i in range(10):
        num = int(input())
        numbers.append(num)

    nList = []
    for j in range(1, 9):
        nList.append(numbers[j-1] + numbers[j+1])

    return nList
def main():
    result = sum_num()
    print(result)

if __name__ == "__main__":
    main()
