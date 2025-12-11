import streamlit as st

#風船アニメーション追加
with st.echo(code_location="below"):
    st.title(":red[風船アニメーション]")
    st.balloons()

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

