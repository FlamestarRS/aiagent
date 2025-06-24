from google.genai import types


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Returns the contents of a file as text.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to return content from. The file exist and be within the working directory.",
            ),
        },
    ),
)
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Overwrites text to an existing file, or creates a file and necessary directory structure if it does not exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to write content to. If the file does not exist, it is created.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to a given file."
            )
        },
    ),
)
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a given .py file and returns the output, error, and any non-zero exit code.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of the .py file to run. Must be within the working directory.",
            ),
        },
    ),
)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file,
    ]
)