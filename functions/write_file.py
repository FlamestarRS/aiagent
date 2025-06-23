import os

def write_file(working_directory, file_path, content):

    working_dir_abs = os.path.abspath(working_directory)
    file_abs = os.path.abspath(os.path.join(working_directory, file_path))
    
    if file_abs.startswith(working_dir_abs) == False:
        return (f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
       
    parent_dir = os.path.dirname(file_abs)
    os.makedirs(parent_dir, exist_ok=True)

    try:
        with open(file_abs, "w") as f:
            f.write(content)
        return (f'Successfully wrote to "{file_path}" ({len(content)} characters written)')
    except Exception as e:
        return f'Error writing data to {file_abs}: {e}'
    
