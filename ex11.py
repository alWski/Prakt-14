def rotate_list():
    lst = list(map(int, input().split()))
    command = input()

    napr = command[0]
    pos = int(command[1:])

    n = len(lst)
    if napr == 'R':
        pos = n - pos % n
    elif napr == 'L':
        pos = pos % n

    result = lst[pos:] + lst[:pos]

    return result

result = rotate_list()
print(result)
