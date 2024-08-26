import streamlit as st
import pandas as pd
import pickle
import numpy as np
import firebase_admin
from firebase_admin import credentials, auth

# Load the model and data
model = pickle.load(open("Pwskills_project/model.pkl", 'rb'))
df = pickle.load(open("main.pkl", 'rb'))

# Initialize Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate("oil-predictor-4fb9fbbcbec5.json")
    firebase_admin.initialize_app(cred)

# Function to handle user login
def login_user(email, password):
    try:
        # Placeholder for Firebase authentication logic
        # Assuming successful login for demonstration
        st.session_state['logged_in'] = True
        st.session_state['email'] = email
        return True
    except Exception as e:
        st.error(f"Login failed: {e}")
        return False

# Function to handle user logout
def logout_user():
    st.session_state['logged_in'] = False
    st.success("You have been logged out.")

# Define the app
def app():
    st.title("User Registration and Login")

    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if st.session_state['logged_in']:
        # Prediction UI
        st.subheader("Predict Oil Prices")
        
        date = st.text_input("Date (in YYYYMMDD format)")
        month = st.slider("Month", 1, 12)
        year = st.slider("Year", 2000, 2050)

        if st.button("Predict Price"):
            try:
                # Prepare the input for the model
                values = np.array([int(date), month, year])
                values = values.reshape(1, -1)

                # Make the prediction
                prediction = model.predict(values)

                st.subheader("Predicted Oil Price")
                st.write(f"Predicted Price: ${prediction[0]:.2f}")
            except Exception as e:
                st.error(f"Prediction failed: {e}")

        if st.button("Logout"):
            logout_user()

        st.feedback("thumbs")
        st.image("https://media.istockphoto.com/id/1330124688/photo/gasoline-fuel-nozzle-and-cash-money-gas-price-tax-ethanol-and-fossil-fuel-concept.jpg?s=612x612&w=0&k=20&c=ylQgTvpQs97yLGzhzCHXvwY5UH4l3xN970-l0AEl-_c=")

    else:
        menu = ["Login", "Register"]
        choice = st.selectbox("Select Action", menu)

        if choice == "Register":
            st.subheader("Create a New Account")

            email = st.text_input("Email Address")
            password = st.text_input("Password", type="password")
            username = st.text_input("Username")

            if st.button("Register"):
                try:
                    # Create a new user
                    user = auth.create_user(
                        email=email,
                        password=password,
                        display_name=username
                    )
                    st.success(f"Account created successfully for {user.display_name}. Please log in.")
                except Exception as e:
                    st.error(f"Error: {e}")

        elif choice == "Login":
            st.subheader("Login to Your Account")

            email = st.text_input("Email Address")
            password = st.text_input("Password", type="password")

            if st.button("Login"):
                login_user(email, password)
                    

# Run the app
if __name__ == "__main__":
    app()
