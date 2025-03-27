from PyPDF2 import PdfReader
import pyttsx3
import time
import os

class MatematikKutuphanesi(object):

    def __init__(self, *args, **kwargs):
        print("deneme")

    def AsalSayii(self):

        print("Bir Sayı Giriniz::")
        sayi = input()
        #print("Girilen Sayı::" + sayi)
        #print("Sayinin iki katı::" + str(2*int(sayi)))
        remainder = 0
        asalmidegilmi = True #sayının asal oldğunu anlatır

        sayi = int(sayi)
        if sayi == 1:
            asalmidegilmi = False
            print(str(sayi) + " ASAL Sayı değildir")
        for s in range(2, sayi):
            asalmidegilmi = True
            #print("sayının "+ str(s) +" ye bölümünden kalan::" + str((sayi % s)))
            remainder = sayi % s

            if remainder == 0:
                asalmidegilmi = False
                print(str(sayi) + " sayısı ASAL Sayı Değildir.")
                break
        if asalmidegilmi:
            print(str(sayi) + "sayısı ASAL Sayıdır.")

    def AsalSayi(self, sayi):

        self.sayi = sayi
        #print("Girilen Sayı::" + sayi)
        #print("Sayinin iki katı::" + str(2*int(sayi)))
        remainder = 0
        asalmidegilmi = True #sayının asal oldğunu anlatır

        #sayi = int(sayi)

        if self.sayi <= 1 or isinstance(type(self.sayi), str):
            asalmidegilmi = False
            #print(str(self.sayi) + " asal sayı değildir")
            return (str(self.sayi) + " ASAL sayı değildir")
        for s in range(2, self.sayi):
            asalmidegilmi = True
            #print("sayının "+ str(s) +" ye bölümünden kalan::" + str((sayi % s)))
            remainder = self.sayi % s

            if remainder == 0:
                asalmidegilmi = False
                #print(str(self.sayi) + "sayısı ASAL Sayı Değildir.")
                return (str(self.sayi) + " sayısı ASAL Sayı Değildir.")
                break
        if asalmidegilmi:
            #print(str(self.sayi) + "sayısı ASAL Sayıdır.")
            return (str(self.sayi) + " sayısı ASAL Sayıdır")

    def AsalSayilar(self, sayi):

        self.sayi = sayi
        remainder = 0
        asalmidegilmi = True #sayının asal oldğunu anlatır

        #sayi = int(sayi)

        if self.sayi <= 1 or isinstance(type(self.sayi), str):
            asalmidegilmi = False

            return asalmidegilmi
        for s in range(2, self.sayi):
            asalmidegilmi = True
            #print("sayının "+ str(s) +" ye bölümünden kalan::" + str((sayi % s)))
            remainder = self.sayi % s

            if remainder == 0:
                asalmidegilmi = False
                #print(str(self.sayi) + "sayısı ASAL Sayı Değildir.")
                return asalmidegilmi
                break
        if asalmidegilmi:
            #print(str(self.sayi) + "sayısı ASAL Sayıdır.")
            return asalmidegilmi

    def PrimeFactors(self):
        num = int(input("Enter a number"))
        d = 2
        while num > 1:
            if num % d == 0:
                print(d)
                num = num / d
                continue
            d = d + 1
    myNumber = 0
    def SayininTersiniAlma(self, myNumber):
        self.myNumber = int(myNumber)
        #myInptNumber = int(myNumber)
        #sayi = int(input("Lütfen Tersi Alınacak Bir sayı Giriniz::"))
        #sayiis = myNumber
        terssayi = []
        while myInptNumber != 0:
            basamak = myInptNumber % 10
            #terssayi = []
            terssayi.append(basamak)
            myInptNumber = myInptNumber // 10
        print("Sayı'nın Tersi ::" + str(terssayi))
        return terssayi

    def ArmstrongSayilariBulma(self,sayi):
        alfa = int(sayi)
        basamakSayisi = len(sayi)
        basamakToplam = []
        sayi = int(sayi)
        hesSayi = sayi
        while alfa :
            basamak = sayi % 10
            basamakDeger = (basamak) ** basamakSayisi
            basamakToplam = [basamakToplam] + [basamakDeger]
            #basamakToplam.append(basamak)
            sayi = sayi // 10
            if hesSayi == basamakToplam:
                print("Armstrong Sayıdır")
            break
        return basamakToplam

    def ArmstrongOrjinal(self,sayi):

        sayi = (input("Bir Sayı giriniz::"))

        toplam = 0

        temp = int(sayi)
        basamaksayisi = len(sayi)

        while temp > 0:
            digit = temp % 10
            toplam += digit ** basamaksayisi
            temp //= 10

        if int(sayi) == toplam:
            print(sayi, "is an Armstrong number")
        else:
            print(sayi, "is not an Armstrong number")

    def KullanıcıGiris(self,sifre,kullaniciAdi):

        #kullaniciAdi = str(input("Kullanıcı Adı:: \n"))
        #sifre = str(input("Şifreyi Giriniz:: \n"))

        dogruSifre = ("y")
        dogruKullanciAdi = ("x")
        dogruGmail = ("eken.mete@gmail.com")

        deneme = 1
        while(deneme < 4) :

            kullaniciAdi = str(input("Kullanıcı Adı:: \n"))
            sifre = str(input("Şifreyi Giriniz:: \n"))

            if (kullaniciAdi == dogruKullanciAdi or kullaniciAdi == dogruGmail) and  sifre == dogruSifre:
                return ("\n Hoş Geldiniz...")
            else:
                deneme = deneme +1
                print("\n Kullanıcı Adı veya Şifre yanlış \n"+ str((3 - int(deneme-1)))+"Kadar Hakkınız Kaldı")
            if deneme == 4:
                return ("Hesabınız Bloklandı")

