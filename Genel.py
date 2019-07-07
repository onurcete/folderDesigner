#print("onur")
#dosya= open("deneme.txt","w")
#print("onurceter",file=dosya)
#dosya.close()

#import sys
#print("Tahir olmak da ayip degil", "Zuhre olmak da", sep=" ", end="\n", file=sys.stdout)

#f= open("deneme.txt","w")
#print("bir",file=f)
#print("iki",file=f)
#f.close()

#f=open("deneme.txt","w")
#print("onurceter",file=f,flush=True)

#print(*"linux",sep=".")
#print(*"linux")
#print("Yarin Adana\'ya gidiyorum")
#print("birinci satir\nikinci satir\nuçuncu satir")

#baslik="Onur Cete Deneme Lisesi"
#print(baslik, "\n", "-"*len(baslik), sep="")

#print("abc\tdef")
#print("bir", "iki", "uc", sep="\t")
#print(*"123456789", sep="\t")

#print("\a")

#print("dusey\vsekme")

#Kaçış Dizisi Anlamı
#\’ Karakter dizisi içinde tek tırnak işaretini kullanabilmemizi sağlar.
#\” Karakter dizisi içinde çift tırnak işaretini kullanabilmemizi sağlar.
#\\ Karakter dizisi içinde \ işaretini kullanabilmemizi sağlar.
#\n Yeni bir satıra geçmemizi sağlar.
#\t Karakterler arasında sekme boşluğu bırakmamızı sağlar.
#\u UNICODE kod konumlarını gösterebilmemizi sağlar.
#\U UNICODE kod konumlarını gösterebilmemizi sağlar.
#\N Karakterleri UNICODE adlarına göre kullanabilmemizi sağlar.
#\x Onaltılı sistemdeki bir sayının karakter karşılığını gösterebilmemizi sağlar.
#\a Destekleyen sistemlerde, kasa hoparlöründen bir ‘bip’ sesi verilmesinisağlar.
#\r Aynı satırın başına dönülmesini sağlar.
#\v Destekleyen sistemlerde düşey sekme oluşturulmasını sağlar.
#\b İmlecin sola doğru kaydırılmasını sağlar
#\f Yeni bir sayfaya geçilmesini sağlar.
#r Karakter dizisi içinde kaçış dizilerini kullanabilmemizi sağlar.

#isim = input("İsminiz nedir? ")
#print("Merhaba", isim, end="!\n")

#sayi=input("Yari cap bilgisi giriniz:")
#print("cap olarak",sayi,"girdiniz")
#print("sayinin turu:",type(sayi))
#print("iyi gunler")

#url = input("site: ")
#print("Hata! Google Chrome {} sitesini bulamadi".format(url))

#metin = "{} ve {} iyi bir ikilidir"
#print(metin.format("Python", "Django"))

#a=56
#if a < 4:
#    print("1")
#elif a> 5:
#    print("3")
#else:
#    print("2")

##############################################
#username = input("Kullanici adi giriniz:")
#password = input("Sifre giriniz:")

#lenn= len(username)+ len(password)

#print("Bilgiler toplami {} dir".format(lenn))
#mesaj="bilgiler toplami {} dir"
#print(mesaj.format(lenn))

##############################################
#sayi = int(input("sayi giriniz"))
#s=sayi%2

#if s==0:
#    print("cift sayi")
#else:
#    print("tek")
##############################################

#bolen= int(input("bolen sayi:"))
#bolunen= int(input("bolunen sayi:"))

#mesaj= "{} sayisi {} sayisina tam".format(bolunen,bolen)

#if bolunen % bolen == 0 :
#    print(mesaj,"bolunur")
#else:
#    print(mesaj,"bolunmez")
##############################################

#print("""Hesap Makinesi
#(1)Toplama
#3(2)Cikarma
#""","*"*len("Hesap Makinesi"), sep="")

#islem=input("Hangi islemi yapmak istiyorsunuz?:")

#sayi1=int(input("birinci sayi:"))
#sayi2=int(input("ikinci sayi:"))

#if islem == "1":
#    sonuc = sayi1+sayi2
#elif islem =="2":
#    sonuc = sayi1-sayi2
#print("sonuc:",sonuc)

##############################################

#print("{0}\n{1}".format(a//b, a/b))
##############################################

#print("""Hesap Makinesi
#(1)Toplama
#3(2)Cikarma
#""","*"*len("Hesap Makinesi"), sep="")
#anahtar=1

#while anahtar == 1:
#    islem=input("Hangi islemi yapmak istiyorsunuz?:")
#
#    if islem =="q":
#        anahtar = 0
#        print("Cikiliyor...")
#    elif islem == "1":
#        sayi1=int(input("birinci sayi:"))
#       sayi2=int(input("ikinci sayi:"))
#        sonuc = sayi1+sayi2
#       print("sonuc:",sonuc)
#    elif islem =="2":
#        sayi1=int(input("birinci sayi:"))
#        sayi2=int(input("ikinci sayi:"))
#        sonuc = sayi1-sayi2
#        print("sonuc:",sonuc)


#a = 0
#while a < 100:
#    a += 1
#    if a % 2 == 0:
#        print(a) 

    
#tr_harfler = "abcd"
#for harf in tr_harfler:
#        print(harf)


#tr_harfler = "abcde"
#a = 0
#while a < len(tr_harfler):
#    print(tr_harfler[a], sep="\n")
#    a += 1  

#ilk_metin = "asdasfddgdhfjfdgdşfkgjdfklgşjdfklgjdfkghdfjghjklsdhajlsdhjkjhkhjjh"
#ikinci_metin = "sdfsuıdoryeuıfsjkdfhdjklghjdfklruseldhfjlkdshfljskeeuf"
#for s in ilk_metin:
#    if not s in ikinci_metin:
#        print(s)


#ilk_metin = "abcefg"
#ikinci_metin = "bgtrek"
#fark = ''
#for s in ikinci_metin:
#    if not s in ilk_metin:
#        if not s in fark:
#            fark += s
#print(fark)



#n = int(input())
#for n in range(0,n):
#    print(n*n)

#nesne = "123456789"
#for n in nesne:
#    print(int(n) * 2)

#site1 = "www.google.com"
#site2 = "www.istihza.com"
#site3 = "www.yahoo.com"
#site4 = "www.gnu.org"
#for isim in site1, site2, site3, site4:
#    print("site: ", isim[4:-4])


#a = "istanbul"
#print(a[::])
#print(a[::1])
#print(a[::2])
#print(a[0:8:1])
#print(a[::-1])
#print(a[7:4:-1])

#print(sorted("kitap"))
#print(*sorted("kitap"), sep="")

site1 = "www.google.com"
site2 = "www.istihza.com"
for i in site1, site2:
    print("http://", i, sep="")
for i in site1, site2:
    print("http://", i[4:], sep="")