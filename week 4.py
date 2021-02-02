import pandas as pd
import numpy as np
data = pd.read_csv("WEEK 4 COURSE.csv")
print(data)
#How many rows and columns are there in your file?
print(data.shape)
#Print row 3-8 ( using iloc/loc)
print(data.iloc[2:7, 0:5])
#Find the mean number of all-inclusive hotels across all destinations.
print(data.mean())
#Find the lowest scoring destination (Feedback_score).
myfilter1 = data["Feedback_Score"] < 7
lowscore = data[myfilter1]
print(lowscore. tail())
#Find the highest scoring destination.
myfilter = data["Feedback_Score"] > 9
highscore = data[myfilter]
print(highscore. head())
#Find all the destinations where there are more than 9 all-inclusive hotels (NB all in my dataset).
myfilter3 = data["All_inclusive"] > 8
inclusive = data[myfilter3]
print(inclusive)
#Filter the data by destination and score above 8.
myfilter4 = data["Feedback_Score"] > 8
above8 = data[myfilter4]
print(above8)
#Filter the data by destination and score below 2 (NB: none in my dataset).
myfilter5 = data["Feedback_Score"] < 2
below2 = data[myfilter5]
print(below2)







