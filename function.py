def data_type(arg):
	if type(arg) == None:
		return 'no value'
	if type(arg) == str:
		return len(arg)
	elif type(arg) == bool:
		return arg
	elif type(arg) == int:
		if arg < 100:
			return "less than 100"
		elif arg == 100:
			return 'equal to 100'
		else:
			return "more than 100"
	elif type(arg) == list:
		if len(arg) < 3:
			return None
		else:
return arg[2]