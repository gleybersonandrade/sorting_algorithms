"""Sorting Algorithms utils."""

# System imports
import os
import random
import string
import timeit

# Local imports
from config import (FILES_REPO, IN_REPO, LOGS_REPO, OUT_REPO, SEPARATOR,
                    STR_NUMBER, STR_SIZE)
from models import (Data, Heapsort, Insertionsort, Mergesort, Quicksort,
                    Radixsort, Selectionsort, Shellsort)


def create_folder(path):
    """Create a folder"""
    if not os.path.exists(path):
        os.mkdir(path)


def create_structure():
    """Generate folders structure."""
    create_folder(FILES_REPO)
    create_folder(IN_REPO)
    create_folder(OUT_REPO)
    create_folder(LOGS_REPO)


def generate_string(number, chars=string.ascii_lowercase+string.digits):
    """Generate a string."""
    return ''.join(random.choice(chars) for _ in range(number))


def generate_in_files(number, order, size):
    """Generate input files."""

    def get_crescent_data():
        return [index for index in range(0, number)]
    
    def get_decreasing_data():
        return [index for index in range(number-1, -1, -1)]

    def get_random_data():
        return random.sample(range(0, number), number)

    switcher = {
        "decreasing": lambda: get_decreasing_data(),
        "crescent": lambda: get_crescent_data(),
        "random": lambda: get_random_data()
    }

    data = []
    path = IN_REPO + str(number)
    create_folder(path)
    keys = switcher.get(order)()
    for key in keys:
        values = [generate_string(STR_SIZE) for _ in range(0, STR_NUMBER)]
        data.append({key: values})
    write_file(data, path, order)
    return get_data(number, order, size)


def generate_out_files(data, number):
    """Generate output files."""
    out_data = [{data[i].key: data[i].values} for i in range(0, number)]
    write_file(out_data, OUT_REPO, str(number))


def generate_log_file(algorithm, number, order, size, compares, moves, time):
    """Generate log file."""
    with open(LOGS_REPO + algorithm + '.log', 'a') as out_file:
        out_file.writelines(str(number) + SEPARATOR +
                            order.upper() + SEPARATOR +
                            size.upper() + SEPARATOR +
                            "COMPARES: " + str(compares) + SEPARATOR +
                            "MOVES: " + str(moves) + SEPARATOR +
                            "TIME: " + str(time) + os.linesep)
        out_file.close()


def get_data(number, order, size):
    """Get input data."""

    def get_large_data():
        data = []
        for d in file:
            spl = d.split(SEPARATOR)
            data.append(Data(int(spl[0]), spl[1]))
        return data
    
    def get_small_data():
        data = []
        for d in file:
            spl = d.split(SEPARATOR)
            data.append(Data(int(spl[0])))
        return data

    switcher = {
        "large": lambda: get_large_data(),
        "small": lambda: get_small_data()
    }

    try:
        path = IN_REPO + str(number)
        file = read_file(path, order)
    except IOError:
        raise
    return switcher.get(size)()


def read_file(repo, name):
    """Read JSON files."""
    with open(repo + '/' + name + '.txt') as file:
        data = [d.rstrip() for d in file.readlines()]
        file.close()
    return data


def write_file(data, repo, name):
    """Write JSON files."""
    with open(repo + '/'+ name + '.txt', 'w') as file:
        for d in data:
            key = list(d.keys())[0]
            value = list(d.values())[0]
            file.writelines(str(key) + SEPARATOR + str(value) + os.linesep)
        file.close()


def sorting_algorithm(data, name):
    """Execute sorting algotithms."""
    switcher = {
        "heapsort": lambda: Heapsort(),
        "insertionsort": lambda: Insertionsort(),
        "quicksort": lambda: Quicksort(),
        "mergesort": lambda: Mergesort(),
        "radixsort": lambda: Radixsort(),
        "selectionsort": lambda: Selectionsort(),
        "shellsort": lambda: Shellsort()
    }
    begin_time = timeit.default_timer()
    algorithm = switcher.get(name)()
    out_data = algorithm.run(data)
    end_time = timeit.default_timer()
    return algorithm, out_data, end_time - begin_time
