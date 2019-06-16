#!/usr/bin/env python
# coding: utf-8

# In[ ]:



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

hedeflenen=np.array([[0.01,0.99]])
eArray=(1/2 * (hedeflenen-sigmoidO)**2)
#print("E[o1 o2] : {}".format(eArray))   #  E[o1 o2] : [[0.27481108 0.02356003]]
eTotal=np.sum(eArray)
print("Etotal : {}".format(eTotal))

degisim = np.dot(sigmoidH.T, -(hedeflenen-sigmoidO) * sigmoidO* (1-sigmoidO))  #etotal/w5:dw w6,w7,w8 sonucu
print(degisim)


guncellenmisDeger = w2 - n*degisim
print(guncellenmisDeger)

