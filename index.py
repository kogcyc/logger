from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'home page route'

@app.route('/logger', methods=['POST'])
def logger():
    data = request.get_json()
    print("📥 Log received:", data)  # This will show in Vercel's function logs

    return jsonify({
        "status": "success",
        "message": "Log received",
        "received": data
    }), 200
