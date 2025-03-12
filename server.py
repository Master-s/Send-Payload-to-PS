import os  # Import os library to delete file after sending
from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app, resources={r"/send": {"origins": "*"}})

@app.route("/send", methods=["POST"])
def send_file():
    try:
        ip = request.form.get("ip")
        file = request.files.get("file")

        if not ip or not file:
            return jsonify({"status": "error", "message": "❌ Please enter IP And download the file"}), 400

        # Save file temporarily
        file_path = "ftp.bin"
        file.save(file_path)

        # Run socat command to send file to PS4
        command = f"socat -t 99999999 - TCP:{ip}:9090 < {file_path}"
        process = subprocess.run(command, shell=True, capture_output=True, text=True)

        # تحقق مما إذا كان الأمر نجح
        if process.returncode != 0:
            return jsonify({"status": "error", "message": f"❌ Failed to send file to PS4: {process.stderr}"}), 500

        # 🔴 Delete the file after sending to avoid locking it 🔴
        os.remove(file_path)

        return jsonify({"status": "success", "message": "✅ File sent to PS4 and deleted successfully!"}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": f"❌ unexpected error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
