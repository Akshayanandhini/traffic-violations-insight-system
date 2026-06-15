import mysql.connector
import streamlit as st
import pandas as pd

def get_conn():
    conn = mysql.connector.connect(
        host="localhost",
        user="akshaya",
        password="221203",
        database="traffic_violations_db")
    return conn

@st.cache_data
def fetch_data(query,params = None):
    conn = get_conn()
    df = pd.read_sql(query,conn,params=params)
    conn.close()
    return df

