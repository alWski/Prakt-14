def del_three():
	num = list(map(int, input().split()))

	new_num = num

	while 3 in new_num:
		new_num.remove(3)
	return new_num
result = del_three()
print(result)
