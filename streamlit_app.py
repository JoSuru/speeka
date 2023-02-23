import streamlit as st
from annotated_text import annotated_text
from streamlit_modal import Modal
from streamlit_ace import st_ace

st.set_page_config("Speeka", "💬", layout="wide")

with open('src/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 3, 1])

with col1:
    st.write("# Import  voice")
    with st.empty():
        file = st.file_uploader("Upload file", type=["wav", "mp3", "oga"])
    col_center1, button, col_center2 = st.columns([1, 1, 1])  # center button
    with button:
        if st.button("Transcribe"):
            st.write("Importing")

with col2:
    st.write("# Transcribe")

    tab1, tab2 = st.tabs(["Transcription", "✏️ Edit "])
    with tab2:
        content = st_ace(
            value='',
            theme='dracula',
            show_gutter=False,
        )
    with tab1:
        col_center1, text_transcribe, col_center2 = st.columns([1, 30, 1])  # center text
        with text_transcribe:
            annotated_text(
                content
            )
with col3:
    st.write("# More infos")
    st.write("Play audio")
    st.audio(file, format='audio/ogg')

modal = Modal("Demo Modal", "Abc")
if open_modal := st.button("Open"):
    modal.open()

if modal.is_open():
    with modal.container():
        st.write("Text goes here")
        st.write("Some fancy text")
        value = st.checkbox("Check me")
        st.write(f"Checkbox checked: {value}")
