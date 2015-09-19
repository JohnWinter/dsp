[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

Problem: Plot percentiles of birth weight versus mother's age, caculate the correlations, analyze the relationship between the variables. 

Solved by following the coding example in ch 7 closely. Consulted the solution for help plotting the percentiles. The plots show the relationship
of the variables better by reducing noise than a raw scatter plot would because, depending on the bin size, it reduces variances through averaging. 


Solution: After plotting the percentiles we see a small linear correlation for age and weight between ages 18 and 37. More than anything this tells
me that my wife and I need to get started early enough to avoid complications that are likely to be part of the weight drop after 37. The Pearson and 
Spearman correlation coefficients are both low (below 0.10). They would be higher if we restricted the data set to the 18 to 37 age group though.  





Code:
```
import numpy

import pandas

import thinkstats2

import nsfg

import thinkplot

preg = nsfg.ReadFemPreg() # complete dataframe
live = preg[preg['outcome'] == 1] # live birth slice
weight = live['totalwgt_lb']
age= live['agepreg']
new = pandas.concat([weight,age],axis=1)

new=new.dropna(subset=['agepreg','totalwgt_lb'])


bins=numpy.arange(0,50,5)
indicies= numpy.digitize(new.agepreg,bins)
groups= new.groupby(indicies)

ages=[group.agepreg.mean() for i, group in groups]
cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups]

for percent in [75,50,25]:
    weights = [cdf.Percentile(percent) for cdf in cdfs]
    label = '%dth' % percent
    thinkplot.Plot(ages,weights,label=label)


thinkplot.Show()

weight = new['totalwgt_lb']
age= new['agepreg']

print('Pearson: ' , thinkstats2.Corr(age,weight))
print("Spearman: " , thinkstats2.SpearmanCorr(age,weight))

```