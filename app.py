
# import streamlit as st
# import numpy as np
# import pandas as pd
# import pickle

# # Load the instances that were created

# with open('model.pkl','rb') as file:
#     model = pickle.load(file)

# with open('pca.pkl','rb') as file:
#     pca = pickle.load(file)

# with open('scaler.pkl','rb') as file:
#     scaler = pickle.load(file)

# def prediction(input_data):

#     scaled_data = scaler.transform(input_data)
#     pca_data = pca.transform(scaled_data)

#     pred = model.predict(pca_data)[0]

#     if pred==0:
#         return 'Under-Developed'
#     elif pred==1:
#         return 'Developed'
#     else:
#         return 'Developing'

# def main():

#     st.title('HELP International Foundation')
#     st.subheader('This application will give the status of the country based on socio-economic factors')
#     ch_mort = st.text_input('Enter the child mortality rate:')
#     exp = st.text_input('Enter Exports (% GDP):')
#     imp = st.text_input('Enter Imports (% GDP):')
#     hel = st.text_input('Enter expenditure on health (% GDP):')
#     inc = st.text_input('Enter average income:')
#     inf = st.text_input('Enter Inflation:')
#     life_exp = st.text_input('Enter life expectancy:')
#     fer = st.text_input('Enter fertility rate:')
#     gdp = st.text_input('Enter GDP per population:')

#     input_list = [[ch_mort,exp,hel,imp,inc,inf,life_exp,fer,gdp]]

#     if st.button('Predict'):
#         response = prediction(input_list)
#         st.success(response)

# if __name__ == '__main__':
#     main()

import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load the instances that were created

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('pca.pkl', 'rb') as file:
    pca = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

def prediction(input_data):
    scaled_data = scaler.transform(input_data)
    pca_data = pca.transform(scaled_data)
    pred = model.predict(pca_data)[0]

    if pred == 0:
        return 'Under-Developed'
    elif pred == 1:
        return 'Developed'
    else:
        return 'Developing'

def main():
    # Custom styles for better aesthetics
    st.markdown(
        """
        <style>
        body {
            background-color: #eef2f3;
            font-family: 'Arial', sans-serif;
        }
        .main-container {
            max-width: 800px;
            margin: auto;
            background: #ffffff;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        }
        .header {
            text-align: center;
            margin-bottom: 20px;
        }
        .header h1 {
            font-size: 36px;
            color: #2a5d84;
        }
        .header p {
            font-size: 18px;
            color: #555555;
        }
        .form-container {
            margin-top: 20px;
        }
        .form-container .stButton button {
            background-color: #2a5d84;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            font-size: 16px;
        }
        .form-container .stButton button:hover {
            background-color: #1d4c6b;
        }
        .result {
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            color: #2a5d84;
            margin-top: 30px;
        }
        </style>
        <div class="main-container">
            <div class="header">
                <h1>HELP International Foundation</h1>
                <p>Predict the status of a country based on socio-economic factors</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Input form
    with st.form(key='input_form'):
        st.markdown("### Input Socio-Economic Data", unsafe_allow_html=True)
        st.write("Provide the required socio-economic metrics below:")

        # Organize input fields into two columns
        col1, col2 = st.columns(2)

        with col1:
            ch_mort = st.text_input('Child Mortality Rate:', '')
            exp = st.text_input('Exports (% GDP):', '')
            imp = st.text_input('Imports (% GDP):', '')
            hel = st.text_input('Expenditure on Health (% GDP):', '')

        with col2:
            inc = st.text_input('Average Income:', '')
            inf = st.text_input('Inflation:', '')
            life_exp = st.text_input('Life Expectancy:', '')
            fer = st.text_input('Fertility Rate:', '')
            gdp = st.text_input('GDP per Population:', '')

        input_list = [[ch_mort, exp, hel, imp, inc, inf, life_exp, fer, gdp]]

        # Submit button
        submit_button = st.form_submit_button(label='Predict')

        if submit_button:
            with st.spinner('Analyzing data and predicting...'):
                response = prediction(input_list)
            st.markdown(f"<div class='result'>The predicted status of the country is: {response}</div>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()


