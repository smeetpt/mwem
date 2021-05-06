#value, a numer and we return a value between [0,1] depeding on value 
def capitallossqeuery1(value):
	threshold = 10000
	if value == 0:
		return 1
	else:
		val = 1 - (value/threshold) if 1 - (value/threshold)  > 0 else 0
		return val 

def capitallossqeuery2(value):
	threshold = 10000
	val = value/threshold if (value/threshold)  < 1 else 1
	return val 

def capitallossqeuery3(value):
	threshold = 1000
	val = value/threshold if (value/threshold)  < 1 else 1
	return val 

def agexhourqeuery1(value):
	threshold = 10000
	if value[1] <= 16:
		return 0
	else:
		
		return val 

def agexhourqeuery1(value):
	threshold = 10000
	val = value/threshold if (vlaue/threshold)  < 1 else 1
	return val 