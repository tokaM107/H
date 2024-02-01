# import pyarrow 
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
# Load  dataset
df = pd.read_csv('/Users/tokamohamed/Downloads/Salaries.csv')
from scipy import stats

#data explor

#print(df.info())

#print(df.isnull().sum())
# print( "Mean of totalPay : " , np.mean(df.loc[:,"TotalPay"])) #mean
# print("Median of totalPay : " , np.median(df.loc[:,"TotalPay"]))
# print("Max of totalPay: ", np.max(df.loc[:,"TotalPay"]))
# print("Min totalPay: " ,np.min(df.loc[:,"TotalPay"]))
# print("Mode of tatalPay:",  stats.mode(df.loc[:,"TotalPay"]))
# print("Standered deviation", np.std(df.loc[:,"TotalPay"]))
# print("Range of salaries: " ,np.ptp(df.loc[:,"TotalPay"]))


#data cleaning

#remove duplicates

# print(df.drop_duplicates(inplace = True))
# print(df.duplicated())


#remove base salary less than or equal zero
# for x in df.index:
#   if df.loc[x, "BasePay"] <= 0:
#     df.drop(x, inplace = True)
# df.to_csv('/Users/tokamohamed/Downloads/Salaries.csv', index=False)


# for x in df.index:
#     if df.loc[x, "BasePay"] <= 0 or df.loc[x, "OtherPay"] < 0 or df.loc[x, "OvertimePay"] < 0:
#       df.drop(x, inplace=True)
# df.to_csv('/Users/tokamohamed/Downloads/Salaries.csv', index=False)


# remove rows contains empty cells
# df.dropna(inplace= True)
# df.to_csv('/Users/tokamohamed/Downloads/Salaries.csv', index=False)

# print(df.info())



#remove notes , statue columes
# ndf=df.drop(["Notes" , "Status"], axis='columns')
# ndf.to_csv('/Users/tokamohamed/Downloads/Salaries.csv', index=False)


# filling null benefit values with 0
# ndf=df.fillna( {"Benefits" : 0})
# ndf.to_csv('/Users/tokamohamed/Downloads/Salaries.csv', index=False)




# data visulization

#histogram of salaries
# sns.histplot(data=df, x="TotalPay" , bins=25)
# plt.xlim(15.5, 567595.43)
# plt.show()



#piechart of jobtitles
# job_counts = df['JobTitle'].str.lower().value_counts()
# top_n = 10  
# top_departments = job_counts.head(top_n)
# plt.pie(top_departments, labels=top_departments.index, autopct='%1.1f%%')
# plt.title("Proportion of Employees in Top 10 Departments")
# plt.show()

#department
# df['dep'] = df['JobTitle'].str.extract(r'(\w+)\s+DEPARTMENT')
# df.to_csv('/Users/tokamohamed/Downloads/Salaries.csv', index=False)

# df['dep'] = df['dep'].str.replace('OF', 'FIRE')
# df.to_csv('/Users/tokamohamed/Downloads/Salaries.csv', index=False)

# dep_counts = df['dep'].value_counts()
# plt.pie(dep_counts, labels=dep_counts.index, autopct='%1.1f%%')
# plt.title("Proportion of Employees in Departments")
# plt.show()


#grouping

# grouped_data = df.groupby(['Year'])['TotalPay'].agg(['count', 'mean', 'median', 'min', 'max', 'std'])

# # Print the grouped data
# print(grouped_data)



#corelation
# plt.scatter(df['BasePay'], df['TotalPay'])
# plt.xlabel('Base pay')
# plt.ylabel('total pay')
# plt.title('Scatter Plot: total pay vs Base pay')
# plt.show()


# plt.scatter(df['TotalPay'], df['TotalPayBenefits'])
# plt.xlabel('total pay')
# plt.ylabel('total pay with benefits')
# plt.title('Scatter Plot: total pay vs total pay benefits')
# plt.show()

