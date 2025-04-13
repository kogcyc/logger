from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import psycopg2
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Expect this to be defined in your Vercel project settings
DATABASE_URL = os.environ.get("NEON_DB_URL")

@app.route('/')
def home():
    return 'home page route'

@app.route('/logger', methods=['POST'])
def logger():
    data = request.get_json()
    url = data.get("url", "")
    timestamp = data.get("timestamp") or datetime.utcnow().isoformat()
    logrec = data.get("logrec", 1)  # default to 1 if not provided

    print("📥 Log received:", data)

    # Insert into Neon PostgreSQL
    try:
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = conn.cursor()
        cur.execute("INSERT INTO logs (url, time, logrec) VALUES (%s, %s, %s)", (url, timestamp, logrec))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({
            "status": "success",
            "message": "Log recorded",
            "received": data
        }), 200

    except Exception as e:
        print("❌ DB Insert Error:", str(e))
        return jsonify({
            "status": "error",
            "message": "Failed to log entry",
            "error": str(e)
        }), 500
