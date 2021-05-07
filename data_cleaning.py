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
	X = np.random.normal(loc = .5, scale = .73, size = 1000)
	Y = np.random.normal(loc = .67, scale = .45, size = 1000) 
	S = X + Y 
	S = S.round(decimals = 2)
	S_freq = {}
	for item in S:
		if item in S_freq:
			S_freq[item] += 1
		else:
			S_freq[item] = 1
	return S_freq