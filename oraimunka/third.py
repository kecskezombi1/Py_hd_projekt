import datetime as dt
import random as rnd
from venv import __main__


#nyelvi szerkezetek

def ker_ter (a,b):
    k = 2 * a + 2 * b
    return k

def otoslotto():
    print("Otoslotto:")
    i=0
    while i<5:
        print(rnd.randint(1,90))
        i=i+1

if __name__=="__main__":
    print("Energia ital kiadás")
    ev_fel=int(input('év:'))
    ho_fel=int(input('hó:'))
    nap_fel=int(input('nap:'))
    felhasznalo_datum=dt.date(year=ev_fel,month=ho_fel,day=nap_fel)
    cel_date=dt.date(day=20,month=9,year=2008)

    if felhasznalo_datum<cel_date:
        print("Jováhagyva.")
    else:
        print("Elutasítva.")

    i = 1
    stopolo=int(input('stopolo:'))
    while i <=10:
        print(i)
        i=i+1
        if i==3:
            continue
        if i==stopolo:
            break
    else:
        print('Gond nélkül lefutott!')
    print("vege a ciklusnak")


    alap=5
    magassag=3
    print(ker_ter(2,1))

    #kerulet=ker_ter(alap,magassag)[0]
    #terulet=ker_ter(alap,magassag)[1]
    #print(f'Kerület={kerulet}\n Terület={terulet}')

    #eredemeny=ker_ter(alap,magassag)
    #print(f'Kerület={eredemeny[0]}\n Terület={terulet}')

otoslotto()