#!/usr/bin/python
#-*- coding:utf-8 -*-

"""
    starter code for exploring the Enron dataset (emails + finances)
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "How many data points (people) are in the dataset?(146) ", \
        len(enron_data.keys())

print "For each person, how many features are available?(21) ", \
        len(enron_data[enron_data.keys()[0]].keys())

poi_count = 0
for k in enron_data:
    if enron_data[k]["poi"] == 1:
        poi_count += 1
print "How many POIs are there in the E+F dataset?(18) ", \
        poi_count

print "What is the total value of the stock belonging to James Prentice?(1095040) ", \
        enron_data['PRENTICE JAMES']['total_stock_value']

print "How many email messages do we have from Wesley Colwell to persons of interest?(11) ", \
        enron_data['COLWELL WESLEY']['from_this_person_to_poi']

print "What’s the value of stock options exercised by Jeffrey Skilling?(19250000) ", \
        enron_data['SKILLING JEFFREY K']['exercised_stock_options']

quantified_salary_count = 0
for k in enron_data:
    if enron_data[k]['salary'] != 'NaN':
        quantified_salary_count += 1
print "How many folks in this dataset have a quantified salary? ", \
        quantified_salary_count


email_address_count = 0
for k in enron_data:
    if enron_data[k]['salary'] != 'NaN':
        email_address_count += 1
print "What about a known email address? ", \
