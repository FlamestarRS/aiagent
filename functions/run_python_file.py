import os
import subprocess

def run_python_file(working_directory, file_path):

    if file_path.endswith(".py") == False:
        return (f'Error: "{file_path}" is not a Python file.')

    working_dir_abs = os.path.abspath(working_directory)
    file_abs = os.path.abspath(os.path.join(working_directory, file_path))
    inside_working_dir = os.path.commonpath([working_dir_abs, file_abs]) == working_dir_abs

    if inside_working_dir == False:
        return (f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')

    if os.path.exists(file_abs) == False:
        return (f'Error: File "{file_path}" not found.')
    
    output = ""

    try:
        result = subprocess.run(["python3", file_abs], capture_output=True, text=True, timeout=30, cwd=working_dir_abs)
        output += f'STDOUT: {result.stdout}\n' if result.stdout else 'No output produced\n'
        output += f'STDERR: {result.stderr}\n'
        output += f'Process exited with code {result.returncode}\n'
    except Exception as e:
        return (f'Error: executing Python file: {e}')

    return output
