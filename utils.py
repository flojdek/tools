def tail(lst):
	return lst[1:]

def head(lst):
	if lst != []:
		return lst[0]

def take_front(lst, n):
	return lst[:n]

def take_back(lst, n):
	return lst[-n:]

def pagination_range(pages_range, curr_page, left_right_radius):
	left_range = pages_range[:(curr_page-1)]
	right_range = pages_range[curr_page:]

	print left_range
	print right_range

	left_pages = take_back(left_range, left_right_radius)
	right_pages = take_front(right_range, left_right_radius)

	more_on_left = len(left_range) > len(left_pages)
	more_on_right = len(right_range) > len(right_pages)

	return (more_on_left, left_pages, right_pages, more_on_right)
