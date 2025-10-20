# 📝 Flask Task Manager (Dark Mode CRUD App)

A sleek and intuitive **Task Manager** web app built with **Flask**, **SQLAlchemy**, and **Bootstrap 5 (Dark Mode)**.  
Easily **create, update, and delete tasks** — with secure user authentication and a minimalist dark-themed interface.

---

## 🚀 Features

- 🌓 **Dark Mode UI** — modern and easy on the eyes  
- 🧾 **Full CRUD Support** — Create, Read, Update, Delete tasks  
- 🔒 **User Authentication** — register, login, logout  
- 🕐 **Timestamps** — automatic creation & update tracking  
- 📦 **SQLite** (local) or **PostgreSQL** (for deployment)  
- ⚡ **Responsive Design** — built with Bootstrap 5  
- 🧠 **Clean Architecture** — easy to extend and maintain  

---

## 🧩 Tech Stack

| Component | Technology |
|------------|-------------|
| Backend | Flask (Python) |
| Database | SQLite / PostgreSQL |
| Frontend | HTML, CSS (Bootstrap 5) |
| Auth | Flask-Login |
| Deployment | Render / Railway / Docker |

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/flask-task-manager.git
cd flask-task-manager
```

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate      # On Windows
# OR
source venv/bin/activate   # On macOS/Linux
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Initialize the database

```bash
python
>>> from app import create_app, db
>>> app = create_app()
>>> with app.app_context():
...     db.create_all()
...     print("Database ready!")
```

### 5️⃣ Run the app

```bash
python run.py
```

Visit 👉 **http://127.0.0.1:5000** in your browser.

---

## ⚙️ Project Structure

```
CRUD_app2/
│
├── app/
│   ├── __init__.py         # Flask app factory
│   ├── models.py           # Database models
│   ├── routes.py           # Routes & logic
│   └── templates/          # HTML templates
│
├── static/
│   └── style.css           # Dark mode styling
│
├── run.py                  # App entry point
├── requirements.txt        # Python dependencies
└── Procfile                # For deployment (Render, etc.)
```

---

## 🌐 Deployment on Render (Quick Guide)

1. Push your project to **GitHub**
2. Go to [Render.com](https://render.com)
3. Click **New → Web Service**
4. Connect your repo
5. Set build and start commands:

   ```bash
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn run:app
   ```

6. Deploy — Render gives you a live URL like:
   ```
   https://flask-task-manager.onrender.com
   ```

---

## 📸 Screenshots

| Dashboard | Login |
|------------|-------|
| ![Dashboard Dark](docs/screenshot_dashboard.png) | ![Login Dark](docs/screenshot_login.png) |

> *(Add screenshots in a `/docs` folder to make your README shine!)*

---

## 🧑‍💻 Author

**[Your Name]**  
💼 GitHub: [@AustinKipsigei](https://github.com/yourusername)  
📧 Email: austin.kipsigei@gmail.com

---

## 🪪 License

This project is open-source under the [MIT License](LICENSE).  
Feel free to modify and share — attribution is appreciated.

---

> *Made with ❤️ using Flask & Bootstrap — clean, dark, and efficient.*
