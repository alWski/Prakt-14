def proc_list():
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))
    start, end = map(int, input().split())

    start = start - 1
    end = end - 1

    element = lst1[start:end + 1][::-1]

    lst2.extend(element)

    del lst1[start:end + 1]

    return lst1, lst2


result1, result2 = proc_list()
print(result1)
print(result2)
