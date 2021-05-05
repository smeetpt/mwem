import numpy as np
import random

# dat rn a  dictionory of values/names to a discreet set.
def empricaldistro(data):
	total = len(data.keys())
	empricaldistro = {}
	for dataum in data.keys():
		empricaldistro[data[dataum]] = empricaldistro[data[dataum]] + 1/total if data[dataum] in empricaldistro	else 1/total
	return empricaldistro

# query is a function 
#distro is a distribution dictionary
def evalquery(query,distro):
	return sum([query(i)*distro[i] for i in distro.keys()])

#Qt is a list of queries chosen at time t
#Distrot is the list of distribtutions over daatset chosen at time t
#trueDistro is the distribution 
def regret(Qt,Distrot,trueDistro):
	return sum([abs(evalquery(Qt[i],Distrot[i]) - evalquery(Qt[i],trueDistro)) for i in range(len(Qt))])
