class Car:
    wheel=4
    def __init__(self, brand, typea="None"):
        self.brand=brand
        self.type=typea

class Teglalap:
    szog = 90
    def __init__(self,a_side=0,b_side=0):
        self.a_side=a_side
        self.b_side=b_side

    def terulet(self):
        return self.a_side * self.b_side

    def kerulet(self):
        return self.a_side * 2 + self.b_side * 2

class Worker:
    ceg="Minta Kft."
    def __init__(self,nev,kor,email,jelszo=""):
        self.nev=nev
        self.kor=kor
        self.email=email
        self.jelszo=jelszo
        self.agequestion()

    def agequestion(self):
        kor=input(f"Hány éves vagy {self.nev}?:")
        self.kor=kor
        error=True
        for i in range(len(kor)):
            if kor[i].isnumeric():
                error=False
                break
        if error:
            print("Nem számjegyeket adtál meg!")
            self.kor=0
        else:
            self.kor=kor
        return

#----------------------------------------------------------------
d=Worker("Pista",0,"pistabatok@mg.hu")
print(d.kor)

t=Teglalap(a_side=10,b_side=20)
print(f"A:{t.a_side},B:{t.b_side}")
print(f"terület: {t.terulet()}cm | kerület: {t.kerulet()}cm2 | szög:{t.szog}° ")


a1=Car("Peugeot","207")
a2=Car("Opel","Astra")

# a1.wheel=3
print(f"{a1.wheel,a2.wheel} car wheels: {Car.wheel}")
print(a1.brand,a1.type)
print(a2.brand,a2.type)