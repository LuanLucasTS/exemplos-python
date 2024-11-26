# pip3 install flask
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fbd7ea2f0f4ea484525828a5b0116aa6acd2adef8d9eec8125c51b1a112a85b7'

def get_db_connection():
    conn = sqlite3.connect('banco.db', check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

conn = get_db_connection()
@app.route('/')
def home():
    exemplo = conn.execute("SELECT * FROM exemplo order by exemplo").fetchall()
    return render_template('index.html', exemplo=exemplo)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
