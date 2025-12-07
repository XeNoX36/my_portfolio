import streamlit as st

# styles
# body-stles
st.markdown('<style>div.block-container{padding-left:8rem; padding-right:7rem;}</style>', unsafe_allow_html=True)

# columns-styles
st.markdown('<style>[data-testid="stColumn"]{background-color: #2b3d645b; border: solid 1px #4e628f75;}</style>', unsafe_allow_html=True)

# test-styles
st.markdown('<style>[data-testid="stText"]>div{color: #d1cdcd; font-size: 14px; padding-left: 4.5px;}</style>', unsafe_allow_html=True)


# header
st.header("Project Experiences")
st.title("", anchor="line")

# columns 1
col1, col2, col3 = st.columns(3, border=True)
with col1:
    st.markdown("#### Cuisine Coffee Sales Analysis Using SQL")
    st.text("Conducted an extensive analysis on Coffee sales across five different cuisines, identifying key trends in customer demography, "
            "purchase history, orders, potential high value customers and provided insights.")
    st.markdown('<span style="background-color: #3e6077; padding: 3px 9px 3px 10px; border-radius: 20px;">SQL **|** Data Analysis  **|** SQL Server</span>',
                unsafe_allow_html=True)
    st.write("[**View Project**](https://github.com/XeNoX36/Cuisine-Orders-SQL-Project/blob/main/README.md)")
with col2:
    st.markdown("#### Walmart Sales Analysis Using SQL and Python")
    st.text("Utilized both python and SQL in this project. with Python the data was retrieved via an API while thorough exploratory analysis of market sales "
            "was accomplished using MySQL.")
    st.markdown('<span style="background-color: #3e6077; padding: 3px 10px 3px 10px; border-radius: 20px;">SQL  **|** SQL Server **|** Python **|** ETL Pipeline</span>',
                unsafe_allow_html=True)
    st.write("[**View Project**](https://github.com/XeNoX36/Walmart-sales/blob/main/README.md)")
with col3:
    st.markdown("#### MTN Churn Analysis Dashboard Using Python")
    st.text("Analyzed the major reasons for customer churn in a telecommunication company during the first-quater of the year 2025, using an interactive dashboard "
            "web-app I created using streamlit.")
    st.markdown('<span style="background-color: #3e6077; padding: 3px 10px 3px 10px; border-radius: 20px;">Streamlit **|** Python **|** Visualization</span>',
                unsafe_allow_html=True)
    container = st.container(border=False, horizontal=True)
    container.write("[**View Project**](https://github.com/XeNoX36/MTN_Site.github.io/blob/main/README.md)")
    container.write("[**View Dashboard**](https://mtnchurnapp.streamlit.app/)")

# columns 2
col1, col2, col3 = st.columns(3, border=True)
with col1:
    st.markdown("#### Retail Strategy and Analytics on Chips Sales")
    st.markdown('<span style="font-size: 14px; padding: 0px 0px 0px 0px;">**Virtual Internship Program**</span>',
                unsafe_allow_html=True)
    st.text("Conducted a detailed analysis on the sales of various chips product within a particular period, to uncover significant market trends, identify "
            "growth in stores and develop insights to improve sales.")
    st.markdown('<span style="background-color: #3e6077; padding: 3px 9px 3px 10px; border-radius: 20px;">Python **|** Statistics **|** Visualization</span>',
                unsafe_allow_html=True)
    st.write("[**View Project**](https://github.com/XeNoX36/Quantium-Internship/blob/main/README.md)")

with col2:
    st.markdown("#### Coffee Sales Dashboard Using Excel")
    st.text("Developed an interactive dashboard in Microsoft Excel to visualize order and sales metrics, enabling efficient tracking and analysis of coffee sales "
            "performance.")
    st.markdown('<span style="background-color: #3e6077; padding: 3px 10px 3px 10px; border-radius: 20px;">Excel **|** Data Analysis **|** Visualization</span>',
                unsafe_allow_html=True)
    container = st.container(border=False, horizontal=True)
    container.write("[**View Project**](https://github.com/XeNoX36/Coffee-Sales-Dashboard/blob/main/README.md)")
    with open("coffeeOrdersData tutorial.xlsx", "rb") as f:
      excel_file = f.read()
    container.download_button("**View Dashboard**", data=excel_file,
                              file_name="Coffee Sales Dashboard.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", on_click="ignore",
                              help="Download excel sheet to view dasboard")

