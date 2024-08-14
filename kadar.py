import streamlit as st
import mysql.connector
import ast
import pandas as pd
import time as t
from streamlit_option_menu import option_menu
        
# df = pd.read_csv("redbus_project1.xls")
# df
    
st.set_page_config(
    page_title="Redbus",
    layout="wide"
)
st.image("rdc-redbus-logo.png",width = 100)
st.title("Kadar's RedBus Project")

web=option_menu(menu_title="🚌OnlineBus",
                options=["Home","📍All RTC Operator Directories"],
                icons=["house","info-circle"],
                orientation="horizontal"
                )
st.subheader("SQL database")
# Home page setting
if web=="Home":
    #st.image("t_500x300.jpg",width=200)
    st.title("Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit")
    st.subheader(":blue[Domain:]  Transportation")
    st.subheader(":blue[Ojective:] ")
    st.markdown("The 'Redbus Data Scraping and Filtering with Streamlit Application' aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry.")
    st.subheader(":blue[Overview:]") 
    st.markdown("Selenium: Selenium is a tool used for automating web browsers. It is commonly used for web scraping, which involves extracting data from websites. Selenium allows you to simulate human interactions with a web page, such as clicking buttons, filling out forms, and navigating through pages, to collect the desired data...")
    st.markdown('''Pandas: Use the powerful Pandas library to transform the dataset from CSV format into a structured dataframe.
                    Pandas helps data manipulation, cleaning, and preprocessing, ensuring that data was ready for analysis.''')
    st.markdown('''MySQL: With help of SQL to establish a connection to a SQL database, enabling seamless integration of the transformed dataset
                    and the data was efficiently inserted into relevant tables for storage and retrieval.''')
    st.markdown("Streamlit: Developed an interactive web application using Streamlit, a user-friendly framework for data visualization and analysis.")
    st.subheader(":blue[Skill-take:]")
    st.markdown("Selenium, Python, Pandas, MySQL,mysql-connector-python, Streamlit.")
    st.subheader(":blue[Developed-by:]  Kadar Meeran")

route_data = pd.read_csv("RTC_routes.csv")
data=pd.read_csv("redbus_project1.csv")
# Function to get routes for a particular RTC name
def get_routes(rtc_name):
    filtered_df = route_data[route_data['RTC Names'] == rtc_name]
    if not filtered_df.empty:
        routes = ast.literal_eval(filtered_df['Route Names'].values[0])
    if routes:
        return routes

# Function to get details for a particular route name
def get_route_details(route_name):
    filtered_df = data[data['Route Name'] == route_name]
    if not filtered_df.empty:
        return filtered_df
    else:
        return None

# States and Routes page setting
if web == "📍All RTC Operator Directories":
    S = st.selectbox("RTC Bus Operator",route_data["RTC Names"])
     
    if S:
        R = st.selectbox("Select Routes",get_routes(S))
    if R:
        rt = get_route_details(R)
        rt
    st.dataframe(buses)
    if buses is not None:
        st.write("Bus details for the selected route:")
        st.dataframe(buses)
    else:
        st.error("Sorry, no bus details found for the selected route.")
else:
    st.error("Sorry, no routes found for the selected RTC name.")
    TIME=st.time_input("select the time")
    st.select_slider("Price",["100","500","1000","2000","4000","6000","8000","10000","12000"])
    st.caption("Caption")
    st.checkbox("Bus Details")
    st.button("click")
    with st.spinner("please wait"):
        t.sleep(2)
    st.sidebar.radio("Choose bus type", ("SEATER","SEMI-SLEEPER","SLEEPER","AC","Non-Ac"))
    st.sidebar.radio("Choose bus fare range", ("0-1000", "1000-2000", "2000-5000","5000 and Above"))
    st.sidebar.title("Route Details")
    st.sidebar.text_input("Source")
    st.sidebar.text_input("Destination")
    st.sidebar.radio("Bus Timings",["Before 6 am Buses","6 am to 12 pm Buses","12 pm to 6 pm","After 6 pm"])
    st.sidebar.button("submit")

    st.error("Sorry No routes found")

    st.success("Data execution done")