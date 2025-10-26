# https://github.com/emiltys/python-intro/
# Emil Tyszka Nr albumu: 167055
#
# --- Laboratorium 1:
#
# Funkcja zip(): Funkcja ta tworzy iterator, który łączy
# elementy z wielu list (lub innych iterowalnych obiektów) w krotki (pary, trójki itd.).
# Działa "jak zamek błyskawiczny" i kończy się, gdy najkrótsza lista się skończy.
# Link do dokumentacji: https://docs.python.org/3/library/functions.html#zip

przedmioty = ["Matematyka", "Fizyka", "Informatyka"]
oceny = [5, 4, 5]

# Użyta została funkcja zip() do połączenia list, a następnie list() aby zobaczyć wynik
oceny_semestralne = list(zip(przedmioty, oceny))

print(f"Połączone przedmioty i oceny: {oceny_semestralne}")
print("-" * 20) # Linia separująca dla czytelności

# Moduł 'math': Ten moduł zapewnia dostęp do funkcji matematycznych
# (np. pierwiastek, logarytm, funkcje trygonometryczne)
# oraz stałych (jak pi).
# Link do dokumentacji: https://docs.python.org/3/library/math.html
import math

# Użycie funkcji 'sqrt()' (square root - pierwiastek kwadratowy) z modułu math
liczba = 64
pierwiastek = math.sqrt(liczba)

print(f"Pierwiastek kwadratowy z {liczba} to: {pierwiastek}")
print("-" * 20)

# Obsługa wyjątku 'ZeroDivisionError': Jest to błąd (wyjątek) zgłaszany,
# gdy w operacji dzielenia lub modulo, drugi argument (dzielnik) wynosi zero.
# Link do dokumentacji: https://docs.python.org/3/library/exceptions.html#ZeroDivisionError

licznik = 100
mianownik = 0

try:
    # Próba wykonania operacji
    wynik_dzielenia = licznik / mianownik
    print(f"Wynik dzielenia: {wynik_dzielenia}")
except ZeroDivisionError:
    # Ten blok wykona się tylko wtedy, gdy w bloku 'try' wystąpi błąd ZeroDivisionError
    print(f"Wystąpił błąd: Próba dzielenia przez zero (mianownik = {mianownik})!")

print("-" * 20)
print("Program zakończył działanie.")