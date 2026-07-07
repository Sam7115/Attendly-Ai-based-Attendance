# 🎓 Attendly – AI-Based Attendance System

Attendly is an AI-powered attendance management system that automates classroom attendance using **Face Recognition**, **Voice Authentication**, and **QR-based Enrollment**. Built with **Streamlit**, **Supabase**, and machine learning, it provides a fast, secure, and user-friendly experience for both teachers and students.

---

## ✨ Features

### 👨‍🏫 Teacher Portal
- Secure teacher authentication
- Create and manage subjects
- Generate QR codes for student enrollment
- Share subject join codes
- Capture classroom images
- Upload multiple attendance images
- Review attendance before confirmation
- AI-powered attendance marking

### 👨‍🎓 Student Portal
- Secure student login
- Face enrollment
- Voice enrollment
- Join subjects using QR code
- View enrolled subjects

### 🤖 AI Features
- Face Recognition for attendance
- Voice Authentication
- KNN-based face classification
- Automatic attendance generation
- Multi-image classroom detection

### ☁ Backend
- Supabase Authentication
- PostgreSQL Database
- Cloud storage integration

---

# 🛠 Tech Stack

## Frontend
- Streamlit

## Backend
- Supabase
- PostgreSQL

## Machine Learning
- Scikit-learn
- Dlib
- Face Recognition
- Librosa
- Resemblyzer

## Image Processing
- Pillow

## QR Code
- Segno

---

# 📂 Project Structure

```
Attendly
│
├── app.py
├── requirements.txt
├── src
│   ├── components
│   ├── database
│   ├── pipelines
│   ├── screens
│   └── ui
│
└── .gitignore
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Sam7115/Attendly-Ai-based-Attendance.git
cd Attendly-Ai-based-Attendance
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create the following file:

```
.streamlit/secrets.toml
```

Add your Supabase credentials:

```toml
SUPABASE_URL="YOUR_SUPABASE_URL"
SUPABASE_KEY="YOUR_SUPABASE_PUBLISHABLE_KEY"
```

---

# ▶ Running the Project

```bash
streamlit run app.py
```

---

# 📸 Workflow

### Teacher

1. Login
2. Create Subject
3. Generate QR Code
4. Students Join
5. Capture/Upload Classroom Images
6. AI Detects Faces
7. Review Attendance
8. Confirm Attendance

### Student

1. Login
2. Complete Face Enrollment
3. Complete Voice Enrollment
4. Scan QR Code
5. Join Subject

---

# 📷 Screenshots

> Add screenshots here.

```
Home Screen

Teacher Dashboard

Student Dashboard

Attendance Result

QR Enrollment

Face Enrollment

Voice Enrollment
```

---

# Future Improvements

- Live webcam attendance
- Attendance analytics dashboard
- Email notifications
- Mobile application
- Anti-spoofing detection
- Multi-class simultaneous attendance
- Attendance reports in PDF/Excel
- Liveness detection

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create your feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add feature"
```

4. Push

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Authors

**Samarth Nalkar**

GitHub: https://github.com/Sam7115

---

## ⭐ If you like this project, don't forget to star the repository!
