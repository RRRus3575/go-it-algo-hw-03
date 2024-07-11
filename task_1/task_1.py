import shutil
import os
from colorama import init, Fore, Style

# Инициализация colorama
init(autoreset=True)

def copy_file(src, dst):
    try:
        shutil.copy2(src, dst)
        print(Fore.GREEN + f"File '{src}' successfully copied to '{dst}'")
    except FileNotFoundError:
        print(Fore.RED + f"File '{src}' not found.")
    except PermissionError:
        print(Fore.RED + f"Permission denied when copying file '{src}' to '{dst}'.")
    except Exception as e:
        print(Fore.RED + f"Error copying file '{src}' to '{dst}': {e}")

def copy_files_in_directory(src_dir, dst_dir):
    try:
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        for item in os.listdir(src_dir):
            src_item = os.path.join(src_dir, item)
            dst_item = os.path.join(dst_dir, item)
            if os.path.isfile(src_item):
                copy_file(src_item, dst_item)
            elif os.path.isdir(src_item):
                copy_files_in_directory(src_item, dst_item)
    except Exception as e:
        print(Fore.RED + f"Error copying directory '{src_dir}' to '{dst_dir}': {e}")

def main():
    src_dir = input("Enter the source directory: ")
    dst_dir = input("Enter the destination directory: ")
    
    if os.path.exists(src_dir):
        print(Fore.BLUE + f"Starting to copy files from '{src_dir}' to '{dst_dir}'")
        copy_files_in_directory(src_dir, dst_dir)
        print(Fore.BLUE + f"Finished copying files from '{src_dir}' to '{dst_dir}'")
    else:
        print(Fore.RED + f"Source directory '{src_dir}' does not exist.")

if __name__ == "__main__":
    main()
