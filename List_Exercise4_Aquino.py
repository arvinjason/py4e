lst = list()
while True:
	line = input('Enter a number: ')
	try:
		s = int(line)
	except:
		s = '-1'
	if line == 'done':
		break	
	if s != '-1':
		lst.append(s)	
	elif s == '-1':
		print('Invalid input')	
if lst == []:
	exit()
else:
	print(' Maximum: ', max(lst), '\n', 'Minimum: ', min(lst))
