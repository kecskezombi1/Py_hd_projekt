def osszeadas(a,b):
    return a+b

if __name__ == "__main__":
    x=3
    y=4
    print(osszeadas(x,y))

    sorozat=[1,2,9,4,6,8]
    for elem in sorozat:
        if elem == 5:
            continue
        print(elem)
        if elem == 6:
            break
    else:
        print("VÉGE")
    print()

    for elem in range(1,10,2):
        print(elem)
    print()

    for elem in "Jó reggelt!":
        print(elem)

    #hibas futas

    s=0
    x='szia'
    try:
        eredmeny=x/s
    except ZeroDivisionError:
        eredmeny=0
        print(f"hiba mivel a szám {s}")
    except TypeError:
        eredmeny=1
        print(f"Az egyik ertek hibas '{x}'")
    else:
        print(eredmeny)