# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists are contained in [] while tuples are contained in (). Lists are mutable so they can be updated with new entries. This property lets them work for dictionaries. 

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists maintain order and allow for multiples of the same value. Sets do not keep order and they only allow for unique items. Also all set items must be hashable. 
>> Set could be used for reviewing all the unique words used in a document. List could be used for keeping a list of phone numbers dialed in a time frame since there will likely be repeats and order of the calls may be of interest. 
>> Sets are faster because all items are hashed, i.e. computer knows exactly where to find them with hash id vs. matching against all items in list.   

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda allows one to create a function without having to define it. A shortcut. 
>> Example: $ sorted("Sort by the last letter of these strings".split(), key = lambda x: x[-1])

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions allow one to apply a function to each element in a list, like using map or extract only elements that meet certain criteria, like filter.
>> Map vs comprehension 
>>>squares = [x**2 for x in range(1,11)] 
>>>squares = list(map(lambda x:x**2, range(1,11)))
>> Filter vs comprehension 
>>>filter_squares = [num for num in squares if  num<71 and num>29]
>>>filter_squares = filter(lambda x: x>29 and x<71,squares)


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





