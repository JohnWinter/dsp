[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)




Problem: Plot the sampling distribution of the estimate L for the exponential distribution with lambda 2, compute standard 
error and 90% confidence interval. Plot how larger sample sizes reduce the value of the standard error. 

Solved by 

1) Generating 1000 sets of samples from an exponential distribution with the the numpy function np.random.exponential.
2) Taking the L of each set and thereby creating a set of estimates (Ls) to compare to Lambda.
3) Took and plotted the CDF of the estimates with the thinkplot module which shows the exponential distribution cdf as expected. 
As we can see the Lambda estimates almost all fall between 1 and 3
4) The standard error, obtained using the RMSE implementation provided (.82) matches what we saw on the CDF. 
5) Confidence interval took using the thinkstats2 Percentile function for 5% and 95%.
6) Created 20 new simulations at varying samples sizes (5 to 24). One clearly sees that as sample size (n) increases 
the standard error decreases. 

Plot solutions provided by running the below.
Code:
```
import numpy as np

import thinkstats2

import thinkplot

import math

def RMSE(estimates, actual):
    e2 = [(estimate-actual)**2 for estimate in estimates]
    mse = np.mean(e2)
    return math.sqrt(mse)

def MeanError(estimates, actual):
    errors = [estimate-actual for estimate in estimates]
    return np.mean(errors)


def Estimate3(n=10, m=1000):
    lam = 2

    means = []

    for _ in range(m):
        xs = np.random.exponential(1.0/lam, n)
        L = 1.0 / np.mean(xs)

        means.append(L)

    cdf = thinkstats2.Cdf(means)
    ci = cdf.Percentile(5), cdf.Percentile(95)
    thinkplot.Cdf(cdf)
    thinkplot.show(xlabel="Sample L",ylabel="CDF")


    print('Standard Error', RMSE(means, lam))

    print('90% confidence interval', ci)
Estimate3()

def StErr(n,m):
    lam = 2

    means = []

    for _ in range(m):
        xs = np.random.exponential(1.0/lam, n)
        L = 1.0 / np.mean(xs)

        means.append(L)
    return(RMSE(means, lam))


x=[]
y=[]
for n in range(5,25):
    x.append(n)
    y.append(StErr(n,1000))


thinkplot.Scatter(x,y)

thinkplot.Show(xlable=' n ',ylabel="Standard Error")
```