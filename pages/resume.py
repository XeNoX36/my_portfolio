import streamlit as st
from PIL import Image

# styles
# download button-style
st.markdown("""<style>[data-testid="stButton"]>[data-testid="stBaseButton-secondary"]{ background-color: #1d7bb975; border: solid 1px #105a8b;
            cursor: pointer; border-radius: 12px; transition: background-color 0.3s ease-in-out;}</style>""", unsafe_allow_html=True)

st.markdown("""<style>[data-testid="stButton"]>[data-testid="stBaseButton-secondary"]:hover{ background-color: #1d7bb9;}</style>""", unsafe_allow_html=True)

st.markdown("""<style>[data-testid="stBaseButton-secondary"]>[data-testid="stMarkdownContainer"]>p{ font-size: 15px;font-weight: 600;
            padding: 0px;}</style>
            """, unsafe_allow_html=True)

image1 = "resume1.png"
image2 = "resume2.png"

images = [Image.open(image1), Image.open(image2)]
if "current_image_index" not in st.session_state:
    st.session_state.current_image_index = 0

col1, col2, col3 = st.columns([1, 3.7, 1])

if col1.button("< Previous"):
    st.session_state.current_image_index = (st.session_state.current_image_index - 1) % len(images)

if col3.button("Next >"):
    st.session_state.current_image_index = (st.session_state.current_image_index + 1) % len(images)

col2.image(images[st.session_state.current_image_index], width="stretch")

# --- Buttons ---
st.download_button("**Resume**", data="Adelaja Sam - Resume.pdf",
                   file_name="Adelaja Sam - Resume.pdf", mime="application/pdf",
                   on_click="ignore", icon=":material/download:")


