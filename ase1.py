import numpy as np
import time


l_elem = 10000
tab = []

def losowanie(tab):
    for i in range(l_elem):
        liczba = np.random.randint(1000000)
        if liczba not in tab:
            tab.append(liczba)

def babelkowy(tab):
    for i in range(dlugosc):
        j = dlugosc - 1
        while j > i:
            if tab[j] < tab[j - 1]:
                buf = tab[j]
                tab[j] = tab[j - 1]
                tab[j - 1] = buf
            j -= 1
    return tab


def wymiana(tab):
    for i in range(0, dlugosc-1):
        najmniejszy = min(tab[i:])
        # print(najmniejszy)
        gdzie = tab.index(najmniejszy)
        buf = tab[i]
        tab[i] = tab[gdzie]
        tab[gdzie] = buf
        # i+=1
    return tab


def quicksort(tab):
    mniejsze = []
    wieksze = []
    rowne = []
    if len(tab) <= 1:
        return tab
    else:
        pivot = tab[0]
        for liczba in tab:
            if liczba < pivot:
                mniejsze.append(liczba)
            elif liczba > pivot:
                wieksze.append(liczba)
            elif liczba == pivot:
                rowne.append(liczba)
            mniejsze = quicksort(mniejsze)
            wieksze = quicksort(wieksze)
            return mniejsze, wieksze, rowne


losowanie(tab)
print(tab)
babelkowy_tab = tab
wymiana_tab = tab
quicksort_tab = tab

dlugosc = len(tab)

print("bąbelkowy")
czas_start = time.time()
babelkowy(babelkowy_tab)
print(babelkowy_tab)
czas_stop = time.time()
print("czas trwania:", czas_stop - czas_start)

print('przez wymiane')
czas_start = time.time()
wymiana(wymiana_tab)
czas_stop = time.time()
print("czas trwania:", czas_stop - czas_start)
print(wymiana_tab)

print('quicksort')
czas_start = time.time()
quicksort(quicksort_tab)
czas_stop = time.time()
print("czas trwania:", czas_stop - czas_start)
print(quicksort_tab)

