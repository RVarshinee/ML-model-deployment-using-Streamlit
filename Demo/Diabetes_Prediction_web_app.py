import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('./trained_model.sav', 'rb'))

# creating a function for Prediction
def diabetes_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return '🚫 The person is not diabetic 🚫'
    else:
        return '✅ The person is diabetic ✅'


def main():
    # Add custom CSS for black background and white text
    st.markdown("""
        <style>
            body {
                background-color: black;
                color: black;
            }
            .css-1v3fvcr {
                color: white;
            }
            .streamlit-expanderHeader {
                color: white;
            }
            .stButton > button {
                color: black;
                background-color: light-blue;
            }
        </style>
        """, unsafe_allow_html=True)
    
    # giving a title with light blue color and emoji
    st.markdown("<h1 style='text-align: center; color: black;'>Diabetes Prediction Web App 🩺</h1>", unsafe_allow_html=True)
    
    # getting the input data from the user
    st.markdown("<h4 style='color: black;'>Enter the following details:</h4>", unsafe_allow_html=True)
    
    Glucose = st.text_input('🍭 Glucose Level')
    BloodPressure = st.text_input('💉 Blood Pressure value')
    SkinThickness = st.text_input('📏 Skin Thickness value')
    Insulin = st.text_input('💉 Insulin Level')
    BMI = st.text_input('⚖️ BMI value')
    DiabetesPedigreeFunction = st.text_input('🧬 Diabetes Pedigree Function value')
    Age = st.text_input('👵 Age of the Person')
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    if st.button('🔍 Diabetes Test Result'):
        diagnosis = diabetes_prediction([Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
    st.success(diagnosis)


if __name__ == '__main__':
    main()
   
