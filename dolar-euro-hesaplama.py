print('Dolar-Euro Hesaplama Programına Hoşgeldiniz')
print('(Program Gireceğiniz TL Cinsinden Parayı Kaç Dolar veya Euro Olduğunu Hesaplar.)')

para=input('Hangi Para Birimine Çevirmek İstediğinizi Giriniz(Dolar-Euro):') 

TL=float (input('TL Değerini Giriniz: '))



if para=='Dolar':
 cevap = TL*0.11
 print('Cevap=', cevap)

elif para=='dolar':
 cevap = TL*0.11
 print('Cevap=', cevap)

elif para=='Euro':
 cevap = TL*0.097
 print('Cevap=', cevap)


elif para=='euro':
 cevap = TL*0.097
 print('Cevap=', cevap)

else:
 print('Yanlış Bir Değer Girdiniz.')