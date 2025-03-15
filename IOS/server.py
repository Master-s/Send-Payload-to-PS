from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
import subprocess
import threading

app = Flask(__name__)
CORS(app)  # Enable CORS for all requests

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send_payload():
    file = request.files.get("file")
    ip = request.form.get("ip")
    port = request.form.get("port")

    if not file or not ip or not port:
        return jsonify({"message": "❌ Please provide the required data!"}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Execute the command in a separate thread to avoid response delay
    def send_file():
        try:
            subprocess.Popen(["socat", "-t", "99999999", "-", f"TCP:{ip}:{port}"], stdin=open(file_path, "rb"))
        except Exception as e:
            print(f"❌ Error sending the file: {e}")

    threading.Thread(target=send_file, daemon=True).start()

    return jsonify({"message": "✅ File sent successfully!"})  # Send the response immediately

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
