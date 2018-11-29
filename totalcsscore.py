import csv
from decimal import *
import math
from collections import Counter


with open('ServiceReviews.csv', 'r') as f:
	data = csv.reader(f)
	for row in f:
		CustomerEmail = row[0]
		ReviewStars = row[1]
		ReferenceID = row[2]
		BusinessUnitID = row[3]
		Tags = row[4]
		c = Counter(row[1] for row in csv.reader(f))
		print (c)
		fivestars = (c['5'])
		print (fivestars)
		fourstars = (c['4'])
		print (fourstars)
		negativereviews = (c['3'] + c['2'] + c['1'])
		print (negativereviews)
		totalreviews = fivestars + fourstars + negativereviews
		print (totalreviews)
		negative_score = (negativereviews / totalreviews) * (100)
		print (negative_score)
		positive_score = (fivestars / totalreviews) * (100)
		print (positive_score)
		customer_satisfaction_score = (positive_score - negative_score)           
		print (round(customer_satisfaction_score, 2))





		
