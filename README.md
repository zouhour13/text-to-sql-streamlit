# 💬 Text-to-SQL Data Assistant

A Streamlit application that translates natural-language questions into SQL and runs them against a sample employee database. It combines Groq's hosted GPT-OSS 120B model with LangChain, SQLite, and a focused browser interface.

![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.50-FF4B4B?logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🚀 Live Demo

[Try the application](https://text-to-sql-app-ilnwyv6bb3qqpb2w6e47bw.streamlit.app/)

## 🎥 Video Demo

Watch a walkthrough of the Text-to-SQL workflow and application interface:

[![Watch the Text-to-SQL application demo](https://img.youtube.com/vi/9NiI0LlIcbY/maxresdefault.jpg)](https://youtu.be/9NiI0LlIcbY)

## 🎯 Problem

SQL can be a barrier for people who need quick answers from structured data. This project demonstrates a simple Text-to-SQL workflow: a user asks a question in English, the language model generates a query for a known schema, and the application returns the matching database rows.

## ✨ Features

- Converts English questions into SQLite queries.
- Uses the `EMPLOYEE` schema as context for SQL generation.
- Executes generated queries against the included `company.db` database.
- Displays both the generated SQL and returned rows.
- Reads credentials from environment variables or Streamlit secrets.
- Provides a responsive Streamlit interface with clear error feedback.

## 🔄 How It Works

```mermaid
flowchart LR
    A[User question] --> B[Streamlit interface]
    B --> C[LangChain prompt]
    C --> D[Groq: GPT-OSS 120B]
    D --> E[Generated SQL]
    E --> F[(SQLite company.db)]
    F --> G[Results in Streamlit]
```

1. The user enters a question in `app.py`.
2. A prompt supplies the `EMPLOYEE` table schema and example queries.
3. Groq's `openai/gpt-oss-120b` model returns SQL through LangChain's string parser.
4. Python's built-in `sqlite3` module executes the SQL against `company.db`.
5. Streamlit shows the generated query and result rows.

## 🧰 Technology

| Technology | Role |
| --- | --- |
| Python | Application and database logic |
| Streamlit | Interactive web interface |
| LangChain Core | Prompt composition and output parsing |
| LangChain Groq | Groq chat-model integration |
| Groq API | GPT-OSS 120B model inference |
| SQLite | Local sample employee database |
| python-dotenv | Local environment-variable loading |

## 🗃️ Database Schema

The application queries the `EMPLOYEE` table in `company.db`.

| Column | SQLite type | Description |
| --- | --- | --- |
| `EMP_ID` | `INT` | Employee identifier |
| `NAME` | `VARCHAR(25)` | Employee name |
| `DEPARTMENT` | `VARCHAR(25)` | Department name |
| `POSITION` | `VARCHAR(25)` | Job title |
| `SALARY` | `INT` | Salary value |
| `BONUS` | `INT` | Bonus value |

## 📁 Project Structure

```text
text-to-sql-streamlit/
├── app.py              # Streamlit entry point and Text-to-SQL pipeline
├── company.db          # Employee database used by the application
├── mydata.py           # Script that creates and populates company.db
├── database.py         # Separate student-database example
├── student.db          # Database created by database.py
├── Screenshot .png     # Application preview
├── requirements.txt    # Pinned runtime dependencies
├── LICENSE             # MIT License
└── README.md
```

## ⚙️ Installation

Requirements: Python 3.11 or newer and a [Groq API key](https://console.groq.com/keys).

```bash
git clone https://github.com/zouhour13/text-to-sql-streamlit.git
cd text-to-sql-streamlit
python -m venv .venv
```

Activate the environment on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Or on macOS/Linux:

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## 🔐 Configuration

For local development, create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

The `.env` file and `.streamlit/secrets.toml` are ignored by Git. Never commit the real key.

## ▶️ Run Locally

```bash
streamlit run app.py
```

Open the local URL printed by Streamlit, normally `http://localhost:8501`.

## 💡 Example

Ask:

```text
List all employees working in the IT department
```

The model is prompted to produce a query such as:

```sql
SELECT * FROM EMPLOYEE WHERE DEPARTMENT = "IT";
```

The generated SQL and matching rows are then displayed in the application.

## ☁️ Deploy to Streamlit Community Cloud

1. Push this repository to GitHub.
2. Sign in to [Streamlit Community Cloud](https://share.streamlit.io/).
3. Create an app with repository `zouhour13/text-to-sql-streamlit`, branch `main`, and entry point `app.py`.
4. In **Advanced settings → Secrets**, add:

   ```toml
   GROQ_API_KEY = "your_groq_api_key"
   ```

5. Deploy the app and review its logs for dependency or startup errors.

## ⚠️ Limitations

- The prompt is designed only for the included `EMPLOYEE` table.
- SQL generation depends on an external model and may occasionally produce invalid queries.
- Generated SQL is executed directly against the bundled SQLite database; this demonstration should not be connected to sensitive or production data without query validation and read-only database controls.
- The interface displays raw result tuples rather than a typed, paginated data table.
- A valid Groq API key and network access are required for query generation.

## 🛣️ Future Improvements

- Validate generated statements and allow only read-only queries.
- Derive prompt context automatically from the database schema.
- Add automated tests for SQL execution and error handling.
- Display results in a labeled dataframe and support CSV export.
- Add conversation history and example prompts.

## 🖼️ Preview

<p align="center">
  <img src="Screenshot%20.png" width="720" alt="Text-to-SQL Streamlit application preview">
</p>

## 👤 Author

**Zouhour Bellamine**  
AI & Data Engineer · Tunis, Tunisia

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.
