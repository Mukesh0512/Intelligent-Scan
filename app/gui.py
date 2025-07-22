from flask import Flask, render_template, request, redirect, url_for, flash
import os
from app import capture, trainer, recognizer
import datetime

app = Flask(__name__)
app.secret_key = 'intelligent-scan-secret'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_id = request.form['id']
        name = request.form['name']
        if user_id and name:
            capture.capture_faces(user_id, name)
            flash('Face images captured successfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('ID and Name are required!', 'danger')
    return render_template('register.html')

@app.route('/train')
def train():
    trainer.train_model()
    flash('Model trained successfully!', 'success')
    return redirect(url_for('home'))

@app.route('/recognize')
def recognize():
    recognizer.recognize_faces()
    flash('Recognition complete. Attendance marked.', 'info')
    return redirect(url_for('home'))

@app.route('/report')
def report():
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    path = f"data/reports/attendance_{today}.csv"
    if os.path.exists(path):
        return redirect(f"/{path}")
    else:
        flash("No attendance marked for today.", "warning")
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
