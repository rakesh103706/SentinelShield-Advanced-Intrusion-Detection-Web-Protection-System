from flask import Flask, request, render_template
from detector import detect_attack
from rate_limiter import is_rate_limited
from logger import init_db, log_event
import sqlite3

app = Flask(__name__)
init_db()

@app.route("/")
def home():
    return "SentinelShield Web Protection System Running"

@app.route("/test", methods=["GET", "POST"])
def test():
    data = request.args.get("input", "") + request.get_data(as_text=True)
    ip = request.remote_addr

    if is_rate_limited(ip):
        log_event(ip, "Rate Limit Exceeded")
        return "Blocked: Too many requests", 403

    attack = detect_attack(data)
    if attack:
        log_event(ip, attack)
        return f"Blocked: {attack} detected", 403

    return "Request Allowed"

@app.route("/dashboard")
def dashboard():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT ip, attack, timestamp FROM logs ORDER BY id DESC")
    logs = c.fetchall()
    conn.close()
    return render_template("dashboard.html", logs=logs)

if __name__ == "__main__":
    app.run(debug=True)