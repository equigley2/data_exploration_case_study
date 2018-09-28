import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table
import numpy as np
import seaborn as sbn

df = pd.read_csv('data/pipeline-accidents.csv')
#cleaning
# df['Date'] = df['Accident Date/Time'].apply(lambda x: (re.split("\s",str(x))[0]))
# df['Month'] = df['Date'].apply(lambda x: (re.split("/",str(x))[0]))
# df['Day'] = df['Date'].apply(lambda x: (re.split("/",str(x))[1]))
# df['Year'] = df['Date'].apply(lambda x: (re.split("/",str(x))[2]))

# df.rename(columns={'Property Damage Costs': 'Property_Damage_Costs'}, inplace=True)
# df.rename(columns={'Lost Commodity Costs': 'Lost_Commodity_Costs'}, inplace=True)
# df.rename(columns={'Public/Private Property Damage Costs': 'Public_Private_Property_Damage_Costs'}, inplace=True)
# df.rename(columns={'Emergency Response Costs': 'Emergency_Response_Costs'}, inplace=True)
# df.rename(columns={'Environmental Remediation Costs': 'Environmental_Remediation_Costs'}, inplace=True)
# df.rename(columns={'Other Costs': 'Other_Costs'}, inplace=True)
# df.rename(columns={'All Costs': 'All_Costs'}, inplace=True)

df2 = df.copy()
cols = df2.columns.tolist()
cols = [col.replace(' ', '_') for col in cols]
df2.columns = cols

# print(df2.info())
df_costs = df2[['Property_Damage_Costs', 'Lost_Commodity_Costs', 'Public/Private_Property_Damage_Costs', 'Emergency_Response_Costs', 'Environmental_Remediation_Costs', 'Other_Costs', 'All_Costs']]

df_costs['Property_Damage'] = df_costs['Property_Damage_Costs']/1000000
df_costs['Lost_Commodity'] = df_costs['Lost_Commodity_Costs']/1000000
df_costs['Public/Private_Property_Damage'] = df_costs['Public/Private_Property_Damage_Costs']/1000000
df_costs['Emergency_Response'] = df_costs['Emergency_Response_Costs']/1000000
df_costs['Environmental_Remediation'] = df_costs['Environmental_Remediation_Costs']/1000000
df_costs['Other_Costs_mil'] = df_costs['Other_Costs']/1000000
df_costs['All_Costs'] = df_costs['All_Costs']/1000000

df_costs_mil = df_costs[['Property_Damage', 'Lost_Commodity', 'Public/Private_Property_Damage', 'Emergency_Response', 'Environmental_Remediation', 'All_Costs']]
df_all_costs = df_costs[['All_Costs']]

pd.options.display.max_columns = 10

# df_costs_mil.describe().to_csv('costs_output.csv')
df_all_costs.describe().round(2).to_csv('Descriptives.csv')
# df_costs.describe('All_costs').to_csv('all_costs_output.csv')


# plot = plt.subplot(111, frame_on=False)
# plot.xaxis.set_visible(False)
# plot.yaxis.set_visible(False)
# table(plot, desc,loc='upper right')
# plt.savefig('desc_plot.png')

# print(plt.hist('Property_Damage_Costs'))
# print(df_costs.columns.tolist())
# print(df_costs.boxplot())
# print(df_costs.plot(kind = 'hist'))
# plt.show()


# print(df_costs.info())
# print(df_costs.describe())

# print(pd.df.columns())
