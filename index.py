from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'home page route'
    
@app.route('/logger')
def logger():
    return 'logger route'
