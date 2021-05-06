import numpy as np
import random
import createqueries, data_cleaning
T = 10
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

def laplace(epsilon):
	return np.random.laplace(loc=0.0,scale = epsilon)

def laplacemechanism(query,data,distro,epsilon):
	return evalquery(query,distro) - evalquery(query,empricaldistro(data)) + laplace(2*T/epsilon)


def update(query,current_distro,para):
	new_distro = {}
	total = 0
	for i in current_distro.keys():
		new_distro[i] = current_distro[i] * np.exp(query(i) * para)
		total += new_distro[i]
	for i in current_distro.keys():
		new_distro[i] = new_distro[i]/total
	return new_distro


def PMW(Queries, data, epsilon):
	domain = findDomain(data)
	doman_size = len(domain)
	A = uniformdistro(domain)
	Qt = []
	At = [A]
	print("PMW Started")
	for i in range(T):
		print("Current iteration number:", i)
		q = exponentialmechanism(Queries,data,A,epsilon/(2*T))
		Qt.append(q)
		m = laplacemechanism(q,data,A,epsilon)
		A = update(q,A,m/(2*doman_size))
		At.append(A)
	print("total regret incured:", regret(Qt,At,data))
	return A,At,Qt

data1,data2 = data_cleaning.getdata()
Queries = [createqueries.capitallossqeuery1,createqueries.capitallossqeuery2,createqueries.capitallossqeuery2]
trueDistro = empricaldistro(data1)
privateDistro, alldistros, querylist = PMW(Queries,data1,1)
print(privateDistro)
print(trueDistro)
print(querylist)
for query in Queries:
	print("True distribution:", evalquery(query,trueDistro))
	print("Private distribution:", evalquery(query,privateDistro))
	print("Error:", mistake(query,privateDistro,trueDistro))
