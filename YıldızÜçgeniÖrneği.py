#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Kat sayisini giriniz : ")
i=int(input())

for katDegiskeni in range(i):
  
  for boslukDegiskeni in range(i-katDegiskeni):
    print("" ,end =" ")
  for yildizDegiskeni in range(2*katDegiskeni+1):
    print("",end="*")
      
  print("",end ="\n")
  