with col3:
    st.markdown("#### Twitter Sentiment Analysis - ML")
    st.text("Performed sentiment analysis on over 50,000 tweets using advanced machine learning techniques. Deployed the best-performing model to predict and classify user's "
            "tweets into different sentiment categories.")
    st.markdown('<span style="background-color: #3e6077; padding: 3px 10px 3px 10px; border-radius: 20px;">Python **|** Pandas **|** Machine Learning</span>',
                unsafe_allow_html=True)
    st.write("[**View Project**](https://github.com/XeNoX36/Twitter-Sentiment-Analysis/blob/main/README.md)")

# columns 3
col1, col2, col3 = st.columns(3, border=True)
with col1:
    st.markdown("#### Analysis of Netflix data using Python")
    st.text("Conducted a well detailed analysis on the different Netflix movies and TV-series, classifying their categories, casts, crews and ratings, to discover "
            "significant trends and insights.")
    st.markdown('<span style="background-color: #3e6077; padding: 3px 9px 3px 10px; border-radius: 20px;">Python **|** Pandas **|** Seaborn **|** Matplotlib</span>',
                unsafe_allow_html=True)
    st.write("[**View Project**](https://github.com/XeNoX36/Netflix-Analysis-Project/blob/main/README.md)")

with col2:
    st.markdown("#### Healthcare Analysis Using SQL")
    st.text("Analyzed a healthcare data uncovering insights within key features such as the revenues, patient demographics, healthworkers information, medications and treatments "
            "performance.")
    st.markdown('<span style="background-color: #3e6077; padding: 3px 10px 3px 10px; border-radius: 20px;">SQL **|** Data Analysis **|** SQL Server</span>', unsafe_allow_html=True)
    st.write("[**View Project**](https://github.com/XeNoX36/Health-Care/blob/main/README.md)")

with col3:
    st.markdown("#### Analysis of Newyork's AirBnB Listing in 2024 using Python")
    st.text("Performed comprehensive data analysis on a AirBnB listings dataset using Python, uncovering insights into Locations, availabilities, pricing, "
            "customer reviews, ratings and market trends to support modern hotel industry research.")
    st.markdown('<span style="background-color: #3e6077; padding: 3px 10px 3px 10px; border-radius: 20px;">Python **|** Pandas **|** Seaborn **|** Matplotlib</span>',
                unsafe_allow_html=True)
    st.write("[**View Project**](https://github.com/XeNoX36/AirBnB-Analysis-Project/blob/main/README.md)")


# columns 4
col1, col2, col3 = st.columns(3, border=True)
with col1:
    st.markdown("#### Patient Profile Analysis Dashboard Using Python")
    st.text("Developed an interactive dashboard with streamlit to visualize patient health profile and metrics to uncover prevalent trends in medical conditions, "
            "bills, insurance, test results and patient behaviour.")
    st.markdown('<span style="background-color: #3e6077; padding: 3px 9px 3px 10px; border-radius: 20px;">Python **|** Streamlit **|** Visualization</span>',
                unsafe_allow_html=True)
    container = st.container(border=False, horizontal=True)
    container.write("[**View Project**](https://github.com/XeNoX36/Patient-Profile-Analysis/blob/main/README.md)")
    container.write("[**View Dashboard**](https://patient-profile-analysis.streamlit.app/)")

with col2:
    st.markdown("#### Analysis on the Mental Health of Students in Asia Using SQL")
    st.text("Conducted a study on the mental health condition of various students studying in Asia, analyzed how certain behavioral and demographic factors "
            "influenced suicidal tendencies in students.")
    st.markdown('<span style="background-color: #3e6077; padding: 3px 10px 3px 10px; border-radius: 20px;">SQL **|** Data Analysis **|** SQL Server</span>',
                unsafe_allow_html=True)
    st.write("[**View Project**](https://github.com/XeNoX36/Students-Mental-Health/blob/main/README.md)")

