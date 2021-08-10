from flask import Flask, app , render_template

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')
if __name__ == '__main__':
    app.run(debug=True)