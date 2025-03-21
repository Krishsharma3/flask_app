from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Dockerized Flask App!"

if __name__ == "__main__":
    # Make sure to listen on all interfaces
    app.run(host="0.0.0.0", port=5000, debug=True)

