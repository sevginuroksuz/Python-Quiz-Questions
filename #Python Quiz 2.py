sayi= int(input("Bir sayi giriniz:")) #Kullanicidan sayi alinir.
listemm=["Amasya", "Ankara", "İstanbul", "Bursa", "İzmir"] 
karakter= listemm[sayi]     #Kullanicidan alinan sayiyiyla listeden eleman çekilir.
x=len(karakter)       #Listdeden kullanicinin seçtigi elemanin uzunlugu hesaplanir.
bas=karakter[0:2]     #Kullanicinin seçtigi elemanin ilk iki harfi bas'a atanir.
son=karakter[x-2:x]   #Kullanicinin seçtigi elemanin son iki harfi son'a atanir.
print(bas+son)