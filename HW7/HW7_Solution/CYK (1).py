# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 21:13:00 2017

@author: mouni
"""
import numpy as np
from itertools import product as prod
CNF_Grammar=[["S","EC"],["E","AB"],["C","BE"],["C","c"],["B","b"],["B","DD"],["A","a"],["D","b"]]

class CYK():
    def get_grammar(self,a):
        self.g=a
    def isInCFL(self,st):
        self.table=np.empty((len(st),len(st)),dtype=object)
        for i in range(len(st)):
            l=[]
            for j in range(len(self.g)):
                if st[i]==self.g[j][1]:
                    l.append(self.g[j][0])
            self.table[0][i]=l
            
        for i in range(1,len(st)):
            for j in range(0,len(st)-i):
                l=[]
                for k in range(0,i):
                    self.p=prod(self.table[k][j],self.table[i-1-k][j+k+1])
                    for q in self.p:
                        for z in range(len(self.g)):
                            if ''.join(q) == self.g[z][1]:
                                l.append(self.g[z][0])
                self.table[i][j]=l               
                                
        output = self.check_final(st)
        return output
                 
    def check_final(self,st):
        if "S" in self.table[len(st)-1][0]:
            return True
        else:
            return False
            
        return self.table   
            
v=CYK()
v.get_grammar(CNF_Grammar)    

def unit_test_1():
    s="abc"
    print(s)
    print(v.isInCFL(s))

def unit_test_2():
    s="abbbabb"
    print(s)
    print(v.isInCFL(s))

def unit_test_3():
    s="abbc"
    print(s)
    print(v.isInCFL(s))

def unit_test_4():
    s="bbc"
    print(s)
    print(v.isInCFL(s))

def unit_test_5():
    s="aaabb"
    print(s)
    print(v.isInCFL(s))   
    
    
    
    