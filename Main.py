def Eggyenlotlenseg():
    a: float = input("Kérem adja meg az a oldalt: ")
    b: float = input("Kérem adja meg az b oldalt: ")
    c: float = input("Kérem adja meg az c oldalt: ")

    possible: bool = False
    if not possible: possible = a + b > c
    if not possible: possible = a + c > b
    if not possible: possible = b + c > a

    print(f"Ezekkel az oldalakkal{"" if possible else " nem"} lehetséges háromszöget csinálni!")


if __name__ == "__main__":
    Eggyenlotlenseg()
