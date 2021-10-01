#!/usr/bin/env python

from operator import itemgetter
import sys


max_age = 0
min_age = 200
current_contre = None
nomber=1
contre=None
age = None
sex=None
listcontre=[]
wordList = dict()
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    
    # parse the input we got from mapper.py
    contre,age = line.split('\t',1)
     
    try:
        age = int(age)
    except ValueError:
           
            continue
    if min_age == 0:
        min_age == age
    if current_contre == contre :
        if age > max_age:
            max_age=age
        if age < min_age:
            min_age=age
        
        nomber+=1 
    else:
        if current_contre:
            if max_age==0 and min_age==200:
                  max_age=age
                  min_age=age
            listcontre.append({'contre':current_contre, 'maxage':max_age,'minage':min_age,'nomber':nomber})  
        nomber=1
        current_contre = contre  
        max_age= age  
        min_age=age


if current_contre == contre:
  
   listcontre.append({'contre':current_contre, 'maxage':max_age,'minage':min_age,'nomber':nomber}) 

def myFunc(e):
  return e['nomber']

listcontre.sort(reverse=True,key=myFunc)


for con in listcontre:
  print 'contre: %s\t max age: %s\t min age: %s\t nomber: %s' % (con['contre'], con['maxage'],con['minage'],con['nomber'])
