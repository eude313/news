from flask import Flask, app , render_template

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')

@app.route("/home")
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)