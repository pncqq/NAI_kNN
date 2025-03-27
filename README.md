# 📊 NAI_kNN

Implementacja algorytmu **k-Nearest Neighbors (k-NN)** do klasyfikacji danych z plików CSV. Projekt zrealizowany w ramach kursu NAI (Narzędzia AI).

## 📂 Zawartość repozytorium

- `main.py` – główny program do uruchamiania klasyfikacji k-NN
- `iris.data`, `iris.test.data` – zbior danych Iris (treningowy i testowy)
- `wdbc.data`, `wdbc.test.data` – zbior danych WDBC (opcjonalny)
- `.idea/` – pliki konfiguracyjne PyCharm

## ⚙️ Technologie

- Python 3.x

## 🧬 Funkcjonalności

- Klasyfikacja punktów testowych z wybranego pliku testowego na podstawie pliku treningowego
- Obliczanie skuteczności klasyfikacji (accuracy)
- Tryb interaktywny: użytkownik może podawać własne punkty do klasyfikacji
- Obsługa zbiorów danych o dowolnej liczbie cech

## 🔄 Parametry wejściowe

Program przyjmuje trzy argumenty:
- `k` – liczba najbliższych sąsiadów
- `train-set` – ścieżka do zbioru treningowego (CSV)
- `test-set` – ścieżka do zbioru testowego (CSV)

### ✨ Przykładowe uruchomienie:
```bash
python main.py 3 iris.data iris.test.data
```

## 🚀 Jak uruchomić

1. Sklonuj repo:
```bash
git clone https://github.com/pncqq/NAI_kNN.git
cd NAI_kNN
```

2. Uruchom program z odpowiednimi argumentami:
```bash
python main.py <k> <train-set> <test-set>
```

3. Po zakończeniu klasyfikacji program uruchomi interaktywny tryb rozpoznawania punktów wpisywanych z klawiatury.

## 📈 Dodatkowe zadania (opcjonalne)

- Testowanie zależności accuracy od wartości `k` (np. z użyciem wykresów)
- Testowanie na zbiorze WDBC (`wdbc.data`, `wdbc.test.data`)

## 👨‍💻 Autor
**Filip Michalski**  
Projekt wykonany w ramach kursu NAI jako implementacja algorytmu uczenia leniwego k-NN.
