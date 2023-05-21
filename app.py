from flask import Flask, render_template, request
from Summarizer.summarizer import get_summary_from_text_file

app = Flask(__name__)


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def handle_login():
    username = request.form['username']
    password = request.form['password']
    # Add your login logic here
    # For example, you can check the credentials against a database or perform any other authentication process
    if username == 'admin' and password == 'password':
        return 'Login successful!'
    else:
        return 'Login failed!'


if __name__ == '__main__':
    app.run()


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        rawtext = request.form.get('rawtext', False)
        summary = get_summary_from_text_file(rawtext)
    return render_template('summary.html', sum_text=summary, org_txt=rawtext)


if __name__ == "__main__":
    app.run(debug=True)
