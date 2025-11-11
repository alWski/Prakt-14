lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
start, end = map(int, input().split())

start = start - 1
end = end - 1

element = lst1[start:end + 1][::-1]

lst2.extend(element)

del lst1[start:end + 1]

print(lst1)
print(lst2)
