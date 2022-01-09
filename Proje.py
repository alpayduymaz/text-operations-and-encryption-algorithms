import hashlib

class dilKontrol:
	def init(self, metin):
		self.metin=metin
	def cumlelereBol(self,metin):
	    parcalananMetin=metin.split(".")
	    return parcalananMetin,len(parcalananMetin)
	def kelimelereBol(self,metin):
	    parcalananCumle=metin.split()
	    return parcalananCumle,len(parcalananCumle)
	def sesliHarfAdediBul(self,metin):
	    sesli_harf = 'AEIİOÖUÜaeıioöuü'
	    sayac = 0
	    for i in metin:
	        if i in sesli_harf:
	            sayac += 1
	    return sayac
	def buyukunluUyumuKontrolEt(self,metin):
	    sesliharfler= ["a","e","ı","i","o","ö","u","ü"]
	    kalinunluler= ["a","ı","o","u"]
	    inceunluler= ["e","i","o","ü"]
	    kelimeler=metin.split()
	    uyanlar=[]
	    uymayanlar=[]
	    tekhece=[]
	    for i in range(len(kelimeler)):
	        icindekisesli=[]
	        for j in range(len(kelimeler[i])):
	            if kelimeler[i][j] in sesliharfler:
	                icindekisesli.append(kelimeler[i][j])
	        if len(icindekisesli)==1:
	            print("{} gibi tek heceli kelimelerde büyük ünlü uyumu aranmaz".format(kelimeler[i]))
	            tekhece.append(kelimeler[i])
	        else:
	            if list(icindekisesli)[0] in kalinunluler:
	                if set(icindekisesli).issubset(set(kalinunluler)):
	                    uyanlar.append(kelimeler[i])
	                else:
	                    uymayanlar.append(kelimeler[i])
	            else:
	                if set(icindekisesli).issubset(set(inceunluler)):
	                    uyanlar.append(kelimeler[i])
	                else:
	                    uymayanlar.append(kelimeler[i])
	    return len(uyanlar),len(uymayanlar)

class sifrelemeYontemleri:
    def init(self, metin):
        self.metin=metin
    def md5(self,metin):
        hash_object = hashlib.md5(metin.encode())
        hex_dig = hash_object.hexdigest()
        return 
    def SHA1(self,metin):
        hash_object = hashlib.sha1(metin.encode())
        hex_dig = hash_object.hexdigest()
        return hex_dig
    def SHA224(self,metin):
        hash_object = hashlib.sha224(metin.encode())
        hex_dig = hash_object.hexdigest()
        return hex_dig
    def SHA256(self,metin):
        hash_object = hashlib.sha256(metin.encode())
        hex_dig = hash_object.hexdigest()
        return hex_dig
    def SHA384(self,metin):
        hash_object = hashlib.sha384(metin.encode())
        hex_dig = hash_object.hexdigest()
        return hex_dig
    def SHA512(self,metin):
        hash_object = hashlib.sha512(metin.encode())
        hex_dig = hash_object.hexdigest()
        return hex_dig

class help:
    def Islemler(self):
        print("Dil kontrol sinifi her hangi bir metni cümlelere ve kelimelere bölebilir. Metin içerisinde kac adet cümle oldugunu kac adet kelime oldugunu ve kac adet kelimenin büyük ünlü uyumu sagladigini, kac adet kelimenin saglamadigini gösterir. Metin icerisinde kac adet ünlü harf bulundugunu gösterir\nSifreleme sinifi ise metni hash, simetrik ve asimetrik sifreleme yöntemleri ile sifrelemektedir.\nDil kontrol için 1\nŞifreleme islemleri icin 2ye basiniz\n")
        hangisi=input()
        return hangisi

