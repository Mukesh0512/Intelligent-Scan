from flask import Flask, render_template, request, redirect, url_for, flash
from app.recognizer import recognize_faces
from app.capture import capture_faces
from app.trainer import train_model
from app.attendance import mark_attendance, get_today_report
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for flashing messages

# --------------------
# Route: Home Page
# --------------------
@app.route('/')
def home():
    return render_template('index.html')


# --------------------
# Route: Dashboard Page
# --------------------
@app.route('/dashboard')
def dashboard():
    report_data = get_today_report()
    return render_template('dashboard.html', report=report_data)


# --------------------
# Route: Capture Face Data
# --------------------
@app.route('/capture', methods=['POST'])
def capture():
    user_id = request.form['user_id']
    user_name = request.form['user_name']
    result = capture_faces(user_id, user_name)

    if result == "success":
        flash("✅ Face data captured successfully.")
    else:
        flash("❌ Face data capture failed.")
        
    return redirect(url_for('dashboard'))


# --------------------
# Route: Train Model
# --------------------
@app.route('/train', methods=['POST'])
def train():
    result = train_model()
    flash(f"🧠 Training status: {result}")
    return redirect(url_for('dashboard'))


# --------------------
# Route: Recognize Faces & Mark Attendance
# --------------------
@app.route('/recognize', methods=['POST'])
def recognize():
    result = recognize_faces()
    flash(f"📸 Recognition result: {result}")
    return redirect(url_for('dashboard'))


# --------------------
# Route: Manual Attendance
# --------------------
@app.route('/attendance', methods=['POST'])
def manual_attendance():
    user_id = request.form['user_id']
    user_name = request.form['user_name']
    result = mark_attendance(user_id, user_name)
    flash(f"📅 Manual attendance result: {result}")
    return redirect(url_for('dashboard'))


# --------------------
# Run App
# --------------------
if __name__ == '__main__':
    app.run(debug=True)
