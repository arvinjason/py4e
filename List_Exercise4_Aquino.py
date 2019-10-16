lst = list()
while True:
	line = input('Enter a number: ')
	try:
		s = int(line)
	except:
		s = '-1'
	if s != '-1':
		lst.append(s)
	if line == 'done':
		break	
	elif s == '-1':
		print('Invalid input')
print(' Maximum: ', max(lst), '\n', 'Minimum: ', min(lst))
