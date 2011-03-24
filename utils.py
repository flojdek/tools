def tail(lst):
	return lst[1:]

def head(lst):
	if lst != []:
		return lst[0]

def take(lst, n):
	if n > len(lst):
		return lst
	else:
		return lst[:n]
