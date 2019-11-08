file = input('Enter file name: ')
fh = open(file)
hour = dict()
for line in fh:
	if line.startswith("From "):
		lst = line.split()
		lst2 = lst[5].split(':')
		if lst2[0] not in hour:
			hour[lst2[0]] = 1
		else:
			hour[lst2[0]] = hour[lst2[0]] + 1
lst = []
for key, val in hour.items():
	print(key, val)