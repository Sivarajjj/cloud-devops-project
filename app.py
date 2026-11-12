
from flask import Flask, jsonify
from datetime import datetime
import platform
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "application": "Cloud DevOps Demo",
        "status": "Running",
        "server": socket.gethostname(),
        "operating_system": platform.system(),
        "timestamp": datetime.now().isoformat()
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "Healthy"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
