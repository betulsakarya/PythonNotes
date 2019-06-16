#!/usr/bin/env python
# coding: utf-8

# In[1]:


istiklalMarsi="""Korkma, sönmez bu şafaklarda yüzen al sancak;
Sönmeden yurdumun üstünde tüten en son ocak.
O benim milletimin yıldızıdır, parlayacak;
O benimdir, o benim milletimindir ancak/
Çatma, kurban olayım, çehreni ey nazlı hilal!
Kahraman ırkıma bir gül! Ne bu şiddet, bu celal?
Sana olmaz dökülen kanlarımız sonra helal...
Hakkıdır, hakk'a tapan, milletimin istiklal/
Ben ezelden beridir hür yaşadım, hür yaşarım.
Hangi çılgın bana zincir vuracakmış? Şaşarım!
Kükremiş sel gibiyim, bendimi çiğner, aşarım.
Yırtarım dağları, enginlere sığmam, taşarım/
Garbın afakını sarmışsa çelik zırhlı duvar,
Benim iman dolu göğsüm gibi serhaddim var.
Ulusun, korkma! Nasıl böyle bir imanı boğar,
'Medeniyet!' dediğin tek dişi kalmış canavar/
Arkadaş! Yurduma alçakları uğratma, sakın.
Siper et gövdeni, dursun bu hayasızca akın.
Doğacaktır sana va'dettigi günler hakk'ın...
Kim bilir, belki yarın, belki yarından da yakın/
Bastığın yerleri 'toprak!' diyerek geçme, tanı:
Düşün altında binlerce kefensiz yatanı.
Sen şehit oğlusun, incitme, yazıktır, atanı:
Verme, dünyaları alsan da, bu cennet vatanı/
Kim bu cennet vatanın uğruna olmaz ki feda?
Şuheda fışkıracak toprağı sıksan, şuheda!
Canı, cananı, bütün varımı alsın da hüda,
Etmesin tek vatanımdan beni dünyada cüda/
Ruhumun senden, ilahi, şudur ancak emeli:
Değmesin mabedimin göğsüne namahrem eli.
Bu ezanlar-ki şahadetleri dinin temeli,
Ebedi yurdumun üstünde benim inlemeli/
O zaman vecd ile bin secde eder -varsa- taşım,
Her cerihamdan, ilahi, boşanıp kanlı yaşım,
Fışkırır ruh-i mücerred gibi yerden na'şım;
O zaman yükselerek arsa değer belki başım/
Dalgalan sen de şafaklar gibi ey şanlı hilal!
Olsun artık dökülen kanlarımın hepsi helal.
Ebediyen sana yok, ırkıma yok izmihlal:
Hakkıdır, hür yaşamış, bayrağımın hürriyet;
Hakkıdır, hakk'a tapan, milletimin istiklal/
"""


def kitaGetir(sayi): 
  return dict[sayi] 
  
  
dict={}
liste=[]
kontrol = True

for kita in istiklalMarsi.split("/"):
  liste.append(kita)
liste.pop()  # listeye eklenen boş 11. elemamı cıkar



while kontrol:
  sayi=input("İstiklal Marşı'nın hangi kıtasını görmek istiyorsunuz? ")
  
  if sayi=="x":
    break
  
  
  kitaSayisi=int(sayi)
  if kitaSayisi > len(liste):
    print("İstiklal Marşı'nda böyle bir kıta yok.")
  
     
  else:
    index=1
    for x in liste:
      dict[index]=x 
      index+=1
      
    
  deger=kitaGetir(kitaSayisi)
  print(deger)

print("Çıkış")
   


# In[ ]:




