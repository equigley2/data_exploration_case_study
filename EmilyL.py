import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
from scipy import stats

import matplotlib as mpl
mpl.rcParams.update({
    'font.size'           : 10,
    'axes.titlesize'      : 'medium',
    'axes.labelsize'      : 'medium',
    'xtick.labelsize'     : 'medium',
    'ytick.labelsize'     : 'medium',
    'legend.fontsize'     : 'medium',
})

df = pd.read_csv('data/pipeline-accidents.csv')
# df.describe()

# changing the formatting of the data:
df['Date'] = df['Accident Date/Time'].apply(lambda x: (re.split("\s",str(x))[0]))
df['Month'] = df['Date'].apply(lambda x: (re.split("/",str(x))[0]))
df['Day'] = df['Date'].apply(lambda x: (re.split("/",str(x))[1]))
df['Year'] = df['Date'].apply(lambda x: (re.split("/",str(x))[2]))


df2 = df.copy()
cols = df2.columns.tolist()
cols = [col.replace(' ', '_') for col in cols]
cols = [col.replace('/','_') for col in cols]
df2.columns = cols


# New dataframe of just Costs:
df2 = df2.fillna(0)

df2.info()

# pd.options.display.max_columns = 10


# hist plots for costs
fig = plt.figure(figsize=(25,10))
new = np.logspace(0,7,100)

# ax1 = fig.add_subplot(341)
# ax1.set_title('Property_Damage_Costs')
# ax1.hist(df2['Property_Damage_Costs'],bins = new,color='blue',alpha=0.8)
#
# ax2 = fig.add_subplot(342)
# ax2.set_title('Lost_Commodity_Costs')
# ax2.hist(df2['Lost_Commodity_Costs'],bins = new,color='yellow',alpha=0.8)
#
# ax3 = fig.add_subplot(343)
# ax3.set_title('Public_Private_Property_Damage_Costs')
# ax3.hist(df2['Public_Private_Property_Damage_Costs'],bins = new,color='red',alpha=0.8)
#
# ax4 = fig.add_subplot(344)
# ax4.set_title('Emergency_Response_Costs')
# ax4.hist(df2['Emergency_Response_Costs'],bins = new,color='purple',alpha=0.8)
#
# ax5 = fig.add_subplot(345)
# ax5.set_title('Env_Remediation_Costs')
# ax5.hist(df2['Environmental_Remediation_Costs'],bins = new,color='black',alpha=0.8)
#
# ax6 = fig.add_subplot(346)
# ax6.set_title('Other_Costs')
# ax6.hist(df2['Other_Costs'],bins = new,color='green',alpha=0.8)

ax7 = fig.add_subplot(111)
ax7.set_title('All_Costs')
ax7.set_xlabel('Log of Cost')
ax7.set_ylabel('Frequency')
ax7.hist(df2['All_Costs'],bins = new,color='pink',alpha=0.8)


plt.savefig('costs')

# looking at causes

fig = plt.figure(figsize=(25,10))

cause_group_mean = df2.groupby('Cause_Category')['All_Costs'].mean()

cause_group_total = df2.groupby('Cause_Category')['All_Costs'].sum()

cause_group_mean.plot(kind='bar',title='Average Cost Per Cause')
plt.xticks(fontsize=13, rotation=0)
plt.xlabel('Causes')
plt.ylabel('Cost (dollars)')
plt.savefig('cause mean')
cause_group_total.plot(kind='bar',title='Total Cost Per Cause')
plt.xticks(fontsize=13, rotation=0)
plt.xlabel('Causes')
plt.ylabel('Cost (dollars)')
plt.savefig('cause total')
