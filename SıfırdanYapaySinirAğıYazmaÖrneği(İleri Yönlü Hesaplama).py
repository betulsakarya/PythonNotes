#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

def sigmoid(sigmoidHesaplanacakDeger):
  y= 1/(1+np.exp(-sigmoidHesaplanacakDeger))
  return y


b1=0.35
b2=0.60
n=0.5 

x=np.array([[0.05,0.10]], dtype=np.float64)
w=np.array([[0.15,0.25],[0.20,0.30]], dtype=np.float64)  # Input - Hidden Ağırlıklar

gizliKatmanCiktilari=(np.dot(x,w)+b1)   # [0.3775  0.3925]
sigmoidH=sigmoid(gizliKatmanCiktilari ) 
print("sigmoid sonucu [h1,h2] : {} ".format(sigmoidH))

w2=np.array([[0.40,0.50],[0.45,0.55]])        # Hidden - Output Ağırlıklar

cikisKatmanCiktilari=(np.dot(sigmoidH,w2)+b2)    #  [[1.10590597 1.2249214 ]]
sigmoidO=sigmoid(cikisKatmanCiktilari  ) 
print("Sigmoid Sonucu [o1 o2]  : {} ".format(sigmoidO))


# In[ ]:




