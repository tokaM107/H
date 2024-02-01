# ShAI-BootCampAssigment-DataScience
## 1- Data exoploration
### Tasks:
#### 1.Identify the number of rows and columns in the dataset.
#### 2.Determine the data types of each column,
#### 3.Missing values in each column.
### Solution 
#### To make data exploration, first I imported nessary libraries as pandas and numpy:
```
Import pandas as pd
Import numpy as nd
```
#### Then I used pandas library method `read_cvs` to read dataset file:
```
df = pd.read_csv('Salaries.csv')
```
#### To identify number of rows and columes , I used the method `info()` to get the dataset information 
```
print(df.info())
```
##### Data has RangeIndex (rows): 148654 entries, 0 to 148653 ,Data columns (total 13 columns):
##### Data type of each column
| # | Column           |Non-Null Count  | Dtype | 
|---| ------           | -------------- | ----- |
|0  | Id               |148654 non-null |int64  |
|1  | EmployeeName     |148654 non-null |object |
| 2 | JobTitle         |148654 non-null |object |
| 3 | BasePay          |148045 non-null |float64|
|4  | OvertimePay      |148650 non-null |float64|
|5  | OtherPay         |148650 non-null |float64|
|6  | Benefits         |112491 non-null |float64|
|7  | TotalPay         |148654 non-null |float64|
|8  | TotalPayBenefits |148654 non-null |float64|
|9  | Year             |148654 non-null |int64  |
|10 | Notes            |0 non-null      |float64|
|11 | Agency           |148654 non-null |object |
|12 | Status           |0 non-null      |float64|

##### dtypes: float64(8), int64(2), object(3) ,memory usage: 14.7+ MB

#### Missing values : to check for missing values in each colume I used the method `isnull().sum() `to know the count of missing values for each column.
columnName       |    countofmissingvalues 
----------       |     -----------------
Id               |        0
EmployeeName     |        0
JobTitle         |        0
BasePay          |      609
OvertimePay      |        4
OtherPay         |        4
Benefits         |   36163
TotalPay         |       0
TotalPayBenefits |       0
Year             |       0
Notes            |  148654
Agency           |       0
Status           |   148654

##### dtype: int64
## 2. Descriptive Statistics:
### Tasks:
#### 1. Calculate basic statistics mean, median, mode, minimum, and maximum salary, determine the range of salaries, and find the standard deviation.
### Solution 
##### Mean: The sum of the values by adding them all up. Divide the sum by the number of values in the data set. 
##### I used the method ` np.mean() ` from numpy library to calculate mean. then i accessed colume in dataset by this method ` df.loc[:,"TotalPay"] `
```
print( "Mean of totalPay : " , np.mean(df.loc[:,"TotalPay"])) 
```
```
Mean of totalPay :  74768.32197169267
```
##### Median: the average of the two middle numbers by adding them together and dividing the sum by two.
##### I used the method ` np.median() ` .
```
print("Median of totalPay :" , np.median(df.loc[:,"TotalPay"]))
```
```
Median of totalPay :  71426.60999999999
```
##### Mode is the most frequnct element 
##### I used stats libarary from scipy to calculate mode ` from scipy import stats `
```
print( stats.mode(df.loc[:,"TotalPay"]))
```
```
ModeResult(mode=0.0, count=368)
```
##### To calculate min salary I used ` Min() ` method 
```
print("Min totalPay: " ,np.min(df.loc[:,"TotalPay"]))
```
```
Min totalPay:  -618.13
```
##### To calculate max salary i used ` Max() ` method 
```
print("Max of totalPay: ", np.max(df.loc[:,"TotalPay"]))
```
```
Max of totalPay:  567595.43
```
##### To calculate the range of salaries I used method ` ptp() `. This method calaculate range by substracting min salary from max salary 
```
print("Range of salaries: " np.ptp(df.loc[:,"TotalPay"]))
```
##### Standered deviation: the measure of the amount of variation of a random variable expected about its mean.
##### I used the method ` std() ` 
```
print("Standered deviation", np.std(df.loc[:,"TotalPay"]))
```
```
Standered deviation 50516.83535894512
```
## 3. Data cleaning 
### Tasks:
#### 1. Handle missing data by suitable method with explain why you use it.
### Solution: 
#### for Duplicated rows I used the method ` df.duplicated() ` to show if there duplicated rows or not But the data has no duplicated rows as it returns false for all rows.
``` print(df.duplicated()) ```
 ``` 
0         False
1         False
2         False
3         False
4         False
          ...  
146726    False
146727    False
146728    False
146729    False
146730    False

```
#### Then I removed notes and statue column as cells are empty and not effective in calculations. I used `drop()` method when prameter `axis='columns'` to drop columns.
```
ndf=df.drop(["Notes" , "Status"], axis='columns')
ndf.to_csv('Salaries.csv', index=False)
```

