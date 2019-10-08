total = 0
count = 0
average = 0.0
smallest = None
biggest = None
while True:
	line = input('Enter a number: ')
	try:
		s = int(line)
	except:
		s = -1
	if s != -1:
		total = total + s
		count = count + 1
		if smallest is None : 
			smallest = s
		elif s < smallest : 
			smallest = s
		if biggest is None : 
			biggest = s
		elif s > biggest : 
			biggest = s
	if line == 'done':
		break	
	elif s == -1:
		print('Invalid input')
print(total, count, smallest, biggest)