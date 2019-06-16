#!/usr/bin/env python
# coding: utf-8

# In[1]:


def fakt(gelenSayi):
  faktoriyel=1
  if gelenSayi==0 or gelenSayi==1:
     faktoriyel=1
  else:
     liste=list(range(2,gelenSayi+1))
     for i in liste:
          faktoriyel *= i
     
  return(faktoriyel)



sayi=int(input("Faktoriyeli alınacak sayıyı giriniz."))
print(fakt(sayi))


# In[ ]:




