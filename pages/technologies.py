import streamlit as st

# styles
# column-styles
st.markdown('<style>[data-testid="stColumn"]{ background-color: #2b3d645b; border: solid 2px #2b3d645b;}</style>', unsafe_allow_html=True)

# header
st.header("Technical Skills")
st.title("", anchor="line")

# columns 1
col1, col2, col3, col4, col5 = st.columns(5, border=True, width=950)
with col1:
    st.image(r"Streamlit\my_portfolio\images\excel.png")
with col2:
    st.image(r"Streamlit\my_portfolio\images\mysql.png")
with col3:
    st.image(r"Streamlit\my_portfolio\images\server.png")
with col4:
    st.image(r"Streamlit\my_portfolio\images\python.png")
with col5:
    st.image(r"Streamlit\my_portfolio\images\numpy.png")

# columns 2
col1, col2, col3, col4, col5 = st.columns(5, border=True, width=950)
with col1:
    st.image(r"Streamlit\my_portfolio\images\st.png")
with col2:
    st.image(r"Streamlit\my_portfolio\images\pandas.png")
with col3:
    st.image(r"Streamlit\my_portfolio\images\matplot.png")
with col4:
    st.image(r"Streamlit\my_portfolio\images\plotly.png")
with col5:
    st.image(r"Streamlit\my_portfolio\images\scikit.png")

# columns 3
col1, col2, col3, col4, col5 = st.columns(5, border=True, width=950)
with col1:
    st.image(r"Streamlit\my_portfolio\images\seaborn.png")
with col2:
    st.image(r"Streamlit\my_portfolio\images\mpl.png")
with col3:
    st.image(r"Streamlit\my_portfolio\images\etl.png")
with col4:
    st.image(r"Streamlit\my_portfolio\images\datastory.png")
with col5:
    st.image(r"Streamlit\my_portfolio\images\tensor.png")

st.title("")
st.header("Soft Skills & Competencies")
st.title("", anchor="line")

# columns 1
col1, col2, col3, col4 = st.columns(4, border=True, width=950)
with col1:
    st.markdown('<p style="text-align: center;">Teamwork & Stakeholder Management</p>',
                unsafe_allow_html=True)
with col2:
    st.markdown('<p style="text-align: center;">Forecasting and Predictive Analytics</p>',
                unsafe_allow_html=True)
with col3:
    st.markdown('<p style="text-align: center;">Time Series Analysis & Financial Modeling</p>',
                unsafe_allow_html=True)
with col4:
    st.markdown('<p style="text-align: center;">Data Quality Assurance</p>',
                unsafe_allow_html=True)

# columns 1
col1, col2, col3, col4 = st.columns(4, border=True, width=950)
with col1:
    st.markdown('<p style="text-align: center;">Statistical Reporting & Support</p>',
                unsafe_allow_html=True)
with col2:
    st.markdown('<p style="text-align: center;">Problem-Solving & Insight Generation</p>',
                unsafe_allow_html=True)
with col3:
    st.markdown('<p style="text-align: center;">Machine Learning & Regression Analysis</p>',
                unsafe_allow_html=True)
with col4:
    st.markdown('<p style="text-align: center;">Data Storytelling & Communication</p>',
                unsafe_allow_html=True)
