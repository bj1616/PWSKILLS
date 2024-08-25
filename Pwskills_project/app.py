import streamlit as st
import pandas as pd
import pickle
import numpy as np

model = pickle.load(open("model.pkl",'rb'))
df = pickle.load(open("main.pkl",'rb'))

USERNAME = "user"
PASSWORD = "password"

# Initialize session state if it doesn't exist
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Define the login function
def login(username, password):
    if username == USERNAME and password == PASSWORD:
        st.session_state['logged_in'] = True
        st.success("Login successful!")
    else:
        st.session_state['logged_in'] = False
        st.error("Invalid username or password")

# Define the logout function
def logout():
    st.session_state['logged_in'] = False
    st.success("You have been logged out")

# Display the login page if the user is not logged in
if not st.session_state['logged_in']:
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        login(username, password)

# Display the prediction model page if the user is logged in
if st.session_state['logged_in']:

    st.header("Oil Price Predictor(In USD)")

    date = st.text_input("Date")

    month = st.slider("Month",1,12)

    year = st.slider("Year",2000,2050)

    st.subheader("Click below to predict tomorrow's oil prices today!")


    if st.button("Predict Price"):
        values = np.array([date,month,year])
        values = values.reshape(1,-1)
        st.title(model.predict(values))

    if st.button("Log Out"):
        logout()
    st.feedback("thumbs")

    st.image("https://media.istockphoto.com/id/1330124688/photo/gasoline-fuel-nozzle-and-cash-money-gas-price-tax-ethanol-and-fossil-fuel-concept.jpg?s=612x612&w=0&k=20&c=ylQgTvpQs97yLGzhzCHXvwY5UH4l3xN970-l0AEl-_c=")
