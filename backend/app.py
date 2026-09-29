from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Backend Application is Running"


@app.route("/health")
def health():
    return "OK"


@app.route("/api/message")
def message():
    return {
        "message": "Hello from Backend API",
        "status": "success"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
