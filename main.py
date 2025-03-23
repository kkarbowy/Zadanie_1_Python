ZADANIA_OPCJE = [1, 2, 3]
DZIALANIA_OPCJE = ["+", "-", "*", "/"]
KONWERSJE_OPCJE = ["f", "c"]
OCENY_OPCJE = [1, 2, 3, 4, 5, 6]

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


# Funkcja do zadania 2 - konwerter temperatur    
def konwerter_temperatur(kierunek_konwersji, temperatura):
    if kierunek_konwersji == "c":
        return temperatura * 1.8 + 32
    elif kierunek_konwersji == "f":
        return (temperatura - 32) / 1.8

# Funkcja do obliczania średniej ocen
def oblicz_srednia(lista_ocen):
    suma_ocen = 0
    for ocena in lista_ocen:
        suma_ocen += ocena
    return suma_ocen / len(lista_ocen)

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

    elif wybrane_zadanie == 2:
        print("Wybierz jak chcesz przeliczać: ['c' - Celjusz -> Farenheit, 'f' - Farenheit -> Celcjusz] ")
        przelicznik = input()
        print("Wpisz wartość temperatury: ")
        temperatura = float(input())
        if przelicznik not in KONWERSJE_OPCJE:
            raise ValueError("Wprowadzono niepoprawną wartość!")
        wynik = konwerter_temperatur(przelicznik, temperatura)
        przelicznik_string = "Farenheita" if przelicznik == "c" else "Celcjusza"
        print(f"Otrzymany wynik: {wynik} stopni {przelicznik_string}")

    elif wybrane_zadanie == 3:
        print("Wpisz ile ocen podasz.")
        ilosc_ocen = int(input())
        lista_ocen = []
        for i in range(0, ilosc_ocen):
            print(f"Podaj ocenę numer: {i + 1}")
            ocena = int(input())
            if ocena not in OCENY_OPCJE:
                raise ValueError("Wprowadzono niepoprawną wartość!")
            lista_ocen.append(ocena)
        srednia = oblicz_srednia(lista_ocen)
        print(f"Średnia ocen ucznia: {srednia}")
        if srednia >= 3.0:
            print("Uczeń zdał")
        else:
            print("Uczeń nie zdał")
    

if __name__ == "__main__":
    main()