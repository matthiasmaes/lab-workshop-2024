#flask app to display pdf on the browser
from flask import Flask, send_from_directory, redirect
import os

app = Flask(__name__)

@app.route("/")
def home_redirect():
    return redirect('/invoice/2022-003')

@app.route("/invoice/<invoice_id>")
def download(invoice_id):
    return send_from_directory(os.path.abspath(os.getcwd()) + '/static/', invoice_id + '.pdf')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)