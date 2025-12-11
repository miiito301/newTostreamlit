from re import T
import streamlit as st

st.title("Hello World")
st.snow()
st.header("This is a header")
st.subheader(
    body="this is a subheader",
    anchor="title",
    help="this is a help",
    divider=True)

st.caption("this is a caption")
st.text("""
    this is a text
    this is a text""")
st.code("""
import streamlit as st
""")