PLACE YOUR CODE HERE

# 1

import pandas as pd
import numpy as np
import itertools

faculty = pd.read_csv("faculty.csv")
faculty.columns = ['name', 'degree', 'title', 'email']
df = pd.DataFrame(faculty)

faculty_dictionary = (df.to_dict(orient='list'))
degree_list = faculty_dictionary.get('degree')
i = 0
for d in degree_list:
    degree_list[i] = d.replace(".", "")
    degree_list[i] = degree_list[i].split(' ')
    i += 1

merged_degree_list = list(itertools.chain(*degree_list))

final_degree_list = []
for d in merged_degree_list:
    if d != '':
        final_degree_list.append(d)

degree_dict = {}
for d in final_degree_list:
    if d not in degree_dict:
        degree_dict[d] = 1
    else:
        degree_dict[d] += 1

print degree_dict


# 2

print df['title'].value_counts()


# 3

df_email_list = df['email'].tolist()
print df_email_list


# 4

domains = []
for p in df_email_list:
    end_email = p.split("@",1)[1]
    if end_email not in domains:
        domains.append(end_email)

print "There are " + str(len(domains)) + " types of domains."
print domains
