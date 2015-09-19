[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)


 
The Problem: Calculate the size of the effect of the condition of a first birth, as opposed to subsequent births, on baby size and pregnancy length.  

Solved by using the Think Stats code to slice the data and my own simple implementation of Cohen's D calc.

It appears that there is a slight negative effect on birth weight(smaller first babies) and a postive effect on pregnancy length (longer first birth pregnancies)

```
import pandas 

import thinkstats2

import nsfg

preg = nsfg.ReadFemPreg() # complete dataframe
live = preg[preg['outcome'] == 1] # live birth slice

firsts = live[live.birthord ==1] # slice to compare
others = live[live.birthord != 1] # slice to compare

cohen_d_weight = (firsts['totalwgt_lb'].mean() - others['totalwgt_lb'].mean())/live['totalwgt_lb'].std() #my Cohen D calc
cohen_d_preglength = (firsts['prglngth'].mean()- others['prglngth'].mean())/live['prglngth'].std() # my Cohen D calc

#Output:
print("Birth Weight: "+ "My Calc = "+str(round(cohen_d_weight,3))+" ThinkStats Calc ="+str(round(thinkstats2.CohenEffectSize(firsts.totalwgt_lb,others.totalwgt_lb),3)))
print("Preg Lengh: "+ "My Calc = "+str(round(cohen_d_preglength,3))+" ThinkStats Calc ="+str(round(thinkstats2.CohenEffectSize(firsts.prglngth,others.prglngth),3)))
```