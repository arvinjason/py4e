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
	if line == 'done':
		if total == 0:
			break
		else:
			average = total / count
		break
	elif s == -1:
		print('Invalid input')		
print(total, count, average)