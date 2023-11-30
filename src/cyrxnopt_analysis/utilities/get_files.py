import os
import re
from typing import List


def get_files(
    directory: str, pattern: str = r"*", recursive: bool = False
) -> List[str]:
    """Helper function to get all files in a directory that match a given
    pattern.

    :param directory: Directory to search for files in.
    :type directory: str
    :param pattern: Regex pattern that result files must match.
                    Defaults to r"*" for all files.
    :type pattern: str, optional
    :param recursive: Whether to find files recursively in subdirectories
                      (True) or not (False). Defaults to "False".
    :type recursive: bool, optional
    :return: List of matching files joined with the given directory path.
    :rtype: List[str]
    """

    if recursive:
        files = _get_files_recursively(directory, pattern)
    else:
        files = _get_files_top_dir(directory, pattern)

    return files


def _get_files_top_dir(directory: str, pattern: str = r"*") -> List[str]:
    """Gets all files that match the given pattern. This function does not
    recurse into subdirectories.

    :param directory: Directory to search for files in.
    :type directory: str
    :param pattern: Regex pattern files must match, defaults to r"*"
    :type pattern: str, optional
    :return: List of matching files joined with the given directory path.
    :rtype: List[str]
    """

    files = [
        os.path.join(directory, file)
        for file in os.listdir(directory)
        if (
            os.path.isfile(os.path.join(directory, file))
            and re.match(pattern, file)
        )
    ]

    return files


def _get_files_recursively(directory: str, pattern: str = r"*") -> List[str]:
    """Gets all files that match the given pattern. This function also searches
    subdirectories.

    :param directory: Directory to search for files in.
    :type directory: str
    :param pattern: Regex pattern files must match, defaults to r"*"
    :type pattern: str, optional
    :return: List of matching files joined with the given directory path.
    :rtype: List[str]
    """

    files = [
        os.path.join(dirpath, file)
        for (dirpath, dirnames, filenames) in os.walk(directory)
        for file in filenames
        if re.match(pattern, file)
    ]

    return files
