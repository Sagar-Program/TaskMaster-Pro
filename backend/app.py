from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "TaskMaster-Pro API is running!"})

if __name__ == '__main__':
    app.run(port=5001, debug=True)

