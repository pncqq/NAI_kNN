import csv
import numpy as np


# Wczytywanie danych z pliku CSV
def load_data(file_name):
    data = []
    label_to_numeric = {}
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            label = row[-1]
            if label not in label_to_numeric:
                label_to_numeric[label] = len(label_to_numeric)
            numeric_label = label_to_numeric[label]

            data.append([float(i) if idx != len(row) - 1 else numeric_label for idx, i in enumerate(row)])
    return data


# Obliczanie odległości eukliedesowej
def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((np.array(x1) - np.array(x2)) ** 2))


# Znajdowanie k najbliższych sąsiadów
def get_neighbors(train_set, test_instance, k):
    distances = []
    for train_instance in train_set:
        dist = euclidean_distance(train_instance[:-1], test_instance)
        distances.append((train_instance, dist))
    distances.sort(key=lambda x: x[1])
    # bierzemy k najblizszych elementów
    neighbors = [x[0] for x in distances[:k]]
    return neighbors


# Predykcja dla pojedynczego wektora
def predict(train_set, test_instance, k):
    neighbors = get_neighbors(train_set, test_instance, k)
    #patrzymy jakie etykiety mają sąsiedzi
    classes = [x[-1] for x in neighbors]
    #zliczamy najczęstszą etykietę
    prediction = max(set(classes), key=classes.count)
    return prediction


# Dokładność predykcji
def accuracy(actual_labels, predictions):
    correct = 0
    for i in range(len(actual_labels)):
        if actual_labels[i] == predictions[i]:
            correct += 1
    return correct / float(len(actual_labels))


def main(k, train_file, test_file):
    # wczytaj zbiory treningowy i testowy
    train_set = load_data(train_file)
    test_set = load_data(test_file)

    # dokonaj predykcji dla wszystkich obserwacji ze zbioru testowego
    predictions = []
    for test_instance in test_set:
        predictions.append(predict(train_set, test_instance[:-1], k))

    # wyznacz rzeczywiste etykiety dla zbioru testowego
    actual_labels = [instance[-1] for instance in test_set]


    # wyświetl wyniki klasyfikacji
    print('Przewidywane etykiety: ', predictions)
    print('Rzeczywiste etykiety: ', actual_labels)
    print('Dokładność: ', accuracy(actual_labels, predictions))

    # testowanie
    while True:
        input_str = input('Wpisz testowy wektor (odzielony przecinkami): ')
        if input_str == 'exit':
            break
        test_instance = [float(i) for i in input_str.split(',')]
        prediction = predict(train_set, test_instance, k)
        print('Przewidywanie:', prediction)


if __name__ == '__main__':
    main(200, 'wdbc.data', 'wdbc.test.data')
