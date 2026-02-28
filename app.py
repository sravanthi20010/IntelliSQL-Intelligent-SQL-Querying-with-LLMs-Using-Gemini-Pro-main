import streamlit as st
import os
import sqlite3
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv('API_KEY'))

# Prompt for Gemini
prompt = ["""
You are an expert in converting English questions to SQL query!
The SQL database has the name STUDENTS and has the following columns - NAME, CLASS, Marks, Company.

Example 1: How many entries of records are present?
SQL: SELECT COUNT(*) FROM STUDENTS;

Example 2: Tell me all the students studying in MCom class?
SQL: SELECT * FROM STUDENTS WHERE CLASS="MCom";
"""]

def get_response(que, prompt):
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content([prompt[0], que])
    return response.text

def read_query(sql, db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return rows

def page_home():
    st.markdown("""
        <style>
        body { background-color: #2E2E2E; }
        .title { color: lightgreen; text-align: center; font-size: 32px; margin-top: 20px; }
        .subtitle { color: lightgreen; text-align: center; font-size: 20px; }
        .offerings { color: white; font-size: 16px; margin-top: 10px; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='title'>Welcome to IntelliSQL!</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Revolutionizing Database Querying with Advanced LLM Capabilities</div>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])
    with col1:
        # Database icon
        st.image("https://cdn-icons-png.flaticon.com/512/2721/2721297.png", width=150)

    with col2:
        st.markdown("""
            <div class='offerings'>
            <ul>
            <li>🔍 Intelligent Query Assistance</li>
            <li>📊 Data Exploration</li>
            <li>⚡ Efficient Data Retrieval</li>
            <li>🚀 Performance Optimization</li>
            <li>💡 SQL Syntax Suggestions</li>
            <li>📈 Trend & Pattern Analysis</li>
            </ul>
            </div>
        """, unsafe_allow_html=True)

def page_about():
    st.markdown("""
        <style>
        .about-title { color: #39FF14; font-size: 28px; }
        .about-content { color: white; font-size: 18px; margin-top: 20px; }
        </style>
    """, unsafe_allow_html=True)
    st.markdown("<div class='about-title'>About IntelliSQL</div>", unsafe_allow_html=True)
    st.markdown("""
        <div class='about-content'>
        IntelliSQL is an innovative project aimed at revolutionizing database querying using advanced Language Model capabilities.
        Powered by cutting-edge LLM (Large Language Model) architecture, this system offers users an intelligent platform for interacting with SQL databases effortlessly and intuitively.
        </div>
    """, unsafe_allow_html=True)
    st.image("https://cdn.iconscout.com/icon/free/png-256/oracle-226075.png", width=180)

def page_intelligent_query_assistance():
    st.markdown("""
        <style>
        .query-title { color: #39FF14; font-size: 26px; }
        .query-desc { color: white; font-size: 16px; margin-bottom: 20px; }
        </style>
    """, unsafe_allow_html=True)
    st.markdown("<div class='query-title'>Intelligent Query Assistance</div>", unsafe_allow_html=True)
    st.markdown("<div class='query-desc'>IntelliSQL enhances the querying process by providing intelligent assistance to users. Whether they are novice or experienced SQL users, IntelliSQL guides them through crafting complex queries with ease. By understanding natural language queries, IntelliSQL suggests relevant SQL statements, offers syntax suggestions, and assists in optimizing query performance, thereby streamlining the database interaction experience.</div>", unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])
    with col1:
        user_input = st.text_input("Enter Your Query:")
        if st.button("Get Answer"):
            if user_input.strip() == "":
                st.warning("Please enter a valid question.")
            else:
                sql = get_response(user_input, prompt)
                st.markdown(f"**Generated SQL Query:** `{sql}`")
                try:
                    result = read_query(sql, "data.db")
                    st.markdown("**The Response is:**")
                    st.table(result)
                except Exception as e:
                    st.error(f"❌ Error: {e}")
    with col2:
        st.image("https://img.icons8.com/color/480/artificial-intelligence.png", width=220)
        # Database icon
        st.image("https://cdn-icons-png.flaticon.com/512/2721/2721297.png", width=120)

def main():
    st.set_page_config(page_title="IntelliSQL", page_icon="🌟", layout="wide")
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "About", "Intelligent Query Assistance"])
    if page == "Home":
        page_home()
    elif page == "About":
        page_about()
    elif page == "Intelligent Query Assistance":
        page_intelligent_query_assistance()

if __name__ == "__main__":
    main()
