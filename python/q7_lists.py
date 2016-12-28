# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0

# 1
def match_ends(words):
    count = 0
    for i in range(len(words)):
        if len(words[i]) >= 2:
            if words[i][0] == words[i][-1]:
                count += 1
    return count

# 2
def front_x(words):
    x_list = []
    no_x_list = []
    new_words = []
    for i in range(len(words)):
        if words[i][0] == "x":
            x_list.append(words[i])
        else:
            no_x_list.append(words[i])
    x_list.sort()
    no_x_list.sort()
    x_list.extend(no_x_list)
    return x_list

# 3
def sort_last(tuples):
    return sorted(tuples, key=lambda x: x[-1])
    
# 4    
def remove_adjacent(nums):
    new_list = nums[:1]
    for i in nums[1:]:
        if i != new_list[-1]:
            new_list.append(i)
    return new_list
    
# 5    
def linear_merge(list1, list2):
    list1.extend(list2)
    list1.sort()
    return list1
