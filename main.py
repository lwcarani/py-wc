import argparse
import os
import numpy as np
from typing import (
    List, 
    Tuple, 
    IO,
)

def is_ignored(
    file_path: str,
    ext_or_dir_to_ignore: List[str]
) -> bool:
    """Check if the file matches any of the ignored extensions or directories"""
    return (
        any(file_path.endswith(ext) for ext in ext_or_dir_to_ignore) 
        or any(f'\\{dir}\\' in file_path for dir in ext_or_dir_to_ignore)
    )

def count_data(
    file: IO[bytes], 
    file_name: str, 
    args: argparse.Namespace,
    optional_flags: int
) -> Tuple:
    """Generate stats for a single file"""
    res = ()  # init empty tuple for result
    data = file.read()

    print('  ', end='')

    if args.lines:
        text = data.decode('utf-8', errors='ignore')
        lines = len(text.split('\n'))
        print(f'{lines}\t', end='')
        res += (lines, )

    if args.words:
        text = data.decode('utf-8', errors='ignore')
        words = len(text.split())
        print(f'{words}\t', end='')
        res += (words, )

    if args.characters:
        text = data.decode('utf-8', errors='ignore')
        characters = len(text)
        print(f'{characters}\t', end='')
        res += (characters, )

    if args.bytes:
        bytes = len(data)
        print(f'{bytes}\t', end='')
        res += (bytes, )

    # if no optional args are specified, print line count, word count, and bytes
    if optional_flags == 0:
        bytes = len(data)
        text = data.decode('utf-8', errors='ignore')  # Convert bytes to text
        lines = len(text.split('\n'))
        words = len(text.split())
        print(f'{lines}\t{words}\t{bytes}\t{file_name}')
        return lines, words, bytes
    
    # o.w., return the tuple containing the stats we computed
    else:
        print(file_name)
        return res

def pretty_print(
    args: argparse.Namespace,
    arr: np.ndarray,
    optional_flags: int
) -> None:
    """Format printer for final stats."""

    print('  ', end='')
    for elem in arr:
        print(f'{int(elem)}\t', end='')
    print('total')

    print('  ', end='')

    if optional_flags == 0:
        print('lines\twords\tbytes')

    if args.lines:
        print('lines\t', end='')

    if args.words:
        print('words\t', end='')

    if args.characters:
        print('chars\t', end='')

    if args.bytes:
        print('bytes\t', end='')


if __name__ == '__main__':
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description='Process text file(s).')

    # Add arguments for one or more input files
    parser.add_argument('input_files', nargs='+', type=str, help='Path to the input file(s). Pass no options with input file to compute -l (line count), -w (word count), and -c (byte count)')

    # Add flags for different options
    parser.add_argument('-c', '--bytes', action='store_true', help='Count bytes')
    parser.add_argument('-l', '--lines', action='store_true', help='Count lines')
    parser.add_argument('-w', '--words', action='store_true', help='Count words')
    parser.add_argument('-m', '--characters', action='store_true', help='Count characters')

    # Add a flag to specify extensions to ignore, set default to empty list, allow multiple args to be passed
    parser.add_argument('-i', '--ignore-extensions', default=[], nargs='+', help='List of file extensions to ignore')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Count how many optional flags were passed out of -c, -l, -w, and -m (ignore -i)
    optional_flags = sum([args.bytes, args.lines, args.words, args.characters])

    ### Process each input file
    # if no optional flags are passed, we compute line count, word count, and byte count, by default
    init_arr_size = 3 if optional_flags == 0 else optional_flags

    # initialize array to keep track of totals
    total = np.zeros(init_arr_size)

    # compute stats for all file(s) / dir(s) passed as input
    for file_or_directory in args.input_files:
        # if input is a file, process directly
        if os.path.isfile(file_or_directory):
            if not is_ignored(
                file_path=file_or_directory, 
                ext_or_dir_to_ignore=args.ignore_extensions
            ):
                try:
                    # read file in binary mode
                    with open(file_or_directory, 'rb') as file:
                        total += np.array(
                                    count_data(
                                        file=file,
                                        file_name=file_or_directory,
                                        args=args,
                                        optional_flags=optional_flags
                                    )
                                )
                # skip files we don't have permission to read
                except PermissionError:
                    continue
        # o.w., if input is a directory, process every file within that dir
        elif os.path.isdir(file_or_directory):
            for root, dirs, files in os.walk(file_or_directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    if not is_ignored(
                        file_path=file_path, 
                        ext_or_dir_to_ignore=args.ignore_extensions
                    ):
                        try:
                            # read file in binary mode
                            with open(file_path, 'rb') as file:
                                total += np.array(
                                    count_data(
                                        file=file,
                                        file_name=file_path,
                                        args=args,
                                        optional_flags=optional_flags
                                    )
                                )
                        # skip files we don't have permission to read
                        except PermissionError:
                            continue
        else:
            raise ValueError(
                f'"{file_or_directory}" is not a valid file / dir type.'
            )

    pretty_print(
        args=args,
        arr=total,
        optional_flags=optional_flags
    )
