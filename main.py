class Valyuta:
    def __init__(self, nom, kurs):
        self.nom = nom
        self.kurs = kurs

    def aylantir(self, kurs):
        self.kurs = kurs

class ValyutaKurslar:
    def __init__(self):
        self.valyuta = {}

    def qo'sh(self, valyuta):
        self.valyuta[valyuta.nom] = valyuta

    def o'chir(self, nom):
        if nom in self.valyuta:
            del self.valyuta[nom]

    def aylantir(self, nom, kurs):
        if nom in self.valyuta:
            self.valyuta[nom].aylantir(kurs)

    def ko'rish(self):
        for valyuta in self.valyuta.values():
            print(f"Valyuta: {valyuta.nom}, Kurs: {valyuta.kurs}")

# Misol:
kurslar = ValyutaKurslar()

usd = Valyuta("USD", 1)
eur = Valyuta("EUR", 0.88)
rub = Valyuta("RUB", 73.5)

kurslar.qo'sh(usd)
kurslar.qo'sh(eur)
kurslar.qo'sh(rub)

kurslar.ko'rish()

kurslar.aylantir("USD", 1.1)
kurslar.aylantir("EUR", 0.9)
kurslar.aylantir("RUB", 75)

kurslar.ko'rish()
```

Bu kodda biz valyuta kurslarini aylantiruvchi dastur yozdik. Dasturda `Valyuta` classi valyuta nomi va kursini saqlaydi, `ValyutaKurslar` classi valyuta kurslarini saqlaydi va ularni aylantiradi.
