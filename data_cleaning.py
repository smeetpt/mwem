#%%
import pandas as pd
import numpy as np 
from sklearn.mixture import GaussianMixture

"""
df_capital_loss = {key : capital loss}
df_age_hours = {key : [age, hours]}
"""
def getdata():
	df = pd.read_csv("adult.data", header = None)
	df['key'] = [x for x in range(0, len(df))]
	df_capital_loss_list = df.iloc[:, [15,11]]
	df_capital_loss_list.columns = ['key','capital_loss']
	df_age_hours_list = df.iloc[:,[15,0,12]]
	df_age_hours_list.columns = ['key','age', 'hours']
	df_capital_loss = {}
	df_age_hours = {}

	for key in df['key']:
		df_capital_loss[key] = df_capital_loss_list['capital_loss'][key]
		df_age_hours[key] = [df_age_hours_list['age'][key], df_age_hours_list['hours'][key]]
	return df_capital_loss, df_age_hours

def get_range_query():
	X = np.random.normal(loc = 50, scale = 50, size = 100) # Check again 
	Y = np.random.normal(loc = 50, scale = 50, size = 100)
	S = X + Y 
	S_freq = {}
	for item in S:
		element = int(item)
		if element in S_freq:
			S_freq[element] += 1
		else:
			S_freq = 1
	return S_freq

