from flask import Flask, render_template, request
from Summarizer.summarizer import get_summary_from_text_file

app = Flask(__name__)


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
