import os


def get_files_info(working_directory, directory=None):

    if directory == None or directory == ".":
        directory = working_directory  


    working_dir_abs = os.path.abspath(working_directory)
    if directory != working_directory:
        dir_abs = os.path.abspath(os.path.join(working_directory, directory))
    else:
        dir_abs = os.path.abspath(directory)
    inside_working_dir = os.path.commonpath([working_dir_abs, dir_abs]) == working_dir_abs

    if inside_working_dir == False:
        return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    
    if os.path.isdir(dir_abs) == False:
        return (f'Error: "{directory}" is not a directory')

    try:
        dir_list = os.listdir(dir_abs)
    except Exception: 
        return ("Error: Could not list directory contents")

    files = ""

    for item in dir_list:
        try: 
            item_abs = os.path.join(dir_abs, item)
            filesize = os.path.getsize(item_abs)
            is_dir = os.path.isdir(item_abs)
            files += (f'- {item}: file_size={filesize} bytes, is_dir={is_dir}\n')
        except Exception: 
            files += (f"Error: No access to file {item}")
            continue

                
    return files