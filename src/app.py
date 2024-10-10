import streamlit as st
import pandas as pd
import plost

# Generelles Layout
st.set_page_config(layout="wide", initial_sidebar_state="expanded")

# Einfügen der CSS Komponenten
with open("Streamlit Dashboard/src/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar
st.sidebar.header("Dashboard `Prototyp`")

st.sidebar.subheader("Sector")
st.sidebar.markdown("Aerospace")

st.sidebar.subheader("Site")
st.sidebar.markdown("1")
st.sidebar.markdown("2")
st.sidebar.markdown("3")
st.sidebar.markdown("4")

# Sidebar Copyright Text
st.sidebar.markdown("""
---
Created with ❤️ by [Tim](https://github.com/Schulsprecher).
""")


# Row A
st.markdown("### Quoten")
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
