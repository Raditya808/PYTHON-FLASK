
from flask import Flask, render_template

app = Flask(__name__, template_folder='template')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('html.html', person=name)

app.run(debug=True, port=5000)

# malas buka vs mending login valorant