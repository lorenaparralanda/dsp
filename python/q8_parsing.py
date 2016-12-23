# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import pandas as pd
import numpy as np
 
def read_data_csv(data):
    file = open(data, "r")
    reader = csv.reader(file)
    for row in reader:
        print row

def read_data_pandas(data):
    parsed_data = pd.read_csv(data)
    return parsed_data
     
def get_min_score_difference(parsed_data):
    parsed_data = read_data_pandas(parsed_data)
    parsed_data['Difference'] = parsed_data['Goals'] - parsed_data['Goals Allowed']
    return parsed_data

def get_team(parsed_data):
    parsed_data = get_min_score_difference(parsed_data)
    parsed_data['Absolute Difference'] = parsed_data['Difference'].abs()
    parsed_data.sort_values(by='Absolute Difference', axis=0, ascending=True, inplace=True)
    return parsed_data.head(n=1)['Team']
