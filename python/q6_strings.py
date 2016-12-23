# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    if count >= 10:
        print "Number of donuts: many"
    else:
        print "Number of donuts: 4"       
        
     

def both_ends(s):
    word = list(s)
    new_string = []
    if len(s) > 1:
        new_string.append(word[0])
        new_string.append(word[1])
        new_string.append(word[-2])
        new_string.append(word[-1])
        return ''.join(new_string)
    else:
        return "''"


    
def fix_start(s):
    word = list(s)
    new_word = []
    new_word.append(word[0])
    for l in word:
        if l != new_word[0]:
            new_word.append(l)
        else:
            new_word.append('*')
    new_word.pop(1)
    return ''.join(new_word)



def mix_up(a, b):
    word_a = list(a)
    word_b = list(b)
    list_a = []
    list_b = []
    list_a.append(word_b[0:2])
    list_a.append(word_a[2:])
    list_b.append(word_a[0:2])
    list_b.append(word_b[2:])
    print ''.join(list_a[0]) + ''.join(list_a[1]) + " " + ''.join(list_b[0]) + ''.join(list_b[1])

    
    
def verbing(s):
    word = list(s)
    if len(word) >= 3:
        if ''.join(word[-3:]) == "ing":
            word.append("ly")
            return ''.join(word)
        else:
            word.append("ing")
            return ''.join(word)
    else:
        return s

    
    
def not_bad(s):
    sentence = s.split()
    not_place = -1
    bad_place = -1
    for i in range(len(sentence)):
        if sentence[i] == "not":
            not_place = i
        elif sentence[i] == "bad" or sentence[i] == "bad!":
            bad_place = i
    if not_place >= 0 and not_place < bad_place:
        del sentence[not_place:]
        sentence.append("good")
        return ' '.join(sentence) 
    else:
        return s


    
def front(s):
    front_list = list(s)
    number_front = len(front_list) / 2
    if len(front_list) % 2 == 0:
        return ''.join(front_list[:(number_front)])
    else:
        return ''.join(front_list[:(number_front + 1)])
  
def back(s):
    front_list = list(s)
    number_front = len(front_list) / 2
    if len(front_list) % 2 == 0:
        return ''.join(front_list[number_front:])
    else:
        return ''.join(front_list[(number_front + 1):])
 
def front_back(a, b):
    return front(a) + front (b) + back(a) + back(b) 
