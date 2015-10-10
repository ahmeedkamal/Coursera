# -*- coding: utf-8 -*-
"""
This is a script in the scope of 
data analysis specialization
"""
# imports
import pandas
import numpy

# data extraction
aData = pandas.read_csv('ool_pds.csv')

#for column in aData.columns:
#    print column
    
print "Number of columns: " + str(len(aData.columns))
print "Number of lines: " + str(len(aData.index))

print ("================================\n"
       "======= Race/Ethnicity =========\n"
       "================================")

#select subdata for people 18-25 years old
aSubData = aData[(aData['PPAGE'] <= 25) & (aData['PPAGE'] >= 18)]

print "Histogram of ages:"
ageHisto = aSubData.groupby("PPAGE").size()
print ageHisto

print "Histogram of political choices:"
choiceHisto = aSubData.groupby("W1_C1").size()
print choiceHisto

print "Histogram of race:"
raceHisto = aSubData.groupby("PPETHM").size()
print raceHisto

# Want to compute the percentages using both methods
aTotalNumber = len(aSubData.index)
print "Total number of people 18-25 years: " + str(aTotalNumber)

aWhiteNumber = float(len(aSubData[(aSubData['PPETHM'] == 1)].index))
print "Percentage of White people: " + str(aWhiteNumber/aTotalNumber)

aBlackPercent = aSubData['PPETHM'].value_counts(sort=False, normalize=True)[2]
print "Percentage of Black people: " + str(aBlackPercent)

aHispanicPercent = aSubData['PPETHM'].value_counts(sort=False, normalize=True)[4]
print "Percentage of Hispanic people: " + str(aHispanicPercent)

aOtherPercent = aSubData['PPETHM'].value_counts(sort=False, normalize=True)[3]
print "Percentage of Other people: " + str(aOtherPercent)

aMixedPercent = aSubData['PPETHM'].value_counts(sort=False, normalize=True)[5]
print "Percentage of Mixed people: " + str(aMixedPercent)

print ("================================\n"
       "====== Political choices =======\n"
       "================================")
       
# Political preferences
print "Histogram of political choices: "
print  aSubData['W1_C1'].value_counts(sort=False, normalize=True)       
       
aRepublican = aSubData['W1_C1'].value_counts(sort=False, normalize=True)[1]
print "Percentage of Republicans: " + str(aRepublican)

aDemocrat = aSubData['W1_C1'].value_counts(sort=False, normalize=True)[2]
print "Percentage of Democrats: " + str(aDemocrat)

aIndependent = aSubData['W1_C1'].value_counts(sort=False, normalize=True)[3]
print "Percentage of Independents: " + str(aIndependent)

aOther = aSubData['W1_C1'].value_counts(sort=False, normalize=True)[4]
print "Percentage of Others: " + str(aOther)

aNoResponse = aSubData['W1_C1'].value_counts(sort=False, normalize=True)[-1]
print "Percentage of N/A respones: " + str(aNoResponse)

# Race/Etchinicity of Democrats
aDemocratRows =  aSubData[aSubData['W1_C1'] == 2].index
print aSubData[aSubData.index.isin(aDemocratRows.values)].groupby('PPETHM').size()

aDemocratData = aSubData[aSubData['W1_C1'] == 2]
print "Histogram of ethnicities of democratic party voters:"
print aDemocratData['PPETHM'].value_counts(sort=False, normalize=True)

# This shows that 79% of young(18-25) democratic party voters are black ! Impressive !! 
