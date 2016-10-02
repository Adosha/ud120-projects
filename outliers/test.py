#!/usr/bin/python


#def outlierCleaner(predictions, ages, net_worths):
import numpy
"""
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
"""
predictions = [1,22,3,4,5,2,4,66,4,3]
net_worths = [2,3,4,5,67,5,4,3,2,1]
ages = [2,4,5,7,7,2,4,5,3,1]

perc = 0.1
number = round(perc * len(net_worths))
#number = 9
diff = []
for x in range(len(net_worths)):
    dif = (predictions[x] - net_worths[x])**2
    diff.append(dif)

print diff
for i in range(1):
    to_exclude = diff.index(max(diff))
    del diff[to_exclude]
    predictions = numpy.delete(predictions,to_exclude)
    ages = numpy.delete(ages,to_exclude)
    net_worths = numpy.delete(net_worths,to_exclude)

cleaned_data = zip(predictions, ages, net_worths)

print cleaned_data
    ### your code goes here


    #return cleaned_data
