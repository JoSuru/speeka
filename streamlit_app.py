import streamlit as st
from annotated_text import annotated_text
from streamlit_modal import Modal


st.set_page_config("Speeka", "💬", layout="wide")

with open('src/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 3, 1])

with col1:
    st.write("# Import  voice")
    with st.empty():
        file = st.file_uploader("Upload file", type=["wav", "mp3"])
    col_center1, button, col_center2 = st.columns([1, 1, 1])  # center button
    with button:
        if st.button("Transcribe"):
            st.write("Importing")

with col2:
    st.write("# Transcribe")
    col_center1, text_transcribe, col_center2 = st.columns([1, 30, 1])  # center text
    with text_transcribe:
        annotated_text(
            "This ",
            ("is", "verb", "#8ef"),
            " some ",
            ("annotated", "adj", "#faa"),
            ("text", "noun", "#afa"),
            " for those of ",
            ("you", "pronoun", "#fea"),
            " who ",
            ("like", "verb", "#8ef"),
            " this sort of ",
            ("thing", "noun", "#afa"),
        )
    if st.button("Edit"):
        st.write("Editing")

modal = Modal("Demo Modal", "Abc")
if open_modal := st.button("Open"):
    modal.open()

if modal.is_open():
    with modal.container():
        st.write("Text goes here")
        st.write("Some fancy text")
        value = st.checkbox("Check me")
        st.write(f"Checkbox checked: {value}")
