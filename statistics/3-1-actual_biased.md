[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> # Answer

>> Mean of actual distribution: 1.02420515504

>> Mean of biased distribution: 2.40367910066

>> Plot of actual and biased distributions:

![actual_biased](https://github.com/lorenaparralanda/dsp/blob/master/img/actual_vs_biased.png)

# Code

```python 
resp = nsfg.ReadFemResp()

pmf = thinkstats2.Pmf(resp.numkdhh, label = 'numkdhh')
biased = BiasPmf(pmf, label = 'biased')

print('Actual mean', pmf.Mean())
print('Observed mean', biased.Mean())thinkplot.PrePlot(2)

thinkplot.Pmfs([pmf, biased])
thinkplot.Config(xlabel='Number of children', ylabel='PMF')
```
