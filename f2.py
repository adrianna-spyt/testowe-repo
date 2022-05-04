# def nieparzyste(lista):
#     if len(lista) > 1:
#         if (lista[0] % 2) == 1:
#             return [lista[0]] + nieparzyste(lista[1:])
#         else:
#             return [] + nieparzyste(lista[1:])
#     else:
#         if lista[0] % 2 == 1:
#             return [lista[0]]
#         else:
#             return []


# lista1 = [1, 2, 3, 4, 5, 6]
# lista2 = [-17, 0, 999, 874, -10000, 36, 4, 93, -7]
# lista3 = [6.45, -15.3, 1, 2.2]
# print(nieparzyste(lista1))
# print(nieparzyste(lista2))
# print(nieparzyste(lista3))

# def usunnieparzyste(lista):
#     for liczba in lista[:]:
#         if liczba % 2 != 0 and liczba % 2 != 1:
#             return "Błędna lista."
#         if liczba % 2 == 1:
#             lista.remove(liczba)
#     return lista


# lista1 = [1, 2, 3, 4, 5]
# lista2 = [-17, 0, 999, 874, -10000, 36, 4, 93, -7]
# lista3 = [6, -15, 1, 2.2]
# print(usunnieparzyste(lista1))
# print(usunnieparzyste(lista2))
# print(usunnieparzyste(lista3))

# def alternatywa_rozlaczna(zmiennaP, zmiennaQ):
#     if (poprawnosc(zmiennaP) and poprawnosc(zmiennaQ))== "Zmienna jest poprawna.":
#         if (zmiennaP == 1 and zmiennaQ == 0) or (zmiennaP == 0 and zmiennaQ == 1):
#             return "True"
#         else:
#             return "False"
#     else:
#         return "Brak odpowiedzi - błędna zmienna."


# def poprawnosc(zmienna):
#     if zmienna == 1 or zmienna == 0:
#         return "Zmienna jest poprawna."
#     else:
#         return "Zmienna jest niepoprawna."


# ptrue = 1
# pfalse = 0
# qtrue = 1
# qfalse = 0
# print("Dla p =", ptrue, "-", poprawnosc(ptrue), "\nI dla q =", qtrue, "-", poprawnosc(qtrue))
# print("Wynikiem alternatywy rozłącznej jest", alternatywa_rozlaczna(ptrue, qtrue))
# print("Dla p =", ptrue, "-", poprawnosc(ptrue), "\nI dla q =", qfalse, "-", poprawnosc(qfalse))
# print("Wynikiem alternatywy rozłącznej jest", alternatywa_rozlaczna(ptrue, qfalse))
# print("Dla p =", pfalse, "-", poprawnosc(pfalse), "\nI dla q =", qtrue, "-", poprawnosc(qtrue))
# print("Wynikiem alternatywy rozłącznej jest", alternatywa_rozlaczna(pfalse, qtrue))
# print("Dla p =", pfalse, "-", poprawnosc(pfalse), "\nI dla q =", qfalse, "-", poprawnosc(qfalse))
# print("Wynikiem alternatywy rozłącznej jest", alternatywa_rozlaczna(pfalse, qfalse))

# print("Dla p =", 7, "-", poprawnosc(7), "\nI dla q =", -3, "-", poprawnosc(-3))
# print("Wynikiem alternatywy rozłącznej jest", alternatywa_rozlaczna(7, -3))
