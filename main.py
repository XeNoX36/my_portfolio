import streamlit as st

with open(r"portfolio.css", "r") as f:
    st.markdown(f"""<style>{f.read()}</style>""", unsafe_allow_html=True)

st.set_page_config(page_title="Adelaja Sam",
                   initial_sidebar_state="auto",
                   page_icon="",
                   layout="wide")
st.markdown('<style>div.block-container{padding:1.8rem; padding-left:15rem;}</style>', unsafe_allow_html=True)

# Nav bars
about = st.Page("pages/about.py", title="About")
technologies = st.Page("pages/technologies.py", title="Skills")
project = st.Page("pages/projects.py", title="Projects")
resume = st.Page("pages/resume.py", title="Resume")
pg = st.navigation([about, technologies, project, resume], position="top")
pg.run()

