import re
fname = "C:\\Users\\sandy\\emp.csv"
fobj = open(fname,'r')
for var in fobj:
    if(re.search('sales',var,re.I)):
        s = re.sub('pune','KOLKATA',var)
        if('KOLKATA' in s):
            print(s.strip())
