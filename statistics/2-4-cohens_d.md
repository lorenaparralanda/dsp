[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> # Answer 

>> Cohen's d = 0.028879044654449883

>> In other words, the difference between the means of pregnancy length for first babies and pregnancy length for other babies is 0.028 standard deviations. Thus, there is no significant difference.

# Code 

```python
def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / np.sqrt(pooled_var)
    return d
    
CohenEffectSize(firsts.prglngth, others.prglngth)
```
