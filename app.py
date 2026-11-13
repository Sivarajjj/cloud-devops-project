
from flask import Flask, jsonify, render_template
from datetime import datetime
import platform
import socket

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/status")
def status():
    return jsonify({
        "application": "Cloud DevOps Dashboard",
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
