import re

def title1(x):
	ret = re.search(u'<title>(.*)</title>', x, re.M)
	if ret == None:
		return 'None'
	else:
		return ret.group(1)

def title2(x):
	ret = re.search(u'<title><!\[CDATA\[(.*)\]\]></title>', x, re.M)
	if ret == None:
		return 'None'
	else:
		return ret.group(1)

def td(x):
	ret = re.search(u'<td(.*)>(.*)</td>', x, re.M)
	if ret == None:
		return 'None'
	else:
		return ret.group(2)

def percent(x):
	ret = re.search(u'(.*)%', x, re.M)
	if ret == None:
		return 'None'
	else:
		return ret.group(1)
