import os
from pathlib import Path
from typing import List


def get_filepaths_from_sub_folders(
        root_directory: str, accepted_file_extensions: List[str]
) -> List[str]:
    """
    return the file paths of all file that have the one of the extension in the
    file_types argument. Will return as a list of string
    Args:
        root_directory: path to the root folder
        accepted_file_extensions: the extensions of the file types that are acceptable to return

    Returns: a list of strings

    """
    list_of_files = []
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for file in filenames:
            extension = Path(file).suffix
            if extension in accepted_file_extensions:
                list_of_files.append(os.path.join(dirpath, file))

    return list_of_files
