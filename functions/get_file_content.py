import os


def get_file_content(working_directory, file_path):

    working_dir_abs = os.path.abspath(working_directory)
    file_abs = os.path.abspath(os.path.join(working_directory, file_path))
    inside_working_dir = os.path.commonpath([working_dir_abs, file_abs]) == working_dir_abs

    if inside_working_dir == False:
        return (f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
    
    if os.path.isfile(file_abs) == False:
        return (f'Error: File not found or is not a regular file: "{file_path}"')
    
    MAX_CHARS = 10000
    chars = os.path.getsize(file_abs)

    with open(file_abs, "r") as f:

        if chars > MAX_CHARS:
            return f.read(MAX_CHARS) + (f'[...File "{file_path}" truncated at 10000 characters]')
        return f.read(MAX_CHARS)

