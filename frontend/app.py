from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    backend_response = requests.get("http://backend-service:5000/")
    return f"Frontend here! Backend says: {backend_response.text}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
