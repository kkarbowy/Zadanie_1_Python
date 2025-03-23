ZADANIA_OPCJE = [1, 2, 3]
DZIALANIA_OPCJE = ["+", "-", "*", "/"]

# Funkcja do zadania 1 - kalkulator
def kalkulator(liczba1, liczba2, dzialanie):
    if dzialanie == "+":
        return liczba1 + liczba2
    elif dzialanie == "-":
        return liczba1 - liczba2
    elif dzialanie == "*":
        return liczba1 * liczba2
    elif dzialanie == "/":
        if liczba2 == 0:
            return "Nie można dzielić przez zero!"
        return liczba1 / liczba2

# Obsługa logiki programu
def main():
    print("Wybierz zadanie wpisując w terminalu odpowiednią cyfrę: 1 - prosty kalkulator, 2 - konwerter temperatur, 3 - średnia ocen ucznia.")

    wybrane_zadanie = int(input())
    if wybrane_zadanie not in ZADANIA_OPCJE:
        raise ValueError("Wprowadzono niepoprawną wartość!")
    
    if wybrane_zadanie == 1:
        print("Wpisz wartość pierwszej liczby: ")
        liczba1 = float(input())
        print("Wpisz wartość drugiej liczby: ")
        liczba2 = float(input())
        print("Wybierz działanie, które chcesz wykonać z dostępnych w liście [+, -, *, /]: ")
        dzialanie = input()
        if dzialanie not in DZIALANIA_OPCJE:
            raise ValueError("Wprowadzono niepoprawną wartość!")
        wynik = kalkulator(liczba1, liczba2, dzialanie)
        print(f"Otrzymany wynik: {wynik}")

    


if __name__ == "__main__":
    main()