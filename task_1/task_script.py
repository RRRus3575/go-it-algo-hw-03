import argparse
from pathlib import Path
from colorama import Fore, Style, init
import os
import shutil

# Ініціалізація Colorama
init(autoreset=True)

def copy_and_sort_files(source_path, destination_directory='dist'):
    source_path = Path(source_path)
    destination_directory = Path(destination_directory)

    try:
        if not destination_directory.exists() or not destination_directory.is_dir():
            print(Fore.RED + 'Dist does not exist. Creating it.')
            os.makedirs(destination_directory, exist_ok=True)

        for element in source_path.iterdir():
            if element.is_dir():
                print(Fore.BLUE + f'Parse folder: This is folder - {element.name}')
                try:
                    copy_and_sort_files(element, destination_directory)
                except Exception as e:
                    print(Fore.RED + f'Failed to process directory {element}: {e}')
            elif element.is_file():
                print(Fore.MAGENTA + f'Parse folder: This is file - {element.name}')
                extension = element.suffix.lstrip('.').lower()
                if not extension:
                    extension = 'no_extension'

                folder_path = destination_directory / extension
                try:
                    folder_path.mkdir(parents=True, exist_ok=True)
                except Exception as e:
                    print(Fore.RED + f'Failed to create directory {folder_path}: {e}')
                    continue

                try:
                    shutil.copy(element, folder_path / element.name)
                    print(Fore.GREEN + f'Copied {element} to {folder_path / element.name}')
                except Exception as e:
                    print(Fore.RED + f'Failed to copy file {element} to {folder_path}: {e}')
    except Exception as e:
        print(Fore.RED + f'Failed to process path {source_path}: {e}')

if __name__ == '__main__':
    # Парсинг аргументів командного рядка
    parser = argparse.ArgumentParser(description='Copy and sort files from source directory to destination directory.')
    parser.add_argument('source', nargs='?', help='Path to the source directory')
    parser.add_argument('destination', nargs='?', default='dist', help='Path to the destination directory (default: dist)')

    args = parser.parse_args()

    if not args.source:
        args.source = input("Please enter the path to the source directory: ")
    if not args.destination:
        args.destination = input("Please enter the path to the destination directory (default: dist): ") or 'dist'

    source_path = Path(args.source)
    destination_path = Path(args.destination)

    print(f"Source: {source_path}")
    print(f"Destination: {destination_path}")

    try:
        copy_and_sort_files(source_path, destination_path)
    except Exception as e:
        print(Fore.RED + f'Failed to start processing: {e}')
