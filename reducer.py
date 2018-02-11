#!/usr/bin/python

import sys
import math

def reducer():
    list_ = []
    old_tuple = ('foo', 'bar')
    i = 0
  
    for line in sys.stdin:
        data = line.strip().split("\t")
        
        if len(data) != 3:
            continue
            
        city, year, value = data
        new_tuple = (city, year)
        
        if old_tuple != new_tuple:
            if i != 0:
                print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}".format(old_tuple[0], old_tuple[1], max(list_), min(list_), getMedian(list_), getStandardDeviation(list_))        
                list_ = []    

        i += 1 
        list_.append(value)   
        old_tuple = new_tuple
                                 
    if old_tuple != ('foo', 'bar'):
         print "{0}\t{1}\t{2}\t{3}\tf{4}\t{5}".format(old_tuple[0], old_tuple[1], max(list_), min(list_), getMedian(list_), getStandardDeviation(list_))
         
         
def getMedian(list_):
    n = int(math.floor(len(list_)/2))
    
    if len(list_) % 2 == 0:       
        median = (float(list_[n-1]) + float(list_[n]))/2           
    else:
        median = list_[n] 
    return median
    
def getStandardDeviation(list_):
    sum = 0
    for i in list_:
        sum += float(i)
    
    mean = sum/len(list_)
    
    diff_squared = []
    for i in list_:
        diff = float(i) - mean
        diff_squared.append(diff*diff)
        
    sum = 0
    
    for i in diff_squared:
        sum += i
    
    mean_diff_squared = sum/len(diff_squared)
    
    return math.sqrt(mean_diff_squared)
    
if __name__ == '__main__':
    reducer()
