from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
  return "<h1>Hello from your local Flask app!</h1>"

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)

