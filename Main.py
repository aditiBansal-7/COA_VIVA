import streamlit as st

import psycopg2







st.title("PostgreSQL Connection with Streamlit through Docker")



DB_HOST = "my_postgres_container"

DB_NAME = "testdb"

DB_USER = "tarak"

DB_PASSWORD = "secret"



def fetch_data():

    try:

        st.write("Connecting to database...")

        conn = psycopg2.connect(

            host=DB_HOST,

            database=DB_NAME,

            user=DB_USER,

            password=DB_PASSWORD

        )

        st.write("<p class='success'> Connected to PostgreSQL!</p>", unsafe_allow_html=True)

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM passengers;")

        data = cursor.fetchall()

        cursor.close()

        conn.close()

        return data

    except Exception as e:

        st.write(f"<p class='error'> Database connection error: {str(e)}</p>", unsafe_allow_html=True)

        return []



data = fetch_data()



if data:

    st.subheader(" Data Retrieved:")

    for row in data:

        st.markdown(f"""

            <div class="card">

                <p class="data"><strong> ID:</strong> {row[0]} <strong>🏷 Name:</strong> {row[1]} <strong>📍 Location:</strong> {row[2]}</p>

            </div>

        """, unsafe_allow_html=True)

else:

    st.markdown("<p class='warning'>⚠ No data found in the passengers table.</p>", unsafe_allow_html=True)