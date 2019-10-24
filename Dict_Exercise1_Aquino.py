file = input('Enter file name: ')
fh = open(file)
date = dict()
for line in fh:
	if line.startswith("From "):
		lst = line.split()
		if lst[2] not in date:
			date[lst[2]] = 1
		else:
			date[lst[2]] = date[lst[2]] + 1
print(date) 
