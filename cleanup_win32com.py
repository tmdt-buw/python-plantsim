"""
Copyright (c) 2021 Tilo van Ekeris / TMDT, University of Wuppertal
Distributed under the MIT license, see the accompanying
file LICENSE or https://opensource.org/licenses/MIT
"""

"""
Sometimes the win32com has a hiccup that results in something like this

AttributeError: module 'win32com.gen_py.AAAAAAAA-AAAA-AAAA-AAAA-AAAAAAAAAAAAxAxAxA' has no attribute 'CLSIDToClassMap'

when calling the EnsureDispatch() method.

This script cleans the win32com cache up. Afterwards, the other scripts should work as usual

Solution based on:
https://stackoverflow.com/questions/52889704/python-win32com-excel-com-model-started-generating-errors
"""

import win32com
import shutil


def main():

    gen_path = win32com.__gen_path__

    print(f'Removing the following directory with all of its contents:')
    print(f'{gen_path}')
    print(f'Press enter to continue or Ctrl+C to cancel...')

    try:
        input()
    except KeyboardInterrupt:
        exit(99)

    shutil.rmtree(gen_path)


if __name__ == '__main__':
    main()
