import math
from decimal import *

negative_reviews = 38
neutral_reviews = 31
positive_reviews = 173

total_reviews = (negative_reviews + neutral_reviews + positive_reviews)
print (total_reviews)

negative_score = (negative_reviews / total_reviews) * (100)
print (negative_score)

positive_score = (positive_reviews / total_reviews) * (100)
print (positive_score)

customer_satisfaction_score = (positive_score - negative_score)
print (round(customer_satisfaction_score, 2))