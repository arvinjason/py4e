def count(st, c):
	num = 0
	i = 0
	while i != len(st):
		if st[i] == c:
			num = num + 1
			i = i + 1
		else:
			i = i + 1
	return num

inp1 = input('Please input string: ')
inp2 = input('Please input char: ')
print('character occurrence:', count(inp1, inp2))