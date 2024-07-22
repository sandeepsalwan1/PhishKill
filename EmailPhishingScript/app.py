import os
from flask import Flask, request, render_template
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Initialize the OpenAI client
client = OpenAI(
    api_key=OPENAI_API_KEY,
)

talk = [
    {"role": "system", "content": "You're an assistant that helps detecting phishing mails."}
]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_mail', methods=['POST'])
def check_mail():
    mail = request.form['mail']

    prompt = f"""
    Could the following mail be a phishing mail?
    {mail}

    Answer with a risk (0% - 100%)! This is important! Answer with a risk in percent (0% - 100%)!!!
    What indicators did you use?
    """

    talk.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=talk
    )

    answer = response.choices[0].message.content

    with open('results.txt', 'w') as result_file:
        result_file.write(answer)

    return answer

if __name__ == "__main__":
    app.run(debug=True)
