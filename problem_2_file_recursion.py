import os

def find_files(suffix, path):
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
    pathsList = []
    
    if os.path.isfile(path):
        if path.endswith(suffix):
            return[path]
        
    if os.path.isdir(path):
        for item in os.listdir(path):
            subPath = os.path.join(path, item)
            pathsList.extend(find_files(suffix, subPath))
        
    return pathsList