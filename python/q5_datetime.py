# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

from datetime import datetime

def days_between_dashes(d1, d2):
    d1 = datetime.strptime(d1, "%m-%d-%Y")
    d2 = datetime.strptime(d2, "%m-%d-%Y")
    return abs((d2-d1).days)

days_between_dashes (date_start, date_stop)

####b)  
date_start = '12312013'  
date_stop = '05282015'  

def days_between_joint(d1, d2):
    d1 = datetime.strptime(d1, "%m%d%Y")
    d2 = datetime.strptime(d2, "%m%d%Y")
    return abs((d2-d1).days)

days_between_joint (date_start, date_stop)

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

from dateutil import parser

d1 = (parser.parse(date_start)).strftime("%m-%d-%Y")
d2 = (parser.parse(date_stop)).strftime("%m-%d-%Y")

days_between_dashes(d1, d2)

