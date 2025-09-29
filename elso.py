def Eggyenlotlenseg():
    a: float = float(input("Kérem adja meg az a oldalt: "))
    b: float = float(input("Kérem adja meg az b oldalt: "))
    c: float = float(input("Kérem adja meg az c oldalt: "))

    possible: bool = True

    if possible: possible = (a + b) > c
    if possible: possible = (a + c) > b
    if possible: possible = (b + c) > a

    print(f"Ezekkel az oldalakkal{"" if possible else " nem"} lehetséges háromszöget csinálni!")

if __name__ == "__main__":
    Eggyenlotlenseg()
