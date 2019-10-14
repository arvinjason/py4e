fn = input('Enter a file name: ')
fh = open(fn,'r')
for line in fh:
	print(line.upper())