file = input('Enter file name: ')
fh = open(file)
count = 0
for line in fh:
	if line[0:4] == 'From':
		lst = line.split()
		print(lst[1])
		count = count + 1
	else:
		continue
print('There were', count ,'lines with From as the first word')