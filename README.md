# Attendance Helper — Keep Above 75%

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)](https://www.python.org/)  
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-brightgreen?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)  
[![Uvicorn](https://img.shields.io/badge/Uvicorn-0.23.0-orange?logo=python&logoColor=white)](https://www.uvicorn.org/)  
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 📖 Overview
**Attendance Helper** is a web app to help students:
- Calculate **minimum lectures to attend** to reach a target attendance percentage.
- Calculate **maximum lectures you can skip** without falling below the target.
- Simulate **upcoming scheduled lectures**.

---

## 🖥️ Features
- Real-time attendance calculation.
- Upcoming lectures simulation.
- Downloadable results (HTML).
- Responsive UI for desktop and mobile.
- Reset and calculation buttons.

---

## ⚙️ Technologies & Versions
| Technology | Version | Purpose |
|------------|--------|---------|
| Python     | 3.10   | Backend programming language |
| FastAPI    | 0.100.0 | Web framework |
| Uvicorn    | 0.23.0 | ASGI server |
| HTML/CSS/JS | N/A    | Frontend interactive UI |
| Pydantic   | 2.3.0  | Request validation |

---

## 🗂️ Folder Structure
```text
attendance_helper/
│
├─ app/
│  ├─ main.py          # FastAPI entrypoint
│  ├─ schemas.py       # Pydantic models
│  ├─ utils.py         # Calculation logic
│  └─ static/
│      └─ index.html   # Frontend HTML
│
├─ requirements.txt
└─ README.md
```

# Installation

# Clone the repo
```
git clone https://github.com/yourusername/attendance-helper.git
cd attendance-helper
```

# Create virtual environment
```
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

# Install dependencies
```
pip install -r requirements.txt
```
# Run the application
```
uvicorn app.main:app --reload
```


# UI Preview  
```
![UI Preview](https://github.com/pranitdhanade-sys/AttendanceRequired.git)
```

# Contributing
```
1. Fork the repo
2. Create a branch: git checkout -b feature/YourFeature
3. Make your changes
4. Commit: git commit -m "Add feature"
5. Push: git push origin feature/YourFeature
6. Open a Pull Request
```

# Author
Pranit Dhanade