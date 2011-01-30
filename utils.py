def tail(lst):
	if lst != []:
		return lst[1:]
	else:
		return []

def head(lst):
	if lst != []:
		return lst[0]

def take(lst, n):
	ret = []
	lst_len = len(lst)
	for i in range(0, n):
		if i >= lst_len: break	
		ret.append(lst[i])
	return ret
