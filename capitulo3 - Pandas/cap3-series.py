import pandas as pd

#series = pd.Series([1,2,3,4,5])
series = pd.Series([1,2,3,4,5],index=['a','b','c','d','c']) #NOT unique indices are VALID
#print(series[2])
print(series.iloc[2]) #same as series[2]

#print(series['d'])
print(series.loc['d']) #same as series['d']

print(series['c']) #returns another series resulted from doubled indices

print(series[2:]) #slicing the series returns another series
print(series.iloc[2:]) #same as above

#dates1 = pd.date_range('26/01/2022', periods=12, freq='M') # end of each month
#dates1 = pd.date_range('26/01/2022', periods=12, freq='MS') # start of each month
dates1 = pd.date_range('26/01/2022 14:00:00', periods=12, freq='H') # hourly
print(dates1)

series1 = pd.Series([1,2,3,4,5,6,7,8,9,10,11,12])
series1.index = dates1
print(series1)
