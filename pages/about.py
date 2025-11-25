import streamlit as st

# Front page
st.title("")
st.title("")
st.title("Hi, i'm Sam", anchor="pdg")
st.markdown("### Data Analyst | Data App Developer | ML Engineer")
st.markdown("###### Transforming data into useful and interactive ideas.")

# --- Buttons ---
st.download_button("**Resume**", data="Adelaja Sam - Resume.pdf",
                   file_name="Adelaja Sam - Resume.pdf", mime="application/pdf",
                   on_click="ignore", icon=":material/download:")
# with col2:

st.title("")
st.title("")
st.header("About me")
st.title("", anchor="line")
col1, col2 = st.columns([0.4, 0.6])
with col1:
    st.image("images/Photo Sam.jpg", width=400)
with col2:
    st.write("Results-driven data analyst with an eye for detail and an open mind for learning. I am motivated to learn, grow and excel in my field. "
             "I have developed a strong foundation in statistical modeling, data extraction, exploration, visualization and interactive data app creation.")
    st.write("With my skills i have deliverd high-impact projects, including a **MTN Churn Prediction app** created using Python-Streamlit, "
             "which analyzes the major driving causes of churn for MTN during the first quarter of 2025 in Nigeria, "
             "highlighting regions affected and also providing useful insights.")
    st.write("I have also created several solution driven projects such as **Healthcare Patient Profile Analysis App** [Python], **Student Mental health Analysis** [SQL], "
             "**Twitter Sentiment Analysis - Machine Learning** [Python] among many others. I'm excited to collaborate with like-minded professionals and explore new opportunities "
             "in data analysis.")
    st.write("")
    st.write("")
    col1, col2, col3, col4, col5 = st.columns(5, gap="small", width=420)
    with col2:
        st.image("images/twitter_3670211.png")
        st.markdown('<p style="text-align: center; color: #94cff7; font-weight: bold;"><a href="https://x.com/adelajasamuel99">Twitter</a></p>',
                    unsafe_allow_html=True)
    with col3:
        st.image("images/social_16033412.png")
        st.markdown('<p style="text-align: center; color: #94cff7; font-weight: bold;"><a href="https://www.linkedin.com/in/adelajasamuel99">Linkedin</a></p>',
                    unsafe_allow_html=True)
    with col4:
        st.image("images/github_270798.png")
        st.markdown('<p style="text-align: center; color: #94cff7; font-weight: bold;"><a href="https://github.com/XeNoX36/">Github</a></p>',
                    unsafe_allow_html=True)
    with col5:
        st.image("images/email_3031693.png")
        st.markdown('<p style="text-align: center; color: #94cff7; font-weight: bold;"><a href="adelajasamuel99@gmail.com">Gmail</a></p>',
                    unsafe_allow_html=True)







