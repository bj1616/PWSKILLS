**Oil Price Prediction Model**

This repository contains a machine learning model for predicting oil prices based on historical data. The model uses various features such as date, month, and year to forecast future oil prices. The model is deployed as an interactive web application using Streamlit Cloud.

**Table of Contents**
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Model Details](#model-details)
6. [Deployment](#deployment)
7. [Results](#results)
8. [Contributing](#contributing)

**Introduction**
The Oil Price Prediction Model is designed to forecast future oil prices using historical data. Predicting oil prices is crucial for industries like energy, finance, and economics, as it can influence investment decisions, policy-making, and more. This model leverages machine learning techniques to provide accurate predictions.

**Features**
- **Interactive Prediction**: Users can input specific dates (day, month, year) and receive a predicted oil price.
- **Streamlit Deployment**: The model is deployed on Streamlit Cloud, making it easy to use through a web interface.
- **User Authentication**: The app includes a login/register page to ensure secure access to the prediction tool.

**Installation**
To run this project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/oil-price-prediction.git
    cd oil-price-prediction
    ```

2. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

4. **Access the app**:
   - The app will run locally on "http://localhost:8501/".
   - Enter your credentials or register to use the prediction model.

**Usage**

1. **Launch the Web App**:
   - The app is deployed on Streamlit Cloud. You can access it .
   
2. **Predicting Oil Prices**:
   - After logging in, input the date, month, and year for which you want to predict the oil price.
   - Click the "Predict" button to see the forecasted price.


**Model Details**
- **Algorithm Used**: Decision Tree
- **Training Data**: Historical oil price data, including features such as date, month, year, and possibly external economic indicators of USA.
- **Evaluation Metrics**: Root Mean Squared Error (RMSE)

**Deployment**
The application is deployed on Streamlit Cloud, ensuring it is accessible from any device with an internet connection. The deployment process involved:

1. Creating a Streamlit app (`app.py`).
2. Packaging the model using `pickle`.
3. Uploading the code and model files to Streamlit Cloud.
4. Configuring the app to load the model and respond to user inputs.

**Results**
The model provides predictions with a high degree of accuracy.

**Contributing**
Contributions are welcome! If you have suggestions or improvements, please create an issue or submit a pull request.


Feel free to customize this template to better fit your project specifics and personal style.
