import streamlit as st

st.set_page_config(page_title="Welcome", page_icon="👋")

st.write("# Welcome to Market Dashboard!")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    **👈 Select a demo from the sidebar** to see some examples!
    ### Want to learn more?
    - Check out [baovest.github.io](https://baovest.github.io)
"""
)
