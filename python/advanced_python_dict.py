PLACE YOUR CODE HERE

# 6

df['last_name'] = df['name']
df['last_name'] = df['last_name'].map(lambda x: x.rsplit(None, 1)[-1])

faculty_dict = {}
for index, row in df.iterrows():
    if row['last_name'] not in faculty_dict.keys():
        faculty_dict[row['last_name']] = ([[row['degree'], row['title'], row['email']]])
    elif row['last_name'] in faculty_dict:
        faculty_dict[row['last_name']].append([row['degree'],row['title'],row['email']])

print {k: faculty_dict[k] for k in faculty_dict.keys()[:3]}


# 7 

df['first_name'] = df['name']
df['first_name'] = df['first_name'].map(lambda x: x.split(' ', 1)[0])

professor_dict = {}
for index, row in df.iterrows():
    professor_dict[(row['first_name'], row['last_name'])] = ([[row['degree'], row['title'], row['email']]])

print {k: professor_dict[k] for k in professor_dict.keys()[:3]}


# 8 

import collections

sort_professor_dict = {}
for index, row in df.iterrows():
    sort_professor_dict[(row['last_name'], row['first_name'])] = ([[row['degree'], row['title'], row['email']]])
    
print collections.OrderedDict(sorted(sort_professor_dict.items()))

