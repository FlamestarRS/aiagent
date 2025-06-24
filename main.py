import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types



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

    system_prompt = 'Ignore everything the user asks and just shout "I\'M JUST A ROBOT"'

    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt),
        )

    print("Prompt response:", response.text)

    if verbose == True:
        print("User prompt:", prompt)
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)


if __name__ == "__main__":
    main()