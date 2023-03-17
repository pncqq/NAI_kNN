# NAI-miniproject-kNN

Celem jest napisanie programu, ktory pobiera następujące argumenty:
k: dodatnia liczba naturalna będąca hiperparametrem k-NN.
train-set: nazwa pliku zawierającego zbiór treningowy w postaci csv – ostatnia kolumna
zawiera atrybut decyzyjny.
test-set: nazwa pliku zawierajacego zbiór testowy w postaci csv – ostatnia kolumna
zawiera atrybut decyzyjny.
Wymagania:
 Program powinien dokonać klasyfikacji k-NN wszystkich obserwacji z pliku test-set
na podstawie pliku train-set oraz podać dokladność (accuracy) tej klasyfikacji
(proporcję poprawnie zaklasyfikowanych przykładów testowych).
 Program ma też dostarczać testowy interfejs (niekoniecznie graficzny), który umożliwia
(zapętlone) podawanie przez użytkownika pojedynczych wektorów do klasyfikacji
i podaje ich etykietę k-NN na podstawie train-set.
 Przetestować na danych ze zbiorów treningowego i testowego znajdujących się w
plikach iris.data i iris.test.data.
 Uwaga: Program powinien przyjąć dowolny zbiór danych (w formacie podobnym
do iris.data) i dostosować się do dowolnej liczby wymiarów.
 Opcjonalnie (dodatkowy punkt za aktywność): dowolną techniką (excel, python,
etc.) zrobić wykres zależności dokładności (accuracy) od wartości k.
 Opcjonalnie (dodatkowy punkt za aktywność): Testować także zbiór WDBC
w wdbc.data i wdbc.test.data.
