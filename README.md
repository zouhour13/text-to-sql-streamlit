**Text-to-SQL Streamlit App**

Convert natural language questions into SQL queries using Groq + Llama 3 and run them instantly on a local SQLite database.

**Text-to-SQL Streamlit App**

Convert natural language questions into SQL queries using Groq + Llama 3 and run them instantly on a local SQLite database.

**Features**

✨ Convert English questions → SQL queries using Llama 3
✨ Execute SQL queries automatically on company.db
✨ Beautiful Streamlit UI with custom CSS
✨ Secure API key loading using .env (not uploaded to GitHub)
✨ Beginner-friendly and easy to deploy

**How It Works**

You type a question like:
"Show all employees in the Finance department"

The app sends your question to Groq LLM (Llama-3.3-70B-Versatile).

The model generates the SQL:

SELECT * FROM EMPLOYEE WHERE DEPARTMENT="Finance";


The SQL runs against company.db, and results are displayed beautifully.

**Installation**
1️⃣ Clone the repository
git clone https://github.com/zouhour13/text-to-sql-streamlit.git
cd text-to-sql-streamlit

2️⃣ Create a virtual environment
python -m venv venv


Activate it:

Windows:

venv\Scripts\activate

🔐 Environment Variables

Create a .env file in the root folder:

GROQ_API_KEY=your_groq_key_here


⚠️ The .env file is ignored in `.gitignore** so your keys remain safe.

Install Requirements
pip install -r requirements.txt

▶️ Run the App
streamlit run app.py

🗃 Database Structure

The app uses company.db with one table:

EMPLOYEE
Column	Type
EMP_ID	INT
NAME	VARCHAR
DEPARTMENT	VARCHAR
POSITION	VARCHAR
SALARY	INT
BONUS	INT

Sample data is automatically inserted using your database creation script.


📁 Project Structure

<p align="center">
  <img src="https://raw.githubusercontent.com/zouhour13/text-to-sql-streamlit/main/screenshot.png" width="600">
</p>

text-to-sql-streamlit/
│── app.py
│── mydata.py (optional)
│── company.db
│── .env              # not in GitHub
│── .gitignore
│── requirements.txt
└── README.md

🎨 UI Preview

The app includes:

gradient background

clean modern buttons

styled result rows

centered title and description

❤️ Made By

Zouhour Bellamine
AI & Data Engineer
Tunis, Tunisia
