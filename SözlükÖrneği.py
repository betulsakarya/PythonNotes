#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def tcKontrolu():
  kontrolEvetHayir=True
  while kontrolEvetHayir:
    
    kontrol=input("Tc Numaranızı Girmek İstiyor musunuz? EVET / HAYIR ")
    if kontrol == "evet" or kontrol == "EVET" or kontrol == "Evet": 
      
      onBirHaneKontrol=True
      while onBirHaneKontrol:
        tcNo=input("Tc No :")
        if len(tcNo) != 11:
          print("Tc Numarasını 11 haneli girmelisiniz.") 
          continue
        else:
          liste.append(tcNo)
          break
      break    
  
    elif kontrol == "hayır" or kontrol == "HAYIR" or kontrol == "Hayır":
      print("TcNo girmeden devam ediyorsunuz.")
      break
    
    else:
      print("Lütfen evet yada hayır şeklinde cevaplama yapınız.")  
    
    
    
def sozlukOlustur(gelenListe):
  i=0
  for deger in gelenListe:
    dict[i]=deger
    i+=1
  return dict
  
def sozlukYazdir(gelenSozluk):
  i=0
  for i in gelenSozluk:
    print(gelenSozluk[i])
    i+=1
     
  
  


ad=input("Adınızı giriniz : ")
soyad=input("Soyadınızı giriniz : ")
dYili =int(input("Doğum yılınızı giriniz : "))
dict={}
liste=[]
liste.append(ad)
liste.append(soyad)
liste.append(dYili)

tcKontrolu()

sozlukOlustur(liste)

sozlukYazdir(dict)

