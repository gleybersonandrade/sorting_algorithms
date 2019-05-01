"""Sorting Algorithms main."""

# System imports
import argparse

# Local imports
from config import (ALGORITHM_DESCRIPTION, MAIN_DESCRIPTION, ORDER_DESCRIPTION,
                    NUMBER_DESCRIPTION, SIZE_DESCRIPTION)
from utils import (create_structure, generate_in_files, generate_log_file,
                   generate_out_files, get_data, sorting_algorithm)


def main():
    """Responsible for main control."""
    parser = argparse.ArgumentParser(description=MAIN_DESCRIPTION)
    parser.add_argument('-a', '--algorithm', help=ALGORITHM_DESCRIPTION)
    parser.add_argument('-n', '--number', type=int, help=NUMBER_DESCRIPTION)
    parser.add_argument('-o', '--order', help=ORDER_DESCRIPTION)
    parser.add_argument('-s', '--size', help=SIZE_DESCRIPTION)
    args = parser.parse_args()
    try:
        if not (args.algorithm and args.number and args.order and args.size):
            raise ValueError
        create_structure()
        try:
            data = get_data(args.number, args.order, args.size)
        except IOError:
            data = generate_in_files(args.number, args.order, args.size)
        finally:
            alg, out, time = sorting_algorithm(data, args.algorithm)
            # generate_out_files(out, args.number)
            generate_log_file(args.algorithm, args.number, args.order,
                              args.size, alg.compares, alg.moves, time)
    except (TypeError, UnboundLocalError, ValueError) as e:
        parser.print_help()


if __name__ == "__main__":
    main()
