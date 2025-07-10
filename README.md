# 📄 SmartHire Pro – AI Resume Ranking System

SmartHire Pro is an AI-powered resume screening tool that allows recruiters to **automatically rank uploaded resumes** against a given job description using intelligent text analysis and machine learning techniques.

---

## 🚀 Features

- 📤 Upload resumes (`.txt`, `.pdf`, `.docx`)
- 🧠 Match against job descriptions using NLP
- 📊 Visual resume ranking with interactive UI
- 🔧 REST API built with FastAPI
- 📥 Export results as CSV

---

## 📁 Project Structure

```
SmartHirePro/
├── backend/
│   ├── api/
│   │   └── main.py            # FastAPI endpoints
│   ├── model/
│   │   ├── resume_ranker.py   # JD-to-resume matching logic
│   │   └── utils.py           # Text preprocessing and helpers
│   └── data/
│       └── uploads/           # Uploaded resume storage
├── frontend/
│   └── streamlit_app.py       # Streamlit-based user interface
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Pratik0P/SmartHirePro.git
cd SmartHirePro
```

### 2. Create and activate virtual environment

```bash
python -m venv .venv
.\.venv\Scripts\activate       # For Windows
# source .venv/bin/activate    # For macOS/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

### Start the FastAPI backend

```bash
uvicorn backend.api.main:app --reload
```

API will run at: `http://127.0.0.1:8000`

### Start the Streamlit frontend

```bash
streamlit run frontend/streamlit_app.py
```

Frontend UI will open at: `http://localhost:8501`

---

## 📬 API Endpoints

- `POST /upload` – Upload a resume file
- `POST /rank` – Match resumes with a job description

---

## 🧪 How to Test

1. Upload `.txt` resumes via the Streamlit app.
2. Paste a job description.
3. Click “🎯 Rank Resumes” to see ranked matches.
4. Export the results as CSV if needed.

---

## 🛠 Built With

- **FastAPI** – For building APIs
- **Streamlit** – For frontend UI
- **scikit-learn** – For vectorization & similarity scoring
- **Requests, Pandas, NumPy** – For data handling

---

## 👤 Author

Pratik Prakash
GitHub: [@Pratik0P](https://github.com/Pratik0P)

---

## 📄 License

This project is licensed under the **MIT License**.

---

> 💡 Tip: Use this project to showcase your API, ML, and fullstack skills when applying to top tech companies!
