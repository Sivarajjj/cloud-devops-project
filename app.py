
from flask import Flask, Response, g, jsonify, render_template, request
from datetime import datetime
import platform
import socket
import time

from prometheus_client import CONTENT_TYPE_LATEST, Counter, Histogram, generate_latest

app = Flask(__name__)

HTTP_REQUESTS = Counter(
    "http_requests_total",
    "Total HTTP requests handled by the application.",
    ["method", "endpoint", "status"],
)
HTTP_REQUEST_DURATION = Histogram(
    "http_request_duration_seconds",
    "HTTP request duration in seconds.",
    ["method", "endpoint"],
)


@app.before_request
def start_request_timer():
    g.request_start_time = time.perf_counter()


@app.after_request
def record_request_metrics(response):
    endpoint = request.endpoint or "unknown"
    if endpoint != "metrics":
        HTTP_REQUESTS.labels(
            request.method,
            endpoint,
            str(response.status_code),
        ).inc()
        HTTP_REQUEST_DURATION.labels(
            request.method,
            endpoint,
        ).observe(time.perf_counter() - g.request_start_time)
    return response


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


@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
