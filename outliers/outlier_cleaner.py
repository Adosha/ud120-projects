#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """
    import numpy
    perc = 0.1
    number = round(perc * len(net_worths))
    diff = []
    for x in range(len(net_worths)):
        dif = (predictions[x] - net_worths[x])**2
        diff.append(dif)

    for i in range(9):
        to_exclude = diff.index(max(diff))
        del diff[to_exclude]
        predictions = numpy.delete(predictions,to_exclude)
        ages = numpy.delete(ages,to_exclude)
        net_worths = numpy.delete(net_worths,to_exclude)

    cleaned_data = zip(ages, net_worths, diff)

    ### your code goes here


    return cleaned_data


"""
!!!!!!!!!!!!!!!!!!!!More short way:

 ### your code goes here

    errors = (net_worths-predictions)**2
    cleaned_data =zip(ages,net_worths,errors)
    cleaned_data = sorted(cleaned_data,key=lambda x:x[2][0], reverse=True)
    limit = int(len(net_worths)*0.1)


    return cleaned_data[limit:]
"""
