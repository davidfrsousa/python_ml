import pandas as pd
import numpy as np

#df = pd.DataFrame(np.random.randn(10,4),columns=list('ABCD'))
df = pd.read_csv('data.csv')
days = pd.date_range('26/01/2022', periods=10)
df.index = days
#print(df) # print the dataframe
#print(df.index) # print indinces of dataframe
#print(df.values) # print the values of dataframe
#print(df.describe()) # print various statistics of dataframe
#print(df.mean(axis=1)) # print mean of each column (0) or row (1)
#print(df.head()) # print first 5 rows of dataframe
#print(df.tail()) # print last 5 rows of dataframe

########## SLICING BASED ON ROWS/COLUMNS #############

#print(df[['A', 'C']]) # selecting a specific column by label
#print(df[2:4]) # slicing dataframe on row number
#print(df.iloc[2:4]) # same as above
#print(df.iloc[[2,4]]) # extract rows 2 and 4 specifically (iloc's obrigatory)
#print(df.iloc[2]) # extract only row 2 (iloc's obrigatory)
#print(df.iloc[2:4, 1:4]) # extract interval of row/columns (iloc's obrigatory)
#print(df.iloc[[2,4],[1,3]]) # extract specific rows/columns (USE ILOC)

########## SLICING BASED ON LABELS ############
# Slicing by label(value) includes the end row unlike by row/column

#print(df['26/01/2022':'28/01/2022']) 
#print(df.loc['26/01/2022':'28/01/2022']) 
#print(df.loc['26/01/2022':'28/01/2022', 'A':'C']) # loc is obrigatory - interval of columns
#print(df.loc['26/01/2022':'28/01/2022', ['A','C']]) # loc is obrigatory - specific columns
#print(df.loc['29/01/2022']) # specific row - loc's obrigatory

# !!!!! Specific rows with datetime as index !!!!!
# First convert the date into a datetime format

from datetime import datetime
date1 = datetime(2022,2,1,0,0,0)
date2 = datetime(2022,1,28,0,0,0)
#print(df.loc[[date1,date2]])
#print(df.loc[date1, ['A','C']])

########## SELECTING CELLS IN DATAFRAME #############

d = datetime(2022,1,28,0,0,0)
#print(df.at[d,'B']) #print at specific cell
#print(df[(df.A > 0) & (df.B > 0)])
#print(df.transpose())
#print(df.T) # same as above, T is an accessor to transpose()

########### CHECKING IF RESULT IS SERIES OR DATAFRAME #########

def checkSeriesOrDataFrame(var):
    if isinstance(var, pd.DataFrame):
        return 'Dataframe'
    if isinstance(var, pd.Series):
        return 'Series'

#print(checkSeriesOrDataFrame(df.A))
#print(checkSeriesOrDataFrame(df.T))

########### SORTING DATAFRAME ###############

#print(df.sort_index(axis=1, ascending=False)) # sort column in descending order, does NOT affect original Dataframe
#print(df.sort_values('A', axis=0)) # sort column A by values
#print(df.sort_values('29/01/2022', axis=1)) # sort row from selected index in ascending order

########### APPLY FUNCTIONS TO DATAFRAME #############

import math

sq_root = lambda x: math.sqrt(x) if x > 0 else x
sq = lambda x: x**2

#print(df.B.apply(sq_root))
#print(df.apply(sq))
for column in df:
    df[column] = df[column].apply(sq_root)
#print(df)

print(df.apply(np.sum, axis=1))