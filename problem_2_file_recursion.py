import os


def find_files(suffix=None, path=None):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if suffix == None:
        return "Please input Args: suffix"
    if path == None:
        return "Please input Args: path"
    try:
        if not os.path.isdir(path):
            return "Please input a vaild path"

        result = find_files_recursion(suffix, path)
        if len(result) == 0:
            result = "Not found"
        return result
    except Exception as e:
        return e


def find_files_recursion(suffix, path):
    pathsList = []
    if os.path.isfile(path):
        if path.endswith(suffix):
            return[path]
    if os.path.isdir(path):
        for item in os.listdir(path):
            subPath = os.path.join(path, item)
            pathsList.extend(find_files_recursion(suffix, subPath))
    return pathsList


# should return ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c']
print(find_files('.c', './testdir'))
print(find_files(path='./testdir'))  # return "Please input Args: suffix"
print(find_files(suffix='.c',))     # return "Please input Args: path"
print(find_files('.cpp', "./testdir"))  # return "Not found"
print(find_files('.cpp', "not_path"))  # return "Please input a vaild path"
