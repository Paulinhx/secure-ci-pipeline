from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Secure CI/CD Example"

if __name__ == "__main__":
    app.run(debug=True)
# This is a simple Flask application that serves as a placeholder for the CI/CD pipeline.