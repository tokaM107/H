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






