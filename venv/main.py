
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate  
import sqlite3
import streamlit as st


# Charger le fichier .env
load_dotenv() 


def get_sql_query(user_query):
    groq_sys_prompt = ChatPromptTemplate.from_template("""
                    You are an expert in converting English questions to SQL query!
                    The SQL database has the name STUDENT and has the following columns - NAME, COURSE, 
                    SECTION and MARKS. For example, 
                    Example 1 - How many entries of records are present?, 
                        the SQL command will be something like this SELECT COUNT(*) FROM STUDENT;
                    Example 2 - Tell me all the students studying in Data Science COURSE?, 
                        the SQL command will be something like this SELECT * FROM STUDENT 
                        where COURSE="Data Science"; 
                    also the sql code should not have ``` in beginning or end and sql word in output.
                    Now convert the following question in English to a valid SQL Query: {user_query}. 
                    No preamble, only valid SQL please
    
                                                  """)
    model="llama-3.3-70b-versatile"
    llm = ChatGroq(
    groq_api_key = os.environ.get("GROQ_API_KEY"),
    model_name=model
    )

    chain = groq_sys_prompt | llm | StrOutputParser()
    response = chain.invoke({"user_query": user_query})
    return response


def return_sql_response(sql_query):
    database = "student.db"
    with sqlite3.connect(database) as conn:
        return conn.execute(sql_query).fetchall()


def main():
    # Page configuration
    st.set_page_config(
        page_title="Text To SQL 🗄️", 
        page_icon="💬", 
        layout="centered", 
        initial_sidebar_state="expanded"
    )

    # Add a gradient background and some custom CSS
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .stButton>button {
            background-color: #6c63ff;
            color: white;
            font-size: 18px;
            border-radius: 10px;
            padding: 10px 20px;
            margin-top: 10px;
        }
        .stTextInput>div>div>input {
            color: #6c63ff;   
            border-radius: 10px;
            padding: 10px;
            font-size: 16px;
           
        }
        .stHeader {
            color: #6c63ff;
        }
        .result-row {
            background: #ffffffaa;
            color: #333;  /* <-- Add this line */
            padding: 15px;
            margin-bottom: 10px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
       
        </style>
        """, unsafe_allow_html=True
    )

    # Main header with emoji
    st.markdown("<h1 style='text-align:center; color:#6c63ff;'> Chat with Your Data !💬</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-size:18px; color:#333;'>Type your query in natural language and get SQL results instantly!</p>", unsafe_allow_html=True)

    # User input section
    st.markdown("<style>label[for^='text_input'] {color:#6c63ff !important; font-weight:bold; font-size:18px;}</style>", unsafe_allow_html=True)
    user_query = st.text_input("Enter your query here:")
    submit = st.button("🚀 Execute")

    if submit and user_query.strip():
        try:
            # Generate SQL and get results
            sql_query = get_sql_query(user_query)
            retrieved_data = return_sql_response(sql_query)

            # Show SQL query in an info box
            st.info(f"Generated SQL Query: `{sql_query}`")

            # Display results beautifully

            st.markdown("<style>h2{color:#6c63ff;font-weight:bold;margin-bottom:15px}.result-row{background:#f8f9fc;padding:10px 15px;border-radius:10px;margin-bottom:10px;border:1px solid #e0e0e0;font-size:16px;color:#333}.result-row b{color:#6c63ff}</style>", unsafe_allow_html=True)
            st.markdown("<h2 style='color:#6c63ff; font-weight:bold;'>Query Results:</h2>", unsafe_allow_html=True)

            for i, row in enumerate(retrieved_data, start=1):
                st.markdown(f"<div class='result-row'><b>Row {i}:</b> {row}</div>", unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Oops! Something went wrong: {e}")

    # Footer / Creative touch
    st.markdown("---")
    st.markdown("<p style='text-align:center; color:#6c63ff;'>Made with ❤️ by Zouhour</p>", unsafe_allow_html=True)


if __name__ == '__main__':
    main()