from flask import Flask, request, jsonify

app = Flask(__name__)
message = ""
latest_metrics = {}
latest_metrics_zero = {}

@app.route("/message", methods=["GET"])
def get_message():
    return jsonify({"text": message})

@app.route("/message", methods=["POST"])
def set_message():
    global message, latest_metrics, latest_metrics_zero
    data = request.get_json()
    if data:
        if "text" in data:
            message = data["text"]
        if "metrics" in data:
            latest_metrics = data["metrics"]
        if "metrics_zero" in data:
            latest_metrics_zero = data["metrics_zero"]
        return jsonify({"status": "success", "text": message, "metrics": latest_metrics}), 200
    else:
        return jsonify({"error": "Missing JSON payload"}), 400


@app.route("/metrics", methods=["GET"])
def get_metrics():
    return jsonify(latest_metrics)

@app.route("/metrics/zero", methods=["GET"])
def get_metrics_zero():
    return jsonify(latest_metrics_zero)

@app.route("/",methods=["GET"])
def home():
    return jsonify(latest_metrics)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
