"""Sorting Algorithms models."""

# System imports
import sys


class Data():
    """Class to manage Data Model."""

    def __init__(self, key, values=None):
        """Create a new data.

        Parameters:
            key (integer): key of a new data.
            values (array): values of a new data.

        """
        self.key = key
        self.values = values

class Algorithm():
    """Class to manage Algorithm Model."""

    def __init__(self):
        self.compares = 0
        self.moves = 0

class Heapsort(Algorithm):
    """Class to manage Heapsort Model."""

    def run(self, data):
        """Execute heapsort algorithm."""
        def heapify(data, n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2
            self.compares += 1
            if l < n and data[i].key < data[l].key:                
                largest = l
            self.compares += 1
            if r < n and data[largest].key < data[r].key:                
                largest = r
            if largest != i:
                self.moves += 2
                data[i], data[largest] = data[largest], data[i]                
                heapify(data, n, largest)

        def hs_main(data):
            n = len(data)
            for i in range(n, -1, -1):
                heapify(data, n, i)
            for i in range(n-1, 0, -1):
                self.moves += 2
                data[i], data[0] = data[0], data[i]
                heapify(data, i, 0)
            return data

        return hs_main(data)

class Insertionsort(Algorithm):
    """Class to manage Insertionsort Model."""

    def run(self, data):
        """Execute insertionsort algorithm."""
        for i in range(1, len(data)):
            aux = data[i]
            j = i - 1
            while j >= 0 and aux.key < data[j].key:
                self.compares += 1
                self.moves += 1
                data[j+1] = data[j]
                j -= 1
            self.compares += 1
            if i != j+1:
                self.moves += 1
            data[j+1] = aux
        return data

class Quicksort(Algorithm):
    """Class to manage Quicksort Model."""

    def run(self, data):
        """Execute quicksort algorithm."""
        def partition(data, low, high):
            i = (low-1)
            pivot = data[int((low + high) / 2)]
            for j in range(low, high):
                self.compares += 1
                if data[j].key <= pivot.key:
                    i = i+1
                    self.moves += 2
                    data[i], data[j] = data[j], data[i]
            self.moves += 2
            data[i+1], data[high] = data[high], data[i+1]
            return i+1

        def qs_main(data, low, high):
            if low < high:
                pi = partition(data, low, high)
                qs_main(data, low, pi-1)
                qs_main(data, pi+1, high)
            return data

        sys.setrecursionlimit(100000)
        return qs_main(data, 0, len(data)-1)

class Mergesort(Algorithm):
    """Class to manage Mergesort Model."""

    def run(self, data):
        """Execute mergesort algorithm."""
        if len(data) > 1:
            mid = len(data)//2
            lefthalf = data[:mid]
            righthalf = data[mid:]
            self.run(lefthalf)
            self.run(righthalf)
            i = 0
            j = 0
            k = 0
            while i < len(lefthalf) and j < len(righthalf):
                self.compares += 1
                if lefthalf[i].key < righthalf[j].key:
                    self.moves += 1
                    data[k] = lefthalf[i]
                    i = i+1
                else:
                    self.moves += 1
                    data[k] = righthalf[j]
                    j = j+1
                k = k+1
            while i < len(lefthalf):
                self.moves += 1
                data[k] = lefthalf[i]
                i = i+1
                k = k+1
            while j < len(righthalf):
                self.moves += 1
                data[k] = righthalf[j]
                j = j+1
                k = k+1
        return data

class Radixsort(Algorithm):
    """Class to manage Radixsort Model."""

    def run(self, data):
        """Execute radixsort algorithm."""
        RADIX_DECIMAL = 10
        maxLength = False
        tmp, placement = -1, 1
        while not maxLength:
            maxLength = True
            buckets = [ list() for _ in range(RADIX_DECIMAL) ]
            for e in data:
                tmp = e.key // placement
                bucketPos = tmp % RADIX_DECIMAL
                self.moves += 1
                buckets[bucketPos].append(e)
                if maxLength and tmp > 0:
                    maxLength = False
            i = 0
            for bucket in buckets:
                for e in bucket:
                    self.moves += 1
                    data[i] = e
                    i += 1
            placement *= RADIX_DECIMAL
        return data

class Selectionsort(Algorithm):
    """Class to manage Selectionsort Model."""

    def run(self, data):
        """Execute selectionsort algorithm."""
        for i in range(len(data)):
            aux = i
            for j in range(i+1, len(data)):
                self.compares += 1
                if data[j].key < data[aux].key:
                    aux = j
            self.moves += 2
            data[i], data[aux] = data[aux], data[i]
        return data

class Shellsort(Algorithm):
    """Class to manage Shellsort Model."""

    def run(self, data):
        """Execute shellsort algorithm."""
        gap = len(data)
        while (gap > 0):
            gap = int(gap / 2)
            for gi in range(gap, len(data)):
                lower_i = gi
                top_el = data[lower_i]
                while (lower_i >= gap and top_el.key < data[lower_i - gap].key):
                    self.compares += 1
                    self.moves += 1
                    lower_i -= gap
                    data[lower_i + gap] = data[lower_i]
                self.compares += 1
                if gi != lower_i:
                    self.moves += 1
                    data[lower_i] = top_el
        return data
