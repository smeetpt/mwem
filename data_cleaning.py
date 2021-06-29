import pandas as pd
import numpy as np 
from sklearn.mixture import GaussianMixture
import seaborn as sns
from scipy.stats import truncnorm

"""
df_capital_loss = {key : capital loss}
df_age_hours = {key : [age, hours]}
"""
def getdata():
	df = pd.read_csv("adult.data", header = None)
	df['key'] = [x for x in range(0, len(df))]
	df_capital_loss_list = df.iloc[:, [15,0]]
	df_capital_loss_list.columns = ['key','age']
	df_age_hours_list = df.iloc[:,[15,0,12]]
	df_age_hours_list.columns = ['key','age', 'hours']
	df_capital_loss = {}
	df_age_hours = {}

	for key in df['key']:
		df_capital_loss[key] = df_capital_loss_list['age'][key]
		df_age_hours[key] = [df_age_hours_list['age'][key], df_age_hours_list['hours'][key]]
	return df_capital_loss, df_age_hours

def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)

def get_range_query():
	X = get_truncated_normal(mean=0.5, sd=0.1, low=0, upp=1)
	S = X.rvs(1000)
	S = S.round(decimals = 2)
	S_freq = {}
	for i in range(1000):
		S_freq[i] = S[i]
	return S_freq

def get_hist(freqs):
	X = []
	Y = []
	for key, value in freqs.items():
		X.append(key)
		Y.append(value)
	sns.histplot([X,Y])
