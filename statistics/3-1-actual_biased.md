[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

Problem: Visualize and compute the difference between the actual and observed number of children per household, by children. 

Solved by using the data source provided in chap03ex.ipynb. Created a pmf as per Chapter 3 example and applied the bias pmf
operations as per the example in chapter 3. Initially I tried to avoid working with thinkstats types but had some trouble converting. 

Solution: Running the code below will show the plot and means. Data is as expected. Children who do not exist cannot observe their non-existance. etc.
Not sure why the Pmf.Mean() operations takes so long. 


```
import thinkplot

import thinkstats2

import chap01soln

resp = chap01soln.ReadFemResp()

pmf = thinkstats2.Pmf(resp.numkdhh)

new_dic = pmf.Copy()

for key,item in new_dic.Items():
    new_dic.Mult(key,key)

new_dic.Normalize()

thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf,new_dic])
thinkplot.Pmf(pmf, label='actual')
thinkplot.Pmf(new_dic,label='observed')
thinkplot.Show()


print("observed mean" + str(new_dic.Mean()))
print("actual mean" + str(pmf.Mean()))
```