# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1F_X6KnNS2elB41J2GkBTBkqSKNUE-lzU
"""

if __name__ == '__main__':
    
    d={} #1
    for _ in range(int(input())): #2
        Name=input() #3
        Grade=float(input()) #4
        d[Name]=Grade #5
        
    v=d.values()#6
    second=sorted(list(set(v)))[1] #7
    second_lowest=[] #8
    for key,value in d.items():  #9
        if value==second: #10
            second_lowest.append(key) #11
    second_lowest.sort() #12
    for name in second_lowest: #13
        print (name)