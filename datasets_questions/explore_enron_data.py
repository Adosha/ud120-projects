#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""
from __future__ import division


import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
#print enron_data
import pprint
#pprint.pprint(enron_data)

print len(enron_data)
print len(enron_data[enron_data.keys()[0]])

numb_poi = 0
for key in enron_data:
    if enron_data[key]["poi"]==True:
        numb_poi +=1

print "POI pers in enron_data = ", numb_poi

import sys
sys.path.insert(0, '../final_project')

from poi_email_addresses import poiEmails
email_list = poiEmails()
print "Real POI pers emails = ", len(email_list)

print "Stock value of James Prentice is ",enron_data["PRENTICE JAMES"]["total_stock_value"]
print "Email from Wesley Colwell to POI: ",enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]


persons_with_salary = 0
persons_with_email = 0
persons_wo_payments = 0
poi_wo_payments=0
for key in enron_data:
    if "SKILLING" in key:
        print "Stock options exercised by Jeffrey K Skilling:", enron_data[key]["exercised_stock_options"]
        print "Total payments to Jeffrey K Skilling:", enron_data[key]["total_payments"]
    if "FASTOW" in key:
        print "Total payments to Fastow:", enron_data[key]["total_payments"]
    if "LAY" in key:
        print "Total payments to Lay:", enron_data[key]["total_payments"]
    if enron_data[key]["salary"] != "NaN":
        persons_with_salary += 1
    if enron_data[key]["email_address"] != "NaN":
        persons_with_email += 1
    if enron_data[key]["total_payments"] == "NaN":
        persons_wo_payments +=1
    if enron_data[key]["poi"] == True and enron_data[key]["total_payments"] == "NaN":
        poi_wo_payments +=1

x= len(enron_data)


percent_wo_pay = persons_wo_payments/x
percent_poi_wo_pay = 1.0*poi_wo_payments/x

print "Persons wo payments: ", persons_wo_payments
print "Percent wo payments:", round(percent_wo_pay,3)
print "POI wo payments:", poi_wo_payments

print "Persons with salary: ", persons_with_salary

print "Persons with email: ", persons_with_email
