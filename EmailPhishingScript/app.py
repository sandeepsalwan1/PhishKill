import os
import json
import sqlite3
from datetime import datetime
from flask import Flask, request, render_template, jsonify
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

def resolve_db_path() -> str:
    base_dir = os.path.dirname(__file__)
    try:
        if os.access(base_dir, os.W_OK):
            return os.path.join(base_dir, 'phishkill.db')
    except Exception:
        pass
    tmp_dir = os.environ.get('TMPDIR') or '/tmp'
    return os.path.join(tmp_dir, 'phishkill.db')


DB_PATH = resolve_db_path()


def get_db_connection():
    connection = sqlite3.connect(DB_PATH, check_same_thread=False)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_db_connection()
    try:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS analyses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email_text TEXT NOT NULL,
                risk INTEGER NOT NULL,
                indicators TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT (datetime('now'))
            );
            """
        )
        connection.commit()
    finally:
        connection.close()


app = Flask(__name__)
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/healthz', methods=['GET'])
def healthz():
    return jsonify({"status": "ok"})


@app.route('/api/classify', methods=['POST'])
def api_classify():
    data = request.get_json(silent=True) or {}
    mail = data.get('text', '').strip()
    if not mail:
        return jsonify({"error": "Missing 'text' in JSON body"}), 400

    prompt = (
        "You are a cybersecurity assistant that detects phishing emails. "
        "Given an email, return a strict JSON object with two fields: "
        "risk (integer 0-100) and indicators (array of strings). "
        "Do not include any extra commentary.\n\n"
        f"EMAIL:\n{mail}\n\n"
        "JSON ONLY RESPONSE EXAMPLE: {\"risk\": 72, \"indicators\": [\"urgent language\", \"suspicious link\"]}"
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You're an assistant that helps detecting phishing mails."},
            {"role": "user", "content": prompt},
        ]
    )

    content = response.choices[0].message.content

    # Best-effort JSON extraction if model returns extra text
    parsed = None
    try:
        parsed = json.loads(content)
    except Exception:
        try:
            start = content.find('{')
            end = content.rfind('}') + 1
            if start != -1 and end != -1:
                parsed = json.loads(content[start:end])
        except Exception:
            parsed = None

    if not isinstance(parsed, dict) or 'risk' not in parsed or 'indicators' not in parsed:
        return jsonify({"error": "Model returned unexpected format", "raw": content}), 502

    try:
        risk_value = int(parsed.get('risk'))
    except Exception:
        risk_value = 0

    indicators_value = parsed.get('indicators')
    if not isinstance(indicators_value, list):
        indicators_value = [str(indicators_value)] if indicators_value is not None else []

    # Persist to DB
    connection = get_db_connection()
    try:
        cursor = connection.execute(
            "INSERT INTO analyses (email_text, risk, indicators) VALUES (?, ?, ?)",
            (mail, max(0, min(100, risk_value)), json.dumps(indicators_value))
        )
        connection.commit()
        analysis_id = cursor.lastrowid
        row = connection.execute(
            "SELECT id, email_text, risk, indicators, created_at FROM analyses WHERE id = ?",
            (analysis_id,)
        ).fetchone()
    finally:
        connection.close()

    return jsonify({
        "id": row[0],
        "risk": row[2],
        "indicators": json.loads(row[3]),
        "created_at": row[4]
    })


@app.route('/api/history', methods=['GET'])
def api_history():
    limit_param = request.args.get('limit', default='20')
    try:
        limit = max(1, min(100, int(limit_param)))
    except Exception:
        limit = 20

    connection = get_db_connection()
    try:
        rows = connection.execute(
            "SELECT id, email_text, risk, indicators, created_at FROM analyses ORDER BY id DESC LIMIT ?",
            (limit,)
        ).fetchall()
    finally:
        connection.close()

    items = []
    for row in rows:
        items.append({
            "id": row[0],
            "email_text": row[1],
            "risk": row[2],
            "indicators": json.loads(row[3]),
            "created_at": row[4]
        })
    return jsonify({"items": items})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=True)
