fn = input('Enter a file name: ')
fh = open(fn,'r')
count = 0.0
counter = 0
for line in fh:
	s = line.find('X-DSPAM-Confidence:')
	lend = line.find('\n')
	if s != -1:
		count = count + float(line[s+20:lend])
		counter = counter + 1
print(count/counter)