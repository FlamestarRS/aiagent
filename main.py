import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from available_funcs import available_functions



def main():

    verbose = False

    if len(sys.argv) < 2:
        # prompt = input("Please enter a prompt: ")
        sys.exit(1)

    else:
        if sys.argv[-1] == "--verbose":
            prompt = " ".join(sys.argv[1:len(sys.argv)-1])
            verbose = True
        else:
            prompt = " ".join(sys.argv[1:])

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)])
    ]
    
    generate_content(client, messages, verbose, prompt)


def generate_content(client, messages, verbose, prompt):

    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read file contents
    - Execute Python files with optional arguments
    - Write or overwrite files

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions],system_instruction=system_prompt),

        )

    if response.function_calls:
        first_call = response.function_calls[0]
        print(f"Calling function: {first_call.name}({first_call.args})")
    else:
        print("Prompt response:", response.text)


    if verbose == True:
        print("User prompt:", prompt)
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)


if __name__ == "__main__":
    main()