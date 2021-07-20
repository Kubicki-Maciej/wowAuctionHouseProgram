# https://www.geeksforgeeks.org/binary-search-a-string/


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


def binarySearchOnStringPandas(arr, x):

    l = 0
    r = len(arr) - 1
    while (l <= r):
        m = (l + r) // 2
        if (arr[m][1] == x):
            return m
        elif (arr[m][1] < x):
            l = m + 1
        else:
            r = m - 1
    return -1