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
	threshold = 10000
	if value == 0:
		return 1
	else:
		return 0

def capitalrangequeries(threshold):
	def query(value):
		if value <= threshold:
			return 1
		else:
			return 0
	return query

def capitalrangequeries2(threshold):
	def query(value):
		if value < threshold or value > 1 - threshold:
			return 1
		else:
			return 0
	return query

def capitalrangequeries3(threshold):
	def query(value):
		if value <= threshold or value >= 1 - threshold:
			return 0
		else:
			return 1
	return query

def agexhourqeuery1(value):
	threshold = 10000
	if value[1] <= 16:
		return 0
	else:
		return val 

def agexhourqeuery1(value):
	threshold = 10000
	val = value/threshold if (value/threshold)  < 1 else 1
	return val 