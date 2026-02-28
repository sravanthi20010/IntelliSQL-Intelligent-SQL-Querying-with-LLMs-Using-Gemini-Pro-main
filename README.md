# IntelliSQL-Intelligent-SQL-Querying-with-LLMs-Using-Gemini-Pro
IntelliSQL is an AI-powered system that converts natural language queries into SQL using Gemini Pro LLM, enabling users to interact with databases without writing complex SQL queries.
Project Overview
Features
Natural Language to SQL: Converts English questions into accurate SQL queries using Gemini Pro.
Instant Data Retrieval: Executes generated queries and displays results in real time.
User-Friendly Interface: Streamlit-based UI with clear navigation and modern styling.
Sample Student Database: Pre-populated SQLite database for demonstration.
Secure API Key Management: Uses .env files to keep credentials safe.
Extensible Design: Easily adaptable for other databases or additional features.
Installation & Setup
Clone the Repository: git clone https://github.com/your-username/IntelliSQL.git cd IntelliSQL

Create and Activate a Virtual Environment: python -m venv myenv

Windows:
myenv\Scripts\activate

macOS/Linux:
source myenv/bin/activate

Install Dependencies: pip install -r requirements.txt

Set Up Environment Variables:

Copy .env.example to .env and add your Gemini API key: API_KEY=your_gemini_api_key_here
Initialize the Database: python 1.sql.py

Run the Application: streamlit run app.py

Open the provided local URL in your browser.
Usage Instructions
Home Page:

View project introduction and key features.
About Page:

Learn about the project’s purpose and technology stack.
Intelligent Query Assistance:

Enter a question in plain English (e.g., "Show all students in BTech").
Click Get Answer to see the generated SQL query and the database results.
Screenshots
Below are sample screenshots from the application placed in screenshots/ folder and referenced as shown.
