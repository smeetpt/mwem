import pandas as pd

"""
df_capital_loss = {key : capital loss}
df_age_hours = {key : [age, hours]}
"""

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
	
# print(dict(list(df_capital_loss.items())[0:20]))
# print(dict(list(df_age_hours.items())[0:20]))