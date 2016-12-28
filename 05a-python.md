# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are sequences of values of any type. Both lists and tuples can be indexed. However, these two types of sequences differ because lists are mutable and tuples are immutable and hashable. Therefore, it is tuples that can be utilized as keys in a dictionary.  

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Similar to tuples and lists, sets are also sequences of values. However, sets do not contain duplicates, are unordered, and use hash tables. 

Example of a list with different types of values. 
```python 
example_list = [‘Mexico’, ‘USA’, ‘Togo’, 2, [‘UDLAP’ , ‘Fordham’, ‘Metis’]]
```

Example of the creation of a set from a list:
```python
random_list = [1, 1, 2, 2, 2, 2, 2, 3, 3] 
set(random_list) 
```
Which outputs the set:
```python
set([1, 2, 3])
```

Sets find elements faster because they are implemented using hash tables. Therefore, when looking for an element, the program looks if it is located at the position determined by its hash, and, unlike lists, does not have to look through every place on the list.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Through `lambda`, Python supports the creation of anonymous functions. `lambda` functions can be used wherever function objects are required. However, they are restricted to a single expression. Example of the `lambda` expression at use:

```python
return sorted(tuples, key=lambda x: x[-1])
```
---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> Similar to what mathematicians do, list comprehension provides a concise way to create lists. For example, a mathematician might create a list this way: S = {x2 : x in {0...9}}. However, we can use Python/list comprehension to create the same list:

```python
S = [x**2 for x in range(10)]
```

A second example of list comprehension is: 

```python
[ord(i) for i in 'some string'] 
```

We can create the same list utilizing `map`:
```python
map(ord,'some string') 
```

A third example of list comprehension: 

```python
special_squares = []
for x in range(10):
    square = x**2
    if square > 5 and square < 50:
        special_squares.append(square)
```

And now the same list utilizing `map` and `filter`:
```python
squares = map(lambda x: x**2, range(10))
special_squares = filter(lambda x: x > 5 and x < 50, squares)
```

When we compare `map` vs list comprehension or `filter` vs list comprehension, depending on what one intends to do, speeds may vary. However, some argue that list comprehension is more direct and clear. 

Finally, here is an example of a set comprehension: 

```python
primes = {x for x in range(2, 101) if all(x%y for y in range(2, min(x, 11)))}
```
And a dictionary comprehension:

```python
{i:i for i in range(1, 11)}
```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)



