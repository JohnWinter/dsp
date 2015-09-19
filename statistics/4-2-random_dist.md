[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

Problem: Compare randomly generated sample and see if the distribution is truly random.  
                                     
Solved by analyzing the pmf visual and the shape of the CDF line from the set of 1000 and 
many lower value sets. 

Solution:
The PMF looked to be and  the straight CDF line confirmed that the "random" data was uniformly 
distributed.To comment on the authenticity of the random property I did the visualizations 
with smaller sample sizes many times. I always found the distribution to seem far more uniform 
than something truly random would produce. If it was random I would expect to find cases of 
clustering at least part of the time. 

```
om

import thinkstats2

import thinkplot

sample = []

i = 0

while i<1000:
    sample.append(random.random())
    i = i+1

pmf = thinkstats2.Pmf(sample)

thinkplot.Pmf(pmf)

thinkplot.Show()

cdf = thinkstats2.Cdf(sample)

thinkplot.Cdf(cdf)

thinkplot.Show()
```