with col3:
    st.markdown("#### Automated Cryptocurrency ETL and Reporting System")
    st.text("Developed a data tracker that downloads over 250 crytocurrency data of the best and worst currencies of each day through a CoinGecko API. The data is automatically "
            "refreshed for each day and sent as an email.")
    st.markdown('<span style="background-color: #3e6077; padding: 3px 10px 3px 10px; border-radius: 20px;">Python **|** ETL **|** Email Automation </span>',
                unsafe_allow_html=True)
    st.write("[**View Project**](https://github.com/XeNoX36/Crypto-Automation-and-ETL-Project/blob/main/README.md)")


# columns 5
col1, col2, col3 = st.columns(3, border=True)
with col1:
    st.markdown("#### Analysis and Prediction of Electricity Distribution - ML")
    st.text("Analyzed a time series data that contained power demand influenced by factors such as seasons, festivals, humidity and temperature, to understand and predict "
            "the distribution of electricity.")
    st.markdown('<span style="background-color: #3e6077; padding: 3px 9px 3px 10px; border-radius: 20px;">Python **|** Time-Series **|** Machine Learning</span>',
                unsafe_allow_html=True)
    st.write("[**View Project**](https://github.com/XeNoX36/Electricity-Distribution-Prediction/blob/main/README.md)")

with col2:
    st.markdown("#### California Real Estate Predictive Modeling - ML ")
    st.text("Analyzed California housing data of the 1990s to determine the impact of geographic, demographic, and economic factors on median house values, identifying median income and regional density as major value drivers.")
    st.markdown('<span style="background-color: #3e6077; padding: 3px 10px 3px 10px; border-radius: 20px;">Python **|** Machine Learning</span>',
                unsafe_allow_html=True)
    container = st.container(border=False, horizontal=True)
    container.write("[**View Project**](https://github.com/XeNoX36/California-Real-Estate-Predictive-Modeling/blob/main/README.md)")

with col3:
    st.markdown("#### Student's SAT Performance Analysis Using SQL")
    st.text("Performed a comprehensive study on the distributions of SAT scores in different racial class of students across several American schools, to better understand the "
            "impact of race in student performance.")
    st.markdown('<span style="background-color: #3e6077; padding: 3px 10px 3px 10px; border-radius: 20px;">SQL  **|** Data Analysis **|** SQL Server</span>',
                unsafe_allow_html=True)
    st.write("[**View Project**](https://github.com/XeNoX36/SAT-Scores-of-Students/blob/main/README.md)")

# columns 6
col1, col2, col3 = st.columns(3, border=True)
with col1:
    st.markdown("#### Euro 2024 Soccer Analysis App ")
    st.text("Deployed a web app that visualizes the shot-map for different teams and players that participated in the Euro 2024 Qualifiers.")
    st.markdown('<span style="background-color: #3e6077; padding: 3px 10px 3px 10px; border-radius: 20px;">Python **|** MPL-Soccer **|** Streamlit</span>',
                unsafe_allow_html=True)
    container = st.container(border=False, horizontal=True)
    container.write("[**View Project**](https://github.com/XeNoX36/SoccerLysis/blob/main/README.md)")
    container.write("[**View App**](https://soccerlysis-app.streamlit.app/)")

# styles
# view dashboad-styles
st.markdown("""<style>[data-testid="stBaseButton-secondary"]{ background-color: transparent; border: none;
            padding: 0 60px 15px 0px;}</style>""", unsafe_allow_html=True)
st.markdown("""<style>[data-testid="stBaseButton-secondary"]:hover{ background-color: transparent; border: none;
            color: white;}</style>""", unsafe_allow_html=True)
st.markdown("""<style>[data-testid="stBaseButton-secondary"]>[data-testid="stMarkdownContainer"]>p{ font-size: 16px;font-weight: 600;
            padding: 0px; color: #94cff7; transition: color 0.3s ease-in-out;}</style>
            """, unsafe_allow_html=True)
st.markdown("""<style>[data-testid="stBaseButton-secondary"]>[data-testid="stMarkdownContainer"]>p:hover{color: white; font-size: 16.3px;}</style>
            """, unsafe_allow_html=True)



