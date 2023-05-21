from flask import Flask, render_template, request
from Summarizer.summarizer import get_summary_from_text_file

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def handle_login():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return render_template('/index.html')
    else:
        return 'Login failed!'


if __name__ == "__main__":
    app.run()


@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        rawtext = request.form.get('rawtext', False)
        summary = get_summary_from_text_file(rawtext)
    return render_template('summary.html', sum_text=summary, org_txt=rawtext)


if __name__ == "__main__":
    app.run(debug=True)
