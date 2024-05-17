""""File with all helper functions"""
import os

colours_dictionary = {
    'red': "\033[91m",  # \033 is an ansi escape code and 91m refers to red.
    'base': "\033[0m"  # the base colour is white. Again, \033 is the escape code and 0m stands for default i.e. white
}


# os.curdir -> gives the current directory which would be usually just "."
# os.path.join -> will join two paths together.
# os.listdir -> gives the name of all files present in the argument directory.


def get_files_path(extension='.txt') -> []:
    """"Returns a list of all files of the given extension with full paths."""

    file_path = os.path.join(os.curdir, 'words_directory')  # file_path = ./words_directory

    files_full_path = [os.path.join(file_path, x) for x in os.listdir(file_path) if x.endswith(extension)]

    return files_full_path


def find_word(word_to_find=None):
    """Find the word in the line"""

    all_files = get_files_path()
    for file in all_files:
        with open(file, 'r') as my_file:  # open the file in reading mode.
            lines = my_file.readlines()  # read_lines is a function that helps in reading. it returns a list of all
            # lines in that file.
            for line in lines:
                if word_to_find in line:
                    new_line = line.replace(word_to_find, f"{colours_dictionary['red']}{word_to_find}{colours_dictionary['base']}")
                    print(f"{file}:{new_line}")
