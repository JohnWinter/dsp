[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)


Problem: What % of men qualify for Blue Men Group in terms of height. 

Solved by using the normal distribution and subtracting the CDF % of the upper bound from the lower bound CDF %. 

Solution: 34% of men qualify for the Blue Men Group in terms of height. 

code:

```
import scipy.stats

x=scipy.stats.norm(loc=178,scale=7.7)

a=(x.cdf(185.42)-x.cdf(177.8))*100

print("Percent of men who qualify for Blue Men Group: " + str(round(a,1))+"%")
```