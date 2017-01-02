PLACE YOUR CODE HERE

# CONTINUED FROM ADVANCED PYTHON REGEX EXERCISES 

for email in df_email_list:
    print email
    
import csv

with open("Email list.csv", "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in df_email_list:
        writer.writerow([val])
