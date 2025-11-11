def sort_string(s):
    nList = list(s)
    nList.sort()
    return ''.join(nList)


strok = input()
res = sort_string(strok)
print(res)
