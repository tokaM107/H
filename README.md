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
df = pd.read_csv('/Users/tokamohamed/Downloads/Salaries.csv')
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











