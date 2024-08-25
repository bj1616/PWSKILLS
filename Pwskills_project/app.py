import streamlit as st
import pandas as pd
import pickle
import numpy as np

model = pickle.load(open("model.pkl","rb"))
df = pickle.load(open("main.pkl","rb"))

st.header("Oil Price Predictor(In USD)")

date = st.text_input("Date")

month = st.slider("Month",1,12)

year = st.slider("Year",2000,2050)

st.subheader("Click below to predict tomorrow's oil prices today!")


if st.button("Predict Price"):
    values = np.array([date,month,year])
    values = values.reshape(1,-1)
    st.title(model.predict(values))

st.feedback("thumbs")

st.image("https://media.istockphoto.com/id/1330124688/photo/gasoline-fuel-nozzle-and-cash-money-gas-price-tax-ethanol-and-fossil-fuel-concept.jpg?s=612x612&w=0&k=20&c=ylQgTvpQs97yLGzhzCHXvwY5UH4l3xN970-l0AEl-_c=")
