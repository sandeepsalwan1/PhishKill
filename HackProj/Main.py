import openai
import sys

OPENAI_API_KEY = "sk-proj-BSL7Vfw0wVAwzqiccepcT3BlbkFJdoxgKLrs0d0H1mnTMb1"

# Set the OpenAI API key
openai.api_key = OPENAI_API_KEY

talk = [
    {"role": "system", "content": "You're an assistant that helps detecting phishing mails."}
]

if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        mail = f.read()

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

    answer = response.choices[0].message.content
    print(answer)

