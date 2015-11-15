import pandas
import scipy.stats

aData = pandas.read_csv('ool_pds.csv', low_memory=False)

# extract only race and the preferred political party
## PPETHM: White(1), Black(2), Other(3), Hispanic(4), Mixed(5)
aSubData = aData[['PPETHM' , 'W1_C2']]
## W1_C2: Liberal(1-3), Moderate(4), Conservative(5-7)
regroup = {1:'Liberal', 2:'Liberal', 3:'Liberal', 4:'Moderate',
           5:'Conservative', 6:'Conservative', 7:'Conservative'}
aSubData['W1_C2'] = aSubData['W1_C2'].map(regroup)


levels = range(1,6)
for n in levels:
    for m in levels:
        if n < m:
            print "=========== (" + str(n) + ", " + str(m) + ") ============="
            
            aPartialData = aSubData[(aSubData['PPETHM'] == n) | (aSubData['PPETHM'] == m)]
            # contingency table of observed counts
            contingency = pandas.crosstab(aPartialData['W1_C2'], aPartialData['PPETHM'])
            print (contingency)
            
            # column %
            col_sum = contingency.sum(axis=0)
            col_percent = contingency/col_sum
            print (col_percent)
            
            # chi_square 
            print ('chi-square value, p-value, expected counts')
            chi_square = scipy.stats.chi2_contingency(contingency) 
            print (chi_square)























