import pandas
import scipy.stats
import seaborn
import matplotlib.pyplot as pyplot

aData = pandas.read_csv('ool_pds.csv', low_memory=False)

# W1_A11: Frequency of watching national news
# invalid data -1 
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
