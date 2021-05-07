import numpy as np
import random
import createqueries, data_cleaning
T = 25
R = 20
def findDomain(data):
	domain = []
	for datum in data.keys():
		if data[datum] not in domain:
			domain.append(data[datum])
	return domain
# dat rn a  dictionory of values/names to a discreet set.
def empricaldistro(data):
	total = len(data.keys())
	empricaldistro = {}
	for dataum in data.keys():
		empricaldistro[data[dataum]] = empricaldistro[data[dataum]] + 1/total if data[dataum] in empricaldistro	else 1/total
	return empricaldistro

# dat rn a  dictionory of values/names to a discreet set.
def uniformdistro(domain):
	total = len(domain)
	uniformdistro = {}
	for i in domain:
		uniformdistro[i] = 1/total
	return uniformdistro

# query is a function 
#distro is a distribution dictionary
#empricaldistro is the true distribution
def evalquery(query,distro):
	return sum([query(i)*distro[i] for i in distro.keys()])

def scoringfunc(query,data,distro):
	return mistake(query,distro,empricaldistro(data))

def mistake(query, distro, empricaldistro):
	return abs(evalquery(query,distro) - evalquery(query,empricaldistro))

def signofmistake(query, distro, empricaldistro):
	return 1 if evalquery(query,distro) - evalquery(query,empricaldistro) > 0 else -1

#Qt is a list of queries chosen at time t
#Distrot is the list of distribtutions over daatset chosen at time t
#empricaldistro is the true distribution 
def regret(Qt,Distrot,data):
	return sum([mistake(Qt[i],Distrot[i],empricaldistro(data)) for i in range(len(Qt))])


def exponentialmechanism(Queries,data,distro,epsilon):
	querydistro = [np.exp(epsilon * scoringfunc(query,data,distro)/2) for query in Queries]
	
	choice = np.random.uniform(0,sum(querydistro))
	choiceindex = 0
	for mass in querydistro:
		choice -= mass
		if choice <= 0:
			break
		choiceindex += 1
	return Queries[choiceindex]

def noisy_max(Queries,data,distro,epsilon):
	diffs = [mistake(query,data,distro) + laplace(epsilon/0.5) for query in Queries]
	for i in range(len(diffs)):
		if diffs[i] == max(diffs):
			return Queries[i]

def laplace(epsilon):
	return np.random.laplace(loc=0.0,scale = epsilon)

def laplacemechanism(query,data,distro,epsilon):
	return evalquery(query,empricaldistro(data)) + laplace(epsilon)


def update(query,current_distro,m):
	new_distro = {}
	error = m - evalquery(query,current_distro) 
	total = sum([current_distro[i] * np.exp(query(i) * error/2) for i in current_distro.keys()])
	#print(total)
	for i in current_distro.keys():
		new_distro[i] = (current_distro[i] * np.exp(query(i) * error/2))/total
	return new_distro

def PMW(Queries, data, epsilon):
	domain = findDomain(data)
	doman_size = len(domain)
	A = uniformdistro(domain)
	scale = 2.0/(epsilon * len(data.keys()))
	Qt = []
	At = [A]
	Mt = []
	print("PMW Started")
	for i in range(T):
		print("Current iteration number:", i)
		q = noisy_max(Queries,data,A,scale)
		Qt.append(q)
		m = laplacemechanism(q,data,A,scale/0.5)
		Mt.append(m)
		A = update(q,A,m)
		for j in range(R):
			arr = [i for i in range(len(Mt))]
			np.random.shuffle(arr)
			for index in arr:
				A = update(Qt[index],A,Mt[index])
		At.append(A)
	print("total regret incured:", regret(Qt,At,data))
	return A,At,Qt

data1,data2 = data_cleaning.getdata()
#Queries = [createqueries.capitallossqeuery3,createqueries.capitallossqeuery1,createqueries.capitallossqeuery2]
domain = findDomain(data1)
Queries = [createqueries.capitalrangequeries(i) for i in domain]
trueDistro = empricaldistro(data1)
privateDistro, alldistros, querylist = PMW(Queries,data1,1)
print(privateDistro)
print(trueDistro)
for query in Queries:
	print("True distribution:", evalquery(query,trueDistro))
	print("Private distribution:", evalquery(query,privateDistro))
	print("Error:", mistake(query,privateDistro,trueDistro))
