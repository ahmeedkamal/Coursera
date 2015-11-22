import pandas
import scipy.stats
import seaborn
import matplotlib.pyplot as pyplot

aData = pandas.read_csv('ool_pds.csv', low_memory=False)

# W1_D1: how would you rate obama
# W1_D11: how would you rate the republican party
# W1_D12: how would you rate the democratic party
# invalid data -1 and 998
# PPAGE: age
aSubData = aData[['PPAGE' , 'W1_A11']]

aSubData = aSubData[(aSubData['W1_A11']!= -1)]

print ('Association between Obama rate and the age of participants: ')
print (scipy.stats.pearsonr(aSubData['PPAGE'], aSubData['W1_A11']))

aPlot = seaborn.regplot(x='PPAGE', y='W1_A11', fit_reg=True, data=aSubData)
pyplot.xlabel('Age of participants')
pyplot.ylabel('Frequency of watching national news ? ')
pyplot.title('''ScatterPlot for the association between the age 
                and the frequency of watching the national news''')