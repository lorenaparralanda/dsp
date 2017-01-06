[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

>> # Answer

>> Plotted birth weight vs mother's age:

![Scatter](https://github.com/lorenaparralanda/dsp/blob/master/img/weight%26mom_scatter.png)

>> Pearson's correlation: 0.0688339703541

>> Spearman's correlation: 0.0946100410966

>> There is no real correlation between the baby's birth weight and the mother's age. 

# Code

```python
import first
import pandas as pd
import numpy as np
import thinkstats2
import thinkplot
%matplotlib inline

live, firsts, others = first.MakeFrames()
live = live.dropna(subset=['agepreg', 'totalwgt_lb'])

ages = live.agepreg
weights = live.totalwgt_lb

thinkplot.Scatter(ages, weights, alpha=1)
thinkplot.Config(xlabel='Age',
                 ylabel='Weight',
                 legend=False)
                 
def Corr(xs, ys):
    xs = np.asarray(xs)
    ys = np.asarray(ys)

    meanx, varx = thinkstats2.MeanVar(xs)
    meany, vary = thinkstats2.MeanVar(ys)

    corr = Cov(xs, ys, meanx, meany) / np.sqrt(varx * vary)
    return corr
    
def SpearmanCorr(xs, ys):
    xranks = pd.Series(xs).rank()
    yranks = pd.Series(ys).rank()
    return Corr(xranks, yranks)    

print('Corr', Corr(ages, weights))
print('SpearmanCorr', SpearmanCorr(ages, weights))
```
