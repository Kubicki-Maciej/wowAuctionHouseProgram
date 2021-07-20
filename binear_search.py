def search(array, target):
    # Definiujmey zmienne, przechowujące zakres, który badamy

    left = 0
    right = len(array)
    index = 0

    # Sprawdzamy czy zakres który jest badany, nie jest pusty

    while left < right:

        # dzielimy listę na 2 zbiory

        index = (left + right) // 2

        # Jeżeli znaleźliśmy liczbę to kończymy
        # jeżeli lewa strona, jest mniejsza do ją odrzucamy
        # a jeżeli nie, to odrzucamy prawą stronę

        if array[index] == target:
            return index
        else:
            if array[index] < target:
                left = index + 1
            else:
                right = index

    return -1


def search_two(array, target):
    left = 0
    right = len(array)
    index = 0
    while left < right:
        index = (left + right) // 2
        if array[index].id_items == target:
            return index
        else:
            if array[index].id_items < target:
                left = index + 1
            else:
                right = index
    return -1


def search_csv(array, target):
    left = 0
    right = len(array)
    index = 0
    while left < right:
        index = (left + right) // 2
        if array[index]['name item'] == target:
            return index
        else:
            if array[index]['name item'] < target:
                left = index + 1
            else:
                right = index
    return -1