class Pyttsx3(object):
    engine = pyttsx3.init()
    def Volume(self):
        engine = pyttsx3.init()

        volume = engine.getProperty('volume')
        print("Current Volume:" + str(volume))

        setVolume = input("PLease Give a number between 0 and 1 to set volume:")
        soundLevel = float(setVolume)

        engine.setProperty("volume", soundLevel)
        engine.runAndWait()

        volume = engine.getProperty('volume')
        return volume

    def speechRate(self):
        engine = pyttsx3.init()

        speechRate = engine.getProperty('rate')
        print("Current Reading Speed:" + str(speechRate))

        setSpeechRate = input("Set a reading speed:")
        setSpeechRate = int(setSpeechRate)

        engine.setProperty('rate', setSpeechRate)
        engine.runAndWait()

        speechRate = engine.getProperty('rate')
        return speechRate

    def readingFromFile(self,fileToRead):

        engine = pyttsx3.init()
        file = open()

        for x in file:
            engine.say(x)
            engine.runAndWait()
        file.close()
        return

    def Voice(self):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        print("Current Voice is :" + str(voices))
        setVoice = input("Set a speaking voice:")
        engine.setProperty('voices', setVoice)
        engine.runAndWait()
        newvoices = engine.getProperty('voices')
        return newvoices

    def ReadWriteToMp3(self):

        engine = pyttsx3.init()
        file = open("E:\z1.bin", "r")

        for x in file:
            engine.say(x)
            engine.runAndWait()

        engine.save_to_file(x, 'speech.mp3')
        engine.runAndWait()
        engine.stop()
        file.close()

    def ReadFromString(self,icerik):

        readEngine = pyttsx3.init()
        #readEngine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_trTR_Tolga")
        readEngine.runAndWait()
        #for str in icerik:
        readEngine.say(icerik)
        readEngine.runAndWait()

    def change_voice(self, engine, language):
        for voice in engine.getProperty('voices'):
            if language in voice.languages :
                engine.setProperty('voice', voice.id)
                engine.runAndWait()
                return True

        raise RuntimeError("Language '{}' for gender '{}' not found".format(language))

    def sesDegistirme(self):
        engine = pyttsx3.init()
        engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_trTR_Tolga")



class PyPDF2(object):

    def PdfToText(self, fileName):
        gelenDosyaAdi = os.path.basename(fileName)
        #print(gelenDosyaAdi)
        dosyaAdi,dosyaUzantisi = os.path.splitext(gelenDosyaAdi)
        if dosyaUzantisi != ".pdf":
            return "Unsupported file extension",0
        reader = PdfReader(fileName)
        page = reader.pages[0]
        print(page.extract_text())
        number_of_pages = len(reader.pages)
        text = (page.extract_text())
        return text, number_of_pages



'''cengizMath = MatematikKutuphanesi()
meteMath = MatematikKutuphanesi()

for i in range(1, 100):
    cengizMath.AsalSayi(i)

meteMath.AsalSayii()'''