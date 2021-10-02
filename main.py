# Program wspomagajacy paczkowanie.
# Program przyjmuje z klawiatury masy elementow i dodaje je do paczki.
# Dopuszczalna masa maksymalna paczki - 20 kg.
# Masy elemetow: od 1 kg do 10 kg.
# Program zwraca na koniec nastepujace informacje:
#   - liczba wyslanych paczek ogolem
#   - liczba wyslanych kilogramow ogolem
#   - liczba "pustych" kilogramow ogolem
#   - nr najlzejszej paczki i liczba "pustych" kilogramow w tej paczce
# Program konczy dzialanie i wyswietla raport po podaniu masy elementu 0 kg.
# Masa paczki z przedzialu (0, 1) kg konczy dzialanie programu bledem.

print('Program wspomagajacy paczkowanie.')
print('Podaj z klawiatury mase elementu z przedzialu od 1 kg do 10 kg.')
print('Masa elementu wieksza od 0 kg i mniejsza od 1 kg jest niedopuszczalna '
      'i konczy dzialanie programu bledem.')
print('Podanie wartosci 0 konczy dzialanie programu i wyswietla raport '
      'koncowy.')
print()
print('Program NIE JEST IDIOTOODPORNY - prosze podawac tylko liczby '
      'calkowite lub dziesietne.')
print()

# zmienne, ktorych przeznaczenie jest chyba oczywiste:
maks_masa_paczki = 20.0
maks_masa_elementu = 10.0
min_masa_elementu = 1.0
masa_elementu = 0.0
masa_biezacej_paczki = 0.0
liczba_wyslanych_paczek = 0
liczba_wyslanych_kilogramow = 0.0
nr_najlzejszej_paczki = 0
masa_najlzejszej_paczki = maks_masa_paczki
# zmienna do sygnalizowania poprawnosci masy paczki, kontrola wyjscia
# z petli WHILE i wydruku raportu koncowego:
czujka = True

while czujka:
  print('Podaj mase elementu (podanie masy elementu 0 kg konczy program): ',
        end='')
  masa_elementu = float(input())
  # podana masa elementu wykracza poza dopuszczalny zakres - natychmiastowe
  # wyjscie z programu:
  if (masa_elementu < min_masa_elementu and masa_elementu != 0) \
          or masa_elementu > maks_masa_elementu:
    czujka = False
    print('---------------------------------------------------')
    print('I po balu panno Lalu - niedozwolona masa paczki !!!')
    print('Zacznij od nowa.')
    print('---------------------------------------------------')
    print('Nacisnij ENTER zeby zakonczyc ', end='')
    input()
    break
  # masa elementu miesci sie w zakresie dopuszczalnym jest niezerowa:
  if masa_elementu >= min_masa_elementu:
    # zwiekszyc kilogramy wyslane ogolem:
    liczba_wyslanych_kilogramow += masa_elementu
    # sprawdzic, czy mozna dodac element do biezacej paczki:
    if masa_elementu + masa_biezacej_paczki <= maks_masa_paczki:
      # - TAK, dodac do biezacej:
      masa_biezacej_paczki += masa_elementu
      # - sprawdzic, czy to jest pierwsza paczka, jesli TAK to numer 1:
      if liczba_wyslanych_paczek == 0:
        liczba_wyslanych_paczek = 1
    else:
      # - NIE, dodac do kolejnej:
      # najpierw sprawdzic, czy ostatnia paczka jest najlzejsza:
      if masa_biezacej_paczki < masa_najlzejszej_paczki:
        masa_najlzejszej_paczki = masa_biezacej_paczki
        nr_najlzejszej_paczki = liczba_wyslanych_paczek
      # teraz dodac element do nowej paczki:
      liczba_wyslanych_paczek += 1
      masa_biezacej_paczki = masa_elementu
  else:
    # wprowadzono mase zero:
    # najpierw sprawdzic, czy ostatnia paczka jest najlzejsza:
    if masa_biezacej_paczki < masa_najlzejszej_paczki:
      masa_najlzejszej_paczki = masa_biezacej_paczki
      nr_najlzejszej_paczki = liczba_wyslanych_paczek
    # wyjscie z petli WHILE
    break

# nie bylo blednego wprowadzenia masy elementu, drukowanie raportu koncowego:
if czujka:
  print()
  print('Raport koncowy:')
  print('---------------------------------------------')
  # czy wyslano chocby jedna paczke:
  # - NIE
  if liczba_wyslanych_paczek == 0:
    print('Wyslano {} paczek. Nic wiecej do zakomunikowania.'
          .format(liczba_wyslanych_paczek))
  # - TAK, wyslano co najmniej jedna paczke
  else:
    print('Ogolem wyslano {} paczke/paczki/paczek.'
          .format(liczba_wyslanych_paczek))
    print('Ogolem wyslano {} kilogramow.'.format(liczba_wyslanych_kilogramow))
    print('Ogolem wyslano {} "puste" kilogramy/"pustych" kilogramow.'
          .format(maks_masa_paczki * liczba_wyslanych_paczek
                  - liczba_wyslanych_kilogramow))
    print('Najwiecej "pustych" kilogamow ({}) w paczce nr {}.'
          .format(maks_masa_paczki - masa_najlzejszej_paczki,
                  nr_najlzejszej_paczki))
