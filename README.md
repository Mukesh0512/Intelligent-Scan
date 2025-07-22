# Intelligent Scan

# 🤖 Intelligent Scan – AI Powered Attendance System

**Powered by Face Recognition. Built with Flask.**

Intelligent Scan is a modern, AI-based attendance system that uses facial recognition to mark and manage attendance — completely touchless, fast, and secure.

---

## 🚀 Features

- ✅ Real-time face detection and recognition
- 📸 Face data capture module
- 🧠 Model training with automatic data management
- 📅 Daily attendance reports generated as CSV
- 📊 Dashboard with visual report view
- 🌐 Web-based interface (accessible from any device)
- 🛡️ Secure, unique filename + timestamp system

---

## 🛠️ Tech Stack

- **Frontend:** HTML5, CSS3, JavaScript
- **Backend:** Python (Flask)
- **AI/ML:** OpenCV, dlib, face_recognition, NumPy
- **Database:** CSV-based report logs (for MVP)
- **Deployment:** Render / Vercel (optional)

---

## 📁 Folder Structure

📦 IntelligentScan
┣ 📂 app/
┃ ┣ 📄 attendance.py
┃ ┣ 📄 capture.py
┃ ┣ 📄 trainer.py
┃ ┣ 📄 recognizer.py
┃ ┣ 📄 utils.py
┃ ┗ 📄 gui.py (optional)
┣ 📂 data/
┃ ┣ 📂 face_data/
┃ ┣ 📂 reports/
┃ ┗ 📂 trained_model/
┣ 📂 static/
┃ ┣ 📂 css/
┃ ┃ ┗ 📄 style.css
┃ ┗ 📂 js/
┃ ┃ ┗ 📄 script.js
┣ 📂 templates/
┃ ┣ 📄 index.html
┃ ┣ 📄 dashboard.html
┃ ┗ 📄 report.html
┣ 📄 main.py
┣ 📄 requirements.txt
┣ 📄 README.md
┗ 📄 .gitignore



---

## ⚙️ How to Run Locally

```bash
git clone https://github.com/YourUsername/IntelligentScan.git
cd IntelligentScan
pip install -r requirements.txt
python main.py



Then open http://localhost:5000 in your browser.

🌐 Live Demo
👉 https://intelligent-scan.onrender.com (if deployed)

📧 Contact
Made with ❤️ by Mukesh Soni
📬 Email: mukeshkumarsoni990@gmail.com
💼 Portfolio: https://portfolio-website-inky-eight-27.vercel.app/