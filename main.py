import re

def strip(string,arg=''):

	if arg == '':
		del_void = re.compile(r'(^\s+)|(\s+$)|(\s){2}')
		result = re.sub(del_void, '', string)
		print(result)
	else:
		del_void = re.compile(r'['+arg+']')
		result = re.sub(del_void, '', string)
		print(result)

strip('$#       apple horse    $     ')
