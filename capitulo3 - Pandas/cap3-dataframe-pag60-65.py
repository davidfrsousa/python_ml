import pandas as pd
import numpy as np

data = {'name': ['Janet', 'Nad', 'Timothy', 'June', 'Amy'],
        'year': [2012,2012,2013,2014,2014],
        'reports': [6,13,14,1,7]}

#df = pd.DataFrame(data, index=['Singapore', 'China', 'Japan', 'Sweden', 'Norway'])

schools = np.array(['Cambridge', 'Oxford', 'Oxford', 'Cambridge', 'Oxford'])
#df['school'] = schools

####### REMOVING ROWS ########### 

#print(df.drop(['China', 'Japan'])) # remove rows based on index value
#print(df[df.name != 'Nad']) # remove rows based on column value 
#print(df.drop(df.index[1])) # remove row based on row number, same as df.drop['China'] / df.index[1] = 'China'
#print(df.drop(df.index[[1,2]])) # remove multiple rows based on row number
#print(df.drop(df.index[-2]))

######### REMOVING COLUMNS ##########
# Set drop paramenter axis to 1

#print(df.drop('reports', axis=1)) # remove columns by name
#print(df.drop(df.columns[2], axis=1)) # remove columns by column number using indexer 'columns'
#print(df.drop(df.columns[[2,3]], axis=1)) # remove multiple columns

df = pd.DataFrame({
    'Gender': ['Male', 'Male', 'Female', 'Female', 'Female'],
    'Team': [1,2,3,3,1]
})
#print(df)

print('Displaying the distribution of genders in each team')
print(pd.crosstab(df.Team, df.Gender))