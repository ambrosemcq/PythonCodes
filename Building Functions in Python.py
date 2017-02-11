# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 09:06:48 2017

@author: Home
"""
#%%
#A function is a three-step process: Input, Transformation, Output
def converterToCelsius(valueInFarenheit): #input: creating functions in Python requires the use of def followed by the name of the function; the function arguments continue between parenthesis
    #transformation
    resultInCelsius= (valueInFarenheit-32)*5/9
    #output
    return resultInCelsius
converterToCelsius(100)
#%%
#From above, creating functions in Python requires the use of def followed by the name of the function; the function arguments continue between parenthesis
def XsumY(valueX,valueY):
    ###
    resultSum=valueX+valueY
    ###
    return resultSum
XsumY(3,10)
def riseToPower(base,exponent=2): # two argument names!!!
    ###
    result=1
    if exponent > 0:
        for time in range(1,exponent+1): # use 'exponent + 1'...!
            result=result*base
    ###
    return(result)
riseToPower(9)
riseToPower(9,3)
riseToPower(9,0)
#%%
# for sure you can use the arguments name:
riseToPower(base=9,exponent=0)
# using arguments names does not require order:
riseToPower(exponent=0,base=9)
#%%
#Homework
def riseToPowerPlus(base,exponent=2): # two argument names!!!
    ###
    result=1
    if exponent > 0:
        for time in range(1,exponent+1): # use 'exponent + 1'...!
            result=result*base
    else: 
        for time in range(1*-1,exponent+1):
            result=result*base
    ###
    return(result)
riseToPower(-9)
riseToPower(-4)
3/0
#Division by zero error
#%%
# Then
def divRounded(numerator,denominator,precision=2):
    try:
        result = numerator/denominator
        return round(result, precision)
    except ZeroDivisionError:
        print('You can not use 0 as the denominator')
        # testing:
n=13
d=12
p=5
divRounded(n,d,p)
inputArgs=[13,12,5] # order matters, keep it.
divRounded(*inputArgs)
inputArgs={'numerator':13, 'precision':5,'denominator':12} # order does not matter
divRounded(**inputArgs)
#%%
# one input, and several output in simple data structure:
#Homework
#Change the function ’factors’to reduce the amount of iterations in the for loop and still get the factors shown above.
def factors(number):
    factorsList=[] # empty list that will collect output

    for i in range(1, int(number/2)):
        #if the remainder of 'number'/'i' equals zero...
        if number % i == 0:
            # ...add 'i' to the list of factors!
            factorsList.append(i)
    return (factorsList,number) # returning  values in a list.
factors(20)
#%%
#Change your new function ‘factors’ to negative values or zeros as input; your code should return a message if an invalid value was input.
def factors1(number):
    factorsList=[] # empty list that will collect output
    for i in range(1, number+1):
        #if the remainder of 'number'/'i' equals zero...
        if i < 0:
            factorsList.append(-i)
        if i ==0:
            print('does not accept zero')
        if number % i == 0:
            # ...add 'i' to the list of factors!
            factorsList.append(i)
            continue
    return (factorsList) # returning  values in a list
factors1(20)
#%%
#Change your newest function ‘factors’ to accept only positive integer values; your code should return a message if an invalid valid was input.
#NEED HELP
def factors(number):
    factorsList=[] # empty list that will collect output
    for i in range(1, number+1):
        # if I have a zero or negative value:
        if number < 0: # if I have a zero or negative value:
            print('does not accept negative values') #   return a message bad input
        if ZeroDivisionError:
            print('You can not use 0 as the denominator')
            continue 
        if number = np.isnan #if the value is not an integer
            print('value is not a number') #return a message of bad input
    # else: do the same as before...
        else:
            number % i == 0:
            # ...add 'i' to the list of factors!
            factorsList.append(i)
        
    return (factorsList) # returning  values in a list
factors(20)
#%%
#Now, make your newest function 'resistant' to missing values of any kind.
#NEED HELP
import numpy as np
def factors(number):
    factorsList=[] # empty list that will collect output
    for i in range(1, number+1):
        #if the remainder of 'number'/'i' equals zero...
        if number < 0:
            print('does not accept negative values')
        if ZeroDivisionError:
            print('You can not use 0 as the denominator')
            continue
        if number==None: # condition1
            print ('missing values as input')
            continue
        else:
            number % i == 0:
            # ...add 'i' to the list of factors!
            factorsList.append(i)
    return (factorsList) # returning  values in a list
factors(20)
#%%
# several input, a composite data structure:
def powerDF(aList,power=2):
    import pandas as pd
    # list comprehension
    powerList=[val**power for val in aList]
    # both lists into a dict:
    answerAsDicts={'number':aList,'power'+str(power):powerList}
    # data frame is created, and that is returned:
    return pd.DataFrame(answerAsDicts)
powerDF(factors(10),3)
# of course, this works:
valsDict={'aList':factors(10), 'power':3}
powerDF(**valsDict)
#%%
#HOMEWORK
#Make a function that reads two lists and returns a data frame with those lists and extra columns with their sum, difference, multiplication and division
# several input, a composite data structure:
#NEED HELP
def operations(x,y):
    import pandas as pd
    # list comprehension
    aList=[1,2,3,4,5]
    bList=[val+val for val in aList]
# both lists into a dict:
    answerAsDicts={'number1':aList,'number2':bList, 'add':aList+bList}
    # data frame is created, and that is returned:
    return pd.DataFrame(answerAsDicts)
operations(operations(5,2),operations(5,2))
# of course, this works:
valsDict={'aList':factors(10), 'power':3}
powerDF(**valsDict)
#%%
#Imaging you have created a function that converts a value like:
def double(x):
    return 2*x
myList=[1,2,3]
double(myList)
map(double,myList)
list(map(double,myList))
#%%
#How should you organize the input so that you get double() to work as it did with R vectors?
#NEED HELP
def double(x):
    return 2*x
myList=(1,2,3)
doublemyList=(val for val in myList)*2
double(doublemyList)
double2=lambda x: 2*x
list(map(double2,myList))
#Easy functions can be written using lambda notation:
drinkingAge= lambda x: x >= 21
#You can use these functions to create filters:
agesList=[12,34,56,19,24,3]
list(filter(drinkingAge,agesList))
#Applying functions to composite structures¶
#%%
#Creating data frame
import pandas as pd
data={'numberA':[10,20,30,40,50],'numberB':[6,7,8,9,10]}
dataDF=pd.DataFrame(data)
dataDF
double(dataDF)
# this will double each element column-wise
dataDF.apply(double,axis=0)
# this will double each element row-wise
dataDF.apply(double,axis=1)
# the sum of the columns
dataDF.apply(sum,axis=0)
# the sum of the rows
dataDF.apply(sum,axis=1)
dataDF.apply(min) # axis=0 is the default, I can omit it.
dataDF.apply(min,axis=1)
dataDF.applymap(double)
# This is a Series
dataDF.numberA
# This is a Series
dataDF['numberA']
# This is a data frame:
dataDF[['numberA']]
# This is a Series
dataDF.loc[:,'numberA']
# This is a data frame:
dataDF.loc[:,['numberA']]
# This is a Series
dataDF.iloc[:,0]
# This is a data frame:
dataDF.iloc[:,[0]]
#Homework
#Understand what this function is doing:
#Need HELP
#%%
import pandas as pd
import os
folderName='data'
fileName='dataforstrangeF.csv'
fileExcel=os.path.join(folderName,fileName)
dataFromExcel=pd.read_csv(fileExcel) # table '1'
dataFromExcel
#%%
def strangerF(x):
    answer=0
    change=True
    for value in x:
        if (change):
            answer+=value
        else:
            answer-=value
    
        change= not change 

    return answer
x=(1,2,3)
strangerF(x)
#Understand what this function is doing
#This function is defining a function as starting with a particiular value (answer=0) and a flag for if an operation causes it to be True or False. Once the function is started, it takes the first value, considers whether it is T/F (in the first instance, it is True), then records the summation of answer and the value. Finally, it then flips the value of change from True to False. It repeats this process for the rermaining values under consideration and combines the sum or difference of each answer.