#### then I replaced null values in ` benefits ` column with zeros as I noticed that in ` totalpaybenefits ` column = ` totalpay` when ` benefits = null `. 
`<img width="899" alt="Screenshot 2024-01-30 at 2 36 56 PM" src="https://github.com/tokaM107/ShAI-BootCampAssigment-DataScience/assets/157342095/4910f05f-0d01-4d48-8809-07ba474a0f4d">
```
ndf=df.fillna( {"Benefits" : 0})
ndf.to_csv('Salaries.csv', index=False)
```

#### then i worked on empty cells in each row and removed them by ` dropna() ` method
<img width="899" alt="image" src="https://github.com/tokaM107/ShAI-BootCampAssigment-DataScience/assets/157342095/8021aa18-7641-4e47-a2bf-5342f182666c">

```
df.dropna(inplace= True)
df.to_csv('Salaries.csv', index=False)
```
#### after that, I worked on wrong data, I removed base salary that is less than or equal zero, I assumed that all employee works in the company have base salary so zeros or negative salaries are wrong data. also, I removed negative values from ` otherpay ` , ` overtimepay ` and ` totalpay ` as I assumed nevative values are wrong data.
<img width="899" alt="Screenshot 2024-01-30 at 3 03 03 PM" src="https://github.com/tokaM107/ShAI-BootCampAssigment-DataScience/assets/157342095/5a20477e-451e-4749-9198-66ff010e988a">

```
for x in df.index:
     if df.loc[x, "BasePay"] <= 0 or df.loc[x, "OtherPay"] < 0 or df.loc[x, "OvertimePay"] < 0 or df.loc[x, "totalPay"]:
       df.drop(x, inplace=True)
df.to_csv('Salaries.csv', index=False)
```

#### This is a sample of data after cleaning 
<img width="708" alt="image" src="https://github.com/tokaM107/ShAI-BootCampAssigment-DataScience/assets/157342095/e17bdabf-f9a3-4bf2-b4d1-8bf5087ccb5d">

#### finally, i repeated the same process 1,2 for the data after cleaning and i got this results: 
` print(df.info())`
```
RangeIndex: 146731 entries, 0 to 146730
Data columns (total 11 columns):
 #   Column            Non-Null Count   Dtype  
---  ------            --------------   -----  
 0   Id                146731 non-null  int64  
 1   EmployeeName      146731 non-null  object 
 2   JobTitle          146731 non-null  object 
 3   BasePay           146731 non-null  float64
 4   OvertimePay       146731 non-null  float64
 5   OtherPay          146731 non-null  float64
 6   Benefits          146731 non-null  float64
 7   TotalPay          146731 non-null  float64
 8   TotalPayBenefits  146731 non-null  float64
 9   Year              146731 non-null  int64  
 10  Agency            146731 non-null  object 
dtypes: float64(6), int64(2), object(3)
memory usage: 12.3+ MB
```
```
 print( "Mean of totalPay : " , np.mean(df.loc[:,"TotalPay"])) #mean
 print("Median of totalPay : " , np.median(df.loc[:,"TotalPay"]))
 print("Max of totalPay: ", np.max(df.loc[:,"TotalPay"]))
 print("Min totalPay: " ,np.min(df.loc[:,"TotalPay"]))
 print("Mode of tatalPay:",  stats.mode(df.loc[:,"TotalPay"]))
 print("Standered deviation", np.std(df.loc[:,"TotalPay"]))
 print("Range of salaries: " ,np.ptp(df.loc[:,"TotalPay"]))
```
```
Mean of totalPay :  75686.63794317494
Median of totalPay :  72094.12
Max of totalPay:  567595.43
Min totalPay:  15.5
Mode of tatalPay: ModeResult(mode=18594.0, count=82)
Standered deviation 50175.3248206361
Range of salaries:  567579.93
```
``` print(df.isnull().sum()) ```
```
Id                  0
EmployeeName        0
JobTitle            0
BasePay             0
OvertimePay         0
OtherPay            0
Benefits            0
TotalPay            0
TotalPayBenefits    0
Year                0
Agency              0
dtype: int64
```
## 4. Basic Data Visualization: 
### tasks:
#### 1.Create histograms or bar charts to visualize the distribution of salaries,
#### 2.use pie charts to represent the proportion of employees in different departments.
##### i used seaborn and matplotlib libraries to represent graphs


##### histogram of distribution of salaries:
![Figure_1](https://github.com/tokaM107/ShAI-BootCampAssigment-DataScience/assets/157342095/79a3d941-b29b-4584-a536-303b737b61f0)

```
#histogram of salaries
sns.histplot(data=df, x="TotalPay" , bins=25)
plt.xlim(15.5, 567595.43)
plt.show()

```

##### there is no column for departments, so i found in the jobtitle column departments but it need to some operations to represent it as a pie chart: 
##### first i used the method ` extract() ` to get the word after " department"

```
 df['dep'] = df['JobTitle'].str.extract(r'(\w+)\s+DEPARTMENT')
 df.to_csv('/Users/tokamohamed/Downloads/Salaries.csv', index=False)
