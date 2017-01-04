[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> # Answer

The first image below is the plotted PMF of the 1,000 randomly selected numbers. As its name suggests, the Probability Mass Function maps the probility of each randomly selected value occuring. In this case, the plot indicates that all values have the same probability of occuring. 

![PMF](https://github.com/lorenaparralanda/dsp/blob/master/img/RandomPMF.png)

The second image is the plotted CDF of the same 1,000 randomly selected numbers. The Cumulative Distribution Function maps the percentile rank of the randomly selected values. Therefore we see an ascending line. As the value of a the number rises, so does its rank. 

![CDF](https://github.com/lorenaparralanda/dsp/blob/master/img/RandomCDF.png)

# Code

```python
r = np.random.random(1000)

pmf = thinkstats2.Pmf(r, label = 'random #s')
thinkplot.Pmf(pmf, linewidth=0.1)
thinkplot.Config(xlabel='Random #s', ylabel='PMF')

cdf = thinkstats2.Cdf(r)
thinkplot.Cdf(cdf)
thinkplot.Config(xlabel='Random #s', ylabel='CDF')
```
