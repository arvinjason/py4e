fn = input('Enter a file name: ')
count = 0
if fn == 'na na boo boo':
	print("NA NA BOO BOO TO YOU - You have been punk'd!")
	quit()
else:
	try:
	      fh = open(fn)
	except:
	      print('File cannot be opened:', fn)
	      quit()
	for line in fh:
	    if line.startswith('Subject:') :
	        count = count + 1
	print('There were', count, 'subject lines in', fn)