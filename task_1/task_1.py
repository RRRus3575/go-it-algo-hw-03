from pathlib import Path
from colorama import Fore, Style, init
import os
import shutil

init(autoreset=True)

parent_folder_path = Path('./task_1/test')

new = Path('./task_1/new')

def copy_and_sort_files(path, destination_directory='dist'):
    new_directory = Path(destination_directory)

    try:
        if not new_directory.exists() or not new_directory.is_dir():
            print(Fore.RED + 'Dist does not exist. Creating it.')
            new_directory = path.parent / 'dist'
            os.makedirs(new_directory, exist_ok=True)

        for element in path.iterdir():
            if element.is_dir():
                print(Fore.BLUE + f'Parse folder: This is folder - {element.name}')
                try:
                    copy_and_sort_files(element, new_directory)
                except Exception as e:
                    print(Fore.RED + f'Failed to process directory {element}: {e}')
            elif element.is_file():
                print(Fore.MAGENTA + f'Parse folder: This is file - {element.name}')
                extension = element.suffix.lstrip('.').lower()
                if not extension:
                    extension = 'no_extension'

                folder_path = new_directory / extension
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
        print(Fore.RED + f'Failed to process path {path}: {e}')


try:
    copy_and_sort_files(parent_folder_path, new)
except Exception as e:
    print(Fore.RED + f'Failed to start processing: {e}')