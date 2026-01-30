from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(__file__)
LOG_FILE = os.path.join(BASE_DIR, "logs", "incident_log.txt")


@app.route("/api/incidents", methods=["GET"])
def get_incidents():
    if not os.path.exists(LOG_FILE):
        return jsonify([])

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    incidents = content.strip().split("============================")
    cleaned = [i.strip() for i in incidents if i.strip()]

    return jsonify(cleaned)


if __name__ == "__main__":
    app.run(debug=True)