metin=input('Metni Giriniz=')
print(metin)
islem=input('Yapilacak islemi seciniz\n1- Dil Kontrol\n2- Sifreleme\n3- Help\n')
try:
    if islem == "1":
        nesne=dilKontrol()
        cumleArray,cumleSayisi=nesne.cumlelereBol(metin)
        print(cumleArray,"Cümle sayisi =",cumleSayisi)
        kelimeArray,kelimeSayisi=nesne.kelimelereBol(metin)
        print(kelimeArray,"Kelime sayisi =",kelimeSayisi)
        sesliHarfSayisi=nesne.sesliHarfAdediBul(metin)
        print("Sesli harf adedi =",sesliHarfSayisi)
        uyanSayisi,uymayanSayisi=nesne.buyukunluUyumuKontrolEt(metin)
        print("Büyük ünlü uyumuna uyan kelime sayisi =",uyanSayisi,"\nBüyük ünlü uyumuna uymayan kelime sayisi =",uymayanSayisi)
    elif islem == "2":
        sifrelemeNesnesi=sifrelemeYontemleri()
        print("Sifreleme yapilacak yöntemin adini giriniz")
        sifrelemeAdi=input()
        if sifrelemeAdi=="md5":
            sifrelenenString=sifrelemeNesnesi.md5(metin)
            print("Sifrelenen string = ",sifrelenenString)
        elif sifrelemeAdi=="SHA1":
            sifrelenenString=sifrelemeNesnesi.SHA1(metin)
            print("Sifrelenen string = ",sifrelenenString)
        elif sifrelemeAdi=="SHA224":
            sifrelenenString=sifrelemeNesnesi.SHA224(metin)
            print("Sifrelenen string = ",sifrelenenString)
        elif sifrelemeAdi=="SHA256":
            sifrelenenString=sifrelemeNesnesi.SHA256(metin)
            print("Sifrelenen string = ",sifrelenenString)
        elif sifrelemeAdi=="SHA384":
            sifrelenenString=sifrelemeNesnesi.SHA384(metin)
            print("Sifrelenen string = ",sifrelenenString)
        elif sifrelemeAdi=="SHA512":
            sifrelenenString=sifrelemeNesnesi.SHA512(metin)
            print("Sifrelenen string = ",sifrelenenString)
    elif islem == "3":
        obje=help()
        if obje.Islemler() == "1":
            nesne=dilKontrol()
            print("Metni giriniz")
            metin=input()
            cumleArray,cumleSayisi=nesne.cumlelereBol(metin)
            print(cumleArray,"Cümle sayisi =",cumleSayisi)
            kelimeArray,kelimeSayisi=nesne.kelimelereBol(metin)
            print(kelimeArray,"Kelime sayisi =",kelimeSayisi)
            sesliHarfSayisi=nesne.sesliHarfAdediBul(metin)
            print("Sesli harf adedi =",sesliHarfSayisi)
            uyanSayisi,uymayanSayisi=nesne.buyukunluUyumuKontrolEt(metin)
            print("Büyük ünlü uyumuna uyan kelime sayisi =",uyanSayisi,"\nBüyük ünlü uyumuna uymayan kelime sayisi =",uymayanSayisi)
        elif obje.Islemler() == "2":
            sifrelemeNesnesi=sifrelemeYontemleri()
            print("Sifrelenecek metni giriniz")
            metin=input()
            print("Sifreleme yapilacak yöntemin adini giriniz")
            sifrelemeAdi=input()
            if sifrelemeAdi=="md5":
                sifrelenenString=sifrelemeNesnesi.md5(metin)
                print("Sifrelenen string = ",sifrelenenString)
            elif sifrelemeAdi=="SHA1":
                sifrelenenString=sifrelemeNesnesi.SHA1(metin)
                print("Sifrelenen string = ",sifrelenenString)
            elif sifrelemeAdi=="SHA224":
                sifrelenenString=sifrelemeNesnesi.SHA224(metin)
                print("Sifrelenen string = ",sifrelenenString)
            elif sifrelemeAdi=="SHA256":
                sifrelenenString=sifrelemeNesnesi.SHA256(metin)
                print("Sifrelenen string = ",sifrelenenString)
            elif sifrelemeAdi=="SHA384":
                sifrelenenString=sifrelemeNesnesi.SHA384(metin)
                print("Sifrelenen string = ",sifrelenenString)
            elif sifrelemeAdi=="SHA512":
                sifrelenenString=sifrelemeNesnesi.SHA512(metin)
                print("Sifrelenen string = ",sifrelenenString)
except:
    print("Hatali Giris Yaptiniz. Lütfen 1 2 veya 3 Giriniz...")