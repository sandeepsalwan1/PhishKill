# import os
# import sys
# from dotenv import load_dotenv
# from openai import OpenAI

# # To run this code type this in terminal:
# # cd "your-path-file"
# # pip install openai python-dotenv
# # echo "OPENAI_API_KEY=your-actual-api-key-here" > .env
# # python Main.py Mail1.txt

# # Load environment variables from .env file
# load_dotenv()


# # Get API key from environment variable
# OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# # Set the OpenAI API key


# client = OpenAI(
#     # This is the default and can be omitted
#     api_key=OPENAI_API_KEY,
# )

# talk = [
#     {"role": "system", "content": "You're an assistant that helps detecting phishing mails."}
# ]

# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         print("Usage: python script.py <path_to_email_file>")
#         sys.exit(1)

#     with open(sys.argv[1], "r") as f:
#         mail = f.read()

#     prompt = f"""
#     Could the following mail be a phishing mail?
#     {mail}

#     Answer with a risk (0% - 100%)! This is important! Answer with a risk in percent (0% - 100%)!!!
#     What indicators did you use?
#     """

#     talk.append({"role": "user", "content": prompt})

#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=talk
#     )


#     answer = response.choices[0].message.content
#     # print(answer)
#     with open('results.txt', 'w') as result_file:
#         result_file.write(answer)

import os
from dotenv import load_dotenv
import openai

# To run this code type this in terminal:
# cd "your-path-file"
# pip install openai python-dotenv
# echo "OPENAI_API_KEY=your-actual-api-key-here" > .env
# python Main.py

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Set the OpenAI API key
openai.api_key = OPENAI_API_KEY

talk = [
    {"role": "system", "content": "You're an assistant that helps detecting phishing mails."}
]

if __name__ == "__main__":
    mail = input("Please enter the email content to check for phishing: ")

    prompt = f"""
    Could the following mail be a phishing mail?
    {mail}

    Answer with a risk (0% - 100%)! This is important! Answer with a risk in percent (0% - 100%)!!!
    What indicators did you use?
    """

    talk.append({"role": "user", "content": prompt})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=talk
    )

    answer = response.choices[0].message['content']
    with open('results.txt', 'w') as result_file:
        result_file.write(answer)