```

##### then i had a wrong department classfication as data have few lines like this: ` CHIEF OF DEPARTMENT, (FIRE DEPARTMENT) ` the method gives "OF" as a result. so i had to replace all "OF" values to "FIRE" 
```
 df['dep'] = df['dep'].str.replace('OF', 'FIRE')
 df.to_csv('/Users/tokamohamed/Downloads/Salaries.csv', index=False)
```
##### after that, i made the pie chart to represent employee departments proportions
```
dep_counts = df['dep'].value_counts()
plt.pie(dep_counts, labels=dep_counts.index, autopct='%1.1f%%')
plt.title("Proportion of Employees in Departments")
plt.show()
```
![image](https://github.com/tokaM107/ShAI-BootCampAssigment-DataScience/assets/157342095/cd375db3-371a-4f69-ae2b-152ed91fb210)

##### pie chart represents employee percentage for the top 10 jobtitles: 
###### the chart represents the top 10 as the data is very big 
![image](https://github.com/tokaM107/ShAI-BootCampAssigment-DataScience/assets/157342095/ecffea54-5653-4f11-8ef0-cd8aa5a721f3)

```
#piechart of jobtitles
job_counts = df['JobTitle'].str.lower().value_counts()
top_n = 10  
top_departments = job_counts.head(top_n)
plt.pie(top_departments, labels=top_departments.index, autopct='%1.1f%%')
plt.title("Proportion of Employees in Top 10 Departments")
plt.show()
```

##### also, departments can be classfiy as the years 
![image](https://github.com/tokaM107/ShAI-BootCampAssigment-DataScience/assets/157342095/305ff579-39ab-4b3e-ac12-0fc688897828)

## 5. Grouped Analysis: 
### Tasks: 
#### 1.Group the data by one or more columns
#### 2.calculate summary statistics for each group,
#### 3.compare the average salaries across different groups.
### solution
#### In groubing data, I used ` groupby() ` method for grouping data accourding to ` Year ` column. 
```
df.groupby(['Year'])
```
#### to calculate summary statistics for each group i used `agg() ` method to calculate mean, median, min, max, std ,count 
```
['TotalPay'].agg(['count', 'mean', 'median', 'min', 'max', 'std']
```

```
grouped_data = df.groupby(['Year'])['TotalPay'].agg(['count', 'mean', 'median', 'min', 'max', 'std'])
print(grouped_data)
```

```
      count      mean       median    min        max           std
Year                                                               
2011  35707  72595.460609  68813.14  17.78  567595.43  47168.232508
2012  36335  74928.282957  71246.55  23.08  362844.66  49212.026306
2013  36996  78810.654705  75254.37  15.83  347102.32  52412.220534
2014  37693  76279.728792  72951.66  15.50  471952.64  51406.677417
```
#### in group 1 (2011) the ave salary was 72595.460609, group 2 (2012) the ave salary was 74928.282957 , group 3 (2013) the ave salary was 78810.654705 , group 4 (2014) the ave salary was 76279.728792 


## 6. Simple Correlation Analysis:
### tasks:
#### Identify any correlation between salary and another numerical column, and plot a scatter plot to visualize the relationship.
### solution 
#### there is a postive relationship between totalpay and totalpaybenefits column as when total pay increases , totalpaybenefits increases.
```
plt.scatter(df['TotalPay'], df['TotalPayBenefits'])
plt.xlabel('total pay')
plt.ylabel('total pay with benefits')
plt.title('Scatter Plot: total pay vs total pay benefits')
plt.show()
```
![image](https://github.com/tokaM107/ShAI-BootCampAssigment-DataScience/assets/157342095/8eed0bf5-8944-4e2b-adaa-20910d7a08aa)

#### alse, there is a positive relationship between basepay and total pay 
```
plt.scatter(df['BasePay'], df['TotalPay'])
plt.xlabel('Base pay')
plt.ylabel('total pay')
plt.title('Scatter Plot: total pay vs Base pay')
plt.show()
```
![image](https://github.com/tokaM107/ShAI-BootCampAssigment-DataScience/assets/157342095/90b5e16b-e002-494b-a90b-f185747b9487)

## 7. Summary of Insights:
#### Write a brief report summarizing the findings and insights from the analyses.
##### Dataset shows employees salaries and names. It has 13 columns and 148654 rows. Data has columns ‘Id’, EmployeeName’, ‘JobTitle’, ‘BasePay’, OvertimePay’, OtherPay, ’Benefits’’, TotalPay' -> salary, TotalPayBenefits, ’Year’, Notes’, Agency , ’Status’. 
##### First of all, I calculated the basic statistics: mean , mode, median, max, min, std. After that, I cleaned the data by removing duplicated values and negative values. Then , I removed notes and statues column as they not effective. And remove base salary less than or equal zero as all employees not have base salary not work in the company. For data visualization, I used seaborn and matplotlib libraries to make graphs. The challenge I faced that there is no department column, so I spliced the column “job title ” to 3 main departments : fire , police , services and made pie chart. Then in grouping data, I classified data set according to “year” and calculated basic statistics and average salaries for each group. Then I made simple correlation between total pay and total pay benefits and they have positive relationship. 












