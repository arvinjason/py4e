def chop(lst):
	l = len(lst)
	lst.pop()
	lst.remove(lst[0])
	return None

def middle(lst):
	chop(lst)
	return lst

