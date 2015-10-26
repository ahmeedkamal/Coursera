# -*- coding: utf-8 -*-
"""
This is a script in the scope of 
data analysis specialization
"""
# imports
import pandas
import numpy
import seaborn
import matplotlib.pyplot as pyplot

# data extraction
aData = pandas.read_csv('ool_pds.csv')

#for column in aData.columns:
#    print column

###################################################
##################### WEEK 2 ######################
###################################################
    
#print "Number of columns: " + str(len(aData.columns))
#print "Number of lines: " + str(len(aData.index))
#
#print ("================================\n"
#       "======= Race/Ethnicity =========\n"
#       "================================")

##select subdata for people 18-25 years old
aSubData = aData[(aData['PPAGE'] <= 25) & (aData['PPAGE'] >= 18)]
#
#print "Histogram of ages:"
#ageHisto = aSubData.groupby("PPAGE").size()
#print ageHisto
#
#print "Histogram of political choices:"
#choiceHisto = aSubData.groupby("W1_C1").size()
#print choiceHisto
#
#print "Histogram of race:"
#raceHisto = aSubData.groupby("PPETHM").size()
#print raceHisto
#
## Want to compute the percentages using both methods
#aTotalNumber = len(aSubData.index)
#print "Total number of people 18-25 years: " + str(aTotalNumber)
#
#aWhiteNumber = float(len(aSubData[(aSubData['PPETHM'] == 1)].index))
#print "Percentage of White people: " + str(aWhiteNumber/aTotalNumber)
#
#aBlackPercent = aSubData['PPETHM'].value_counts(sort=False, normalize=True)[2]
#print "Percentage of Black people: " + str(aBlackPercent)
#
#aHispanicPercent = aSubData['PPETHM'].value_counts(sort=False, normalize=True)[4]
#print "Percentage of Hispanic people: " + str(aHispanicPercent)
#
#aOtherPercent = aSubData['PPETHM'].value_counts(sort=False, normalize=True)[3]
#print "Percentage of Other people: " + str(aOtherPercent)
#
#aMixedPercent = aSubData['PPETHM'].value_counts(sort=False, normalize=True)[5]
#print "Percentage of Mixed people: " + str(aMixedPercent)
#
#print ("================================\n"
#       "====== Political choices =======\n"
#       "================================")
#       
## Political preferences
#print "Histogram of political choices: "
#print  aSubData['W1_C1'].value_counts(sort=False, normalize=True)       
#       
#aRepublican = aSubData['W1_C1'].value_counts(sort=False, normalize=True)[1]
#print "Percentage of Republicans: " + str(aRepublican)
#
#aDemocrat = aSubData['W1_C1'].value_counts(sort=False, normalize=True)[2]
#print "Percentage of Democrats: " + str(aDemocrat)
#
#aIndependent = aSubData['W1_C1'].value_counts(sort=False, normalize=True)[3]
#print "Percentage of Independents: " + str(aIndependent)
#
#aOther = aSubData['W1_C1'].value_counts(sort=False, normalize=True)[4]
#print "Percentage of Others: " + str(aOther)
#
#aNoResponse = aSubData['W1_C1'].value_counts(sort=False, normalize=True)[-1]
#print "Percentage of N/A respones: " + str(aNoResponse)
#
## Race/Etchinicity of Democrats
#aDemocratRows =  aSubData[aSubData['W1_C1'] == 2].index
#print aSubData[aSubData.index.isin(aDemocratRows.values)].groupby('PPETHM').size()
#
#aDemocratData = aSubData[aSubData['W1_C1'] == 2]
#print "Histogram of ethnicities of democratic party voters:"
#print aDemocratData['PPETHM'].value_counts(sort=False, normalize=False)
#
## This shows that 79% of young(18-25) democratic party voters are black ! Impressive !! 



###################################################
##################### WEEK 3 ######################
###################################################

#select subdata for people 18-25 years old
aSubData = aData[(aData['PPAGE'] <= 25) & (aData['PPAGE'] >= 18)]

# Replace missing data (-1 represents "Refused") with NaN
print aSubData['W1_C1'].value_counts(sort=False, dropna=False)
#aSubData['W1_C1'] = aSubData['W1_C1'].replace(-1, numpy.nan)
aSubData = aSubData[aSubData['W1_C1'] != -1]
print "Histogram of political choices after replacing missing data:"
print aSubData['W1_C1'].value_counts(sort=False, dropna=False)
 

# Replace missing data in IDs with a valid number not already used

print aSubData['W2_CASEID2'].value_counts(sort=True, dropna=False)
newIDs = list()
def validID(row):
    num = 2
    if row['W2_CASEID2'] == " ":
        while str(num) in aSubData['W2_CASEID2'].values or num in newIDs:
            num += 1
        newIDs.append(num)
        return num
    else:
        return row['W2_CASEID2']

aSubData['W2_CASEID2'] = aSubData.apply(lambda row: validID(row), axis=1)

print "Histogram of W1_C2 after filling missing data with valid data:"
print aSubData['W2_CASEID2'].value_counts(sort=True, dropna=False)
print "#######################"
print aSubData['W1_C1B'].value_counts(sort=True, dropna=False)
# Replace missing data (-1  and .) with NaN
aSubData['W1_C1B'] = aSubData['W1_C1B'].replace(-1, numpy.nan)
aSubData['W1_C1B'] = aSubData['W1_C1B'].replace('.', numpy.nan)
aSubData = aSubData[aSubData['W1_C1B'] != numpy.nan]

print "Histogram of W1_C1B after coding in valid data:"
print aSubData['W1_C1B'].value_counts(sort=True, dropna=False)

# for W1_C2, we will divide the values to 3 large groups 
# Liberal (1)/Moderate (2)/Conservative (3)
# We will also replace missing data with NaN

print aSubData['W1_C2'].value_counts(sort=True, dropna=False)
regroup = {1:1, 2:1, 3:1, 4:2, 5:3, 6:3, 7:3}#, -1:numpy.nan}
aSubData['W1_C2'] = aSubData['W1_C2'].map(regroup)
#aSubData = aSubData[aSubData['W1_C2'] != -1]

print "Histogram of W1_C2 after grouping:"
print aSubData['W1_C2'].value_counts(sort=True, dropna=False)

###################################################
##################### WEEK 4 ######################
###################################################

aSubData['W1_C1B'] = aSubData['W1_C1B'].convert_objects(convert_numeric=True)
aSubData['W1_C1'] = aSubData['W1_C1'].convert_objects(convert_numeric=True)
aSubData['PPAGE'] = aSubData['PPAGE'].convert_objects(convert_numeric=True)
aSubData['W1_C2'] = aSubData['W1_C2'].convert_objects(convert_numeric=True)

#Display a participants age plot
pyplot.xlabel('Political choices of participants')
pyplot.ylabel('# of participants')
seaborn.distplot(aSubData['W1_C2'], kde=False)

Display a political choices plot for participants (12-25)
pyplot.xlabel('Political choices')
pyplot.ylabel('# of participants aged 18-25')
seaborn.distplot(aSubData['W1_C1'], kde=False)

seaborn.factorplot(x='W1_C1', y='PPAGE', data=aSubData, kind='bar', ci=None)