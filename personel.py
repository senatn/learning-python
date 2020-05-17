class Calisan():
    _personel = []

    def __init__(self, isim):
        self._isim = isim
        self.personel_ekle()

    def personel_ekle(self):
        self._personel.append(self._isim)
        print('{} adli kisi personele eklendi'.format(self._isim))

    @classmethod
    def personeli_goruntule(cls):
        print('Personel lisresi:')
        for i in cls._personel:
            print(i)

    @property
    def isim(self):
        return self._isim
    @isim.setter
    def isim(self, yeni_isim):
        kisi = self._personel.index(self.isim)
        self._personel[kisi] = yeni_isim
        print('Yeni isim: ',yeni_isim)


c1 = Calisan('musa')

c1.isim = 'sena'

Calisan.personeli_goruntule()

