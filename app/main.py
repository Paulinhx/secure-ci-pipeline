from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # 🔥 This line is insecure on purpose for testing Semgrep
    eval("print('This is a Semgrep test finding')")  # Semgrep should flag this
    return "Secure CI/CD Example"

if __name__ == "__main__":
    app.run(debug=True)

