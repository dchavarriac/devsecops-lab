import sqlite3
from flask import Flask, request

app = Flask(__name__)

API_KEY = "FAKE_API_KEY_123456"  # Secret hardcodeado

@app.route("/user")
def get_user():
    username = request.args.get("username")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE name = '{username}'"
    cursor.execute(query)
    return str(cursor.fetchall())

@app.route("/file")
def read_file():
    filename = request.args.get("file")
    with open(filename, "r") as f:
        return f.read